import subprocess

js_code = "2 + 3 * 4"
result = subprocess.run(
    ["node", "script.js", js_code],
    capture_output=True,
    text=True
)

print("JavaScript-Ergebnis:", result.stdout.strip())
