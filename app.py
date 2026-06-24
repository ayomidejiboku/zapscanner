from flask import Flask, request
import bad

app = Flask(__name__)

# -------------------------
# 1. Command Injection
# -------------------------
@app.route("/cmd")
def cmd():
    user_cmd = request.args.get("cmd", "ls")
    output = bad.run_command(user_cmd)
    return f"<pre>{output}</pre>"


# -------------------------
# 2. YAML Unsafe Load
# -------------------------
@app.route("/yaml")
def yaml_vuln():
    data = request.args.get("data", "foo: bar")
    try:
        result = bad.load_yaml(data)
        return f"YAML loaded: {result}"
    except Exception as e:
        return str(e)


# -------------------------
# 3. Pickle Unsafe Load
# -------------------------
@app.route("/pickle")
def pickle_vuln():
    payload = request.args.get("p", "cos\nsystem\n(S'echo test'\ntR.")
    try:
        result = bad.load_pickle(payload.encode())
        return f"Pickle loaded: {result}"
    except Exception as e:
        return str(e)


# -------------------------
# 4. Homepage with links so ZAP can discover routes
# -------------------------
@app.route("/")
def index():
    return """
    <h1>Vulnerable App Using bad.py</h1>
    <ul>
        <li><a href='/cmd?cmd=ls'>Command Injection</a></li>
        <li><a href='/yaml?data=foo: bar'>YAML Unsafe Load</a></li>
        <li><a href='/pickle?p=cos\nsystem\n(S'echo test'\ntR.'>Pickle Unsafe Load</a></li>
    </ul>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
