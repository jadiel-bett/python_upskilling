import sys

def merge_inventory(tags_line: str, qtys_line: str) -> str:
    tags = tags_line.strip().split()
    qty_tokens = qtys_line.strip().split()

    n = min(len(tags), len(qty_tokens))
    merged = {}

    for i in range(n):
        tag = tags[i]
        # parse quantity safely
        try:
            qty = int(qty_tokens[i])
        except ValueError:
            # skip invalid integer tokens
            continue

        if tag in merged:
            merged[tag] = max(merged[tag], qty)
        else:
            merged[tag] = qty

    # produce a dictionary string sorted by key
    items = sorted(merged.items(), key=lambda kv: kv[0])
    pairs = [f"'{k}': {v}" for k, v in items]
    return '{' + ', '.join(pairs) + '}'


if __name__ == '__main__':
    lines = sys.stdin.read().splitlines()
    if not lines:
        print('{}')
        raise SystemExit(0)

    # Expect at least two lines; if only one provided treat quantities as empty
    tags_line = lines[0]
    qtys_line = lines[1] if len(lines) > 1 else ''

    out = merge_inventory(tags_line, qtys_line)
    print(out)
