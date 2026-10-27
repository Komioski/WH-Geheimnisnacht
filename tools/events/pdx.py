"""Small reader for Paradox (CK2) script files.

Used by build_event_db.py and check_events.py. Standard library only.

parse(text) returns a list of entries (key, op, value, line). value is a
string, or a list of entries when the right-hand side is a { block }.
Bare values inside a block (e.g. lists of event ids) have key None.
"""
import os
import re

TOKEN = re.compile(r'"(?:[^"\\]|\\.)*"|[{}]|<=|>=|==|!=|[=<>]|[^\s{}=<>"#]+|#[^\n]*')
OPS = ('=', '<', '>', '<=', '>=', '==', '!=')

# Event-firing effects, e.g. character_event = { id = x.1 }
EVENT_CALL = re.compile(
    r'^(character|province|letter|narrative|long_character|diploresponse|society_quest|unit'
    r'|planned_character|planned_province)_event$|^repeat_event$')


def read(path):
    """Return (text, encoding). CK2 reads cp1252; utf-8 files are reported as such."""
    raw = open(path, 'rb').read()
    bom = raw.startswith(b'\xef\xbb\xbf')
    if bom:
        raw = raw[3:]
    try:
        text = raw.decode('ascii')
        return text, 'ascii'
    except UnicodeDecodeError:
        pass
    try:
        text = raw.decode('utf-8')
        return text, 'utf-8-bom' if bom else 'utf-8'
    except UnicodeDecodeError:
        return raw.decode('cp1252', errors='replace'), 'cp1252'


def tokens(text):
    """Yield (token, line) skipping comments."""
    line = 1
    pos = 0
    for m in TOKEN.finditer(text):
        line += text.count('\n', pos, m.start())
        pos = m.start()
        t = m.group(0)
        if t[0] != '#':
            yield t, line


def parse(text):
    """Return (entries, brace_errors)."""
    toks = list(tokens(text))
    root = []
    stack = [root]
    errors = 0
    i, n = 0, len(toks)
    while i < n:
        t, line = toks[i]
        if t == '}':
            if len(stack) > 1:
                stack.pop()
            else:
                errors += 1
            i += 1
            continue
        if t == '{':
            block = []
            stack[-1].append((None, '', block, line))
            stack.append(block)
            i += 1
            continue
        if i + 1 < n and toks[i + 1][0] in OPS:
            op = toks[i + 1][0]
            if i + 2 < n:
                v = toks[i + 2][0]
                if v == '{':
                    block = []
                    stack[-1].append((t, op, block, line))
                    stack.append(block)
                else:
                    stack[-1].append((t, op, v.strip('"'), line))
                i += 3
                continue
            i += 2
            continue
        stack[-1].append((None, '', t.strip('"'), line))
        i += 1
    return root, errors + len(stack) - 1


def walk(block, depth=0):
    for k, op, v, line in block:
        yield k, op, v, line, depth
        if isinstance(v, list):
            yield from walk(v, depth + 1)


def get(block, key, default=None):
    for k, op, v, line in block:
        if k == key:
            return v
    return default


def getall(block, key):
    return [v for k, op, v, line in block if k == key]


def event_calls(block):
    """Event ids fired anywhere inside block."""
    out = []
    for k, op, v, line, d in walk(block):
        if k and isinstance(v, list) and EVENT_CALL.match(k):
            eid = get(v, 'id')
            if eid:
                out.append(eid)
    return out


def files(root, sub, ext='.txt'):
    d = os.path.join(root, sub)
    out = []
    for base, dirs, names in os.walk(d):
        for name in names:
            if name.endswith(ext):
                out.append(os.path.join(base, name))
    return sorted(out)
