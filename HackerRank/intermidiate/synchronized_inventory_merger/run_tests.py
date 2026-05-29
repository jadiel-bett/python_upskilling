import subprocess
from pathlib import Path

BASE = Path(__file__).parent
TEST_DIR = BASE / 'test_cases'
SOLUTION = BASE / 'solution.py'

inputs = sorted(TEST_DIR.glob('input_*.txt'))

if not inputs:
    print('No test inputs found in', TEST_DIR)
    raise SystemExit(1)

passed = 0
total = 0

for inp in inputs:
    total += 1
    suffix = inp.stem.replace('input_', '')
    expected_file = TEST_DIR / f'output_{suffix}.txt'

    if not expected_file.exists():
        print(f'{inp.name}: expected output file {expected_file.name} not found — SKIP')
        continue

    with inp.open('r', encoding='utf-8') as fh:
        try:
            proc = subprocess.run(['python', str(SOLUTION)], stdin=fh, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=10)
        except subprocess.TimeoutExpired:
            print(f'{inp.name}: TIMEOUT')
            continue

    stdout = proc.stdout.strip()
    expected = expected_file.read_text(encoding='utf-8').strip()

    ok = stdout == expected
    status = 'PASS' if ok else 'FAIL'
    print(f'{inp.name}: {status}')
    if not ok:
        print('  Expected:', expected)
        print('  Got:     ', stdout)
        if proc.stderr:
            print('  STDERR:', proc.stderr.strip())
    else:
        passed += 1

print(f'\nSummary: {passed}/{total} tests passed')

if passed != total:
    raise SystemExit(2)
