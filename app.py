import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['GET'])
def verify():
    # Meta verification
    if request.args.get('hub.verify_token') == os.environ.get('VERIFY_TOKEN'):
        return request.args.get('hub.challenge')
    return "Error", 403

@app.route('/webhook', methods=['POST'])
def webhook():
    # جب message آئے گا
    data = request.json
    print(data)
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
