#!/usr/bin/env python3
"""Reformat Paradox (CK2) script in the house style.

Usage (from the mod root):
    python3 tools/events/pdxfmt.py events/X.txt [more files]   # rewrite in place
    python3 tools/events/pdxfmt.py --check events/X.txt        # exit 1 if not formatted

What it does:
- tabs for indentation, `key = value` with spaces;
- one statement per line, except short blocks with no comments, which stay on
  one line: `modifier = { factor = 0.5 trait = shy }`;
- keeps every comment, either at the end of its line or on its own line;
- keeps single blank lines where the source had them, drops runs of blanks;
- never changes the code itself: the script tokens before and after must match,
  or the file is left alone.
"""
import re
import sys

TOKEN = re.compile(r'"(?:[^"\\]|\\.)*"|[{}]|<=|>=|==|!=|[=<>]|#[^\n]*|[^\s{}=<>"#]+')
OPS = ('=', '<', '>', '<=', '>=', '==', '!=')

# Blocks that always open over several lines: event definitions at the top
# level, their main sections, and random lists anywhere.
EVENT_TYPES = {
    'character_event', 'province_event', 'letter_event', 'narrative_event',
    'long_character_event', 'society_quest_event', 'diploresponse_event', 'unit_event',
}
EVENT_SECTIONS = {'option', 'immediate', 'after', 'trigger', 'mean_time_to_happen', 'weight_multiplier'}
ALWAYS_OPEN = {'random_list'}
INLINE_WIDTH = 100
INLINE_ITEMS = 5


class Tok:
    __slots__ = ('text', 'line')

    def __init__(self, text, line):
        self.text = text
        self.line = line


class Item:
    """One statement: `key op value`, a bare value, or a comment line."""
    __slots__ = ('key', 'op', 'value', 'block', 'comment', 'open_comment', 'blank_before', 'line')

    def __init__(self):
        self.key = None          # str or None for a bare value
        self.op = None
        self.value = None        # scalar str when block is None
        self.block = None        # list of Item for a { block }
        self.comment = None      # trailing comment on the closing line
        self.open_comment = None  # comment right after `{`
        self.blank_before = False
        self.line = 0


def lex(text):
    out = []
    line = 1
    pos = 0
    for m in TOKEN.finditer(text):
        line += text.count('\n', pos, m.start())
        pos = m.start()
        out.append(Tok(m.group(0), line))
    return out


def parse(toks):
    pos = [0]
    n = len(toks)

    def block(depth):
        items = []
        last_line = None
        while pos[0] < n:
            t = toks[pos[0]]
            if t.text == '}':
                if depth == 0:
                    raise ValueError('unbalanced } on line %d' % t.line)
                return items, t
            if t.text.startswith('#'):
                # Trailing comment on the same line as the previous item's end.
                if items and last_line == t.line and items[-1].comment is None:
                    items[-1].comment = t.text
                else:
                    it = Item()
                    it.comment = t.text
                    it.line = t.line
                    it.blank_before = last_line is not None and t.line - last_line > 1
                    items.append(it)
                last_line = t.line
                pos[0] += 1
                continue
            it = Item()
            it.line = t.line
            it.blank_before = last_line is not None and t.line - last_line > 1
            if pos[0] + 1 < n and toks[pos[0] + 1].text in OPS:
                it.key = t.text
                it.op = toks[pos[0] + 1].text
                pos[0] += 2
                if pos[0] >= n:
                    raise ValueError('missing value on line %d' % t.line)
                t = toks[pos[0]]
                if t.text.startswith('#'):
                    raise ValueError('comment between `=` and its value on line %d' % t.line)
            if t.text == '{':
                pos[0] += 1
                open_line = t.line
                if pos[0] < n and toks[pos[0]].text.startswith('#') and toks[pos[0]].line == open_line:
                    it.open_comment = toks[pos[0]].text
                    pos[0] += 1
                it.block, close = block(depth + 1)
                last_line = close.line
                pos[0] += 1
            elif t.text == '}' or t.text in OPS:
                raise ValueError('unexpected %s on line %d' % (t.text, t.line))
            else:
                it.value = t.text
                last_line = t.line
                pos[0] += 1
            items.append(it)
        if depth:
            raise ValueError('unclosed { at end of file')
        return items, None

    items, _ = block(0)
    return items


def has_comment(items):
    for it in items:
        if it.comment or it.open_comment:
            return True
        if it.block is not None and has_comment(it.block):
            return True
    return False


def leaf_count(items):
    total = 0
    for it in items:
        total += leaf_count(it.block) if it.block is not None else 1
    return total


def inline(items):
    parts = []
    for it in items:
        head = '%s %s ' % (it.key, it.op) if it.key is not None else ''
        if it.block is not None:
            body = inline(it.block)
            parts.append(head + ('{ %s }' % body if body else '{ }'))
        else:
            parts.append(head + it.value)
    return ' '.join(parts)


def can_inline(it, indent):
    if it.key in ALWAYS_OPEN or it.open_comment or has_comment(it.block):
        return False
    if (indent == 0 and it.key in EVENT_TYPES) or (indent == 1 and it.key in EVENT_SECTIONS):
        return False
    if leaf_count(it.block) > INLINE_ITEMS:
        return False
    head = '%s %s ' % (it.key, it.op) if it.key is not None else ''
    return indent * 4 + len(head) + len(inline(it.block)) + 4 <= INLINE_WIDTH


def emit(items, indent, out, top=False):
    pad = '\t' * indent
    for i, it in enumerate(items):
        if it.blank_before and i > 0 and not top:
            out.append('')
        if it.key is None and it.value is None and it.block is None:  # comment line
            out.append(pad + it.comment)
            continue
        head = '%s %s ' % (it.key, it.op) if it.key is not None else ''
        tail = (' ' + it.comment) if it.comment else ''
        if it.block is None:
            out.append(pad + head + it.value + tail)
        elif not it.block and not it.open_comment:
            out.append(pad + head + '{ }' + tail)
        elif can_inline(it, indent):
            out.append(pad + head + '{ ' + inline(it.block) + ' }' + tail)
        else:
            out.append(pad + head + '{' + ((' ' + it.open_comment) if it.open_comment else ''))
            emit(it.block, indent + 1, out)
            out.append(pad + '}' + tail)


def code_tokens(text):
    return [t.text for t in lex(text) if not t.text.startswith('#')]


def comments(text):
    return [t.text.rstrip() for t in lex(text) if t.text.startswith('#')]


def format_text(text):
    """Return the formatted text. Raises ValueError if the result would change the code."""
    items = parse(lex(text))
    out = []
    emit(items, 0, out, top=False)
    result = '\n'.join(line.rstrip() for line in out) + '\n'
    if code_tokens(result) != code_tokens(text):
        raise ValueError('formatting would change the code')
    if comments(result) != comments(text):
        raise ValueError('formatting would change the comments')
    return result


def main(argv):
    check = '--check' in argv
    paths = [a for a in argv[1:] if not a.startswith('--')]
    bad = 0
    for path in paths:
        raw = open(path, 'rb').read()
        text = raw.decode('cp1252')
        crlf = '\r\n' in text
        text = text.replace('\r\n', '\n')
        try:
            new = format_text(text)
        except ValueError as e:
            print('%s: %s' % (path, e))
            bad += 1
            continue
        if new != text:
            if check:
                print('%s: not formatted' % path)
                bad += 1
            else:
                if crlf:
                    new = new.replace('\n', '\r\n')
                open(path, 'wb').write(new.encode('cp1252'))
                print('formatted %s' % path)
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
