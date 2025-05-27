# eval.py
import sys

try:
    expr = sys.argv[1]
    # ⚠ Vorsicht: eval kann gefährlich sein!
    result = eval(expr)
    print(result)
except Exception as e:
    print(f"Fehler: {e}")
