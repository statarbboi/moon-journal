import logging
from flask import Flask, render_template, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

# keep logs quiet; don't print content
log = logging.getLogger('werkzeug')
log.setLevel(logging.WARNING)

@app.after_request
def add_security_headers(resp):
    resp.headers['X-Content-Type-Options'] = 'nosniff'
    resp.headers['X-Frame-Options'] = 'DENY'
    resp.headers['Referrer-Policy'] = 'no-referrer'
    resp.headers['Cache-Control'] = 'no-store'
    return resp

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # We do not store anything. We only compute a number and return it.
    data = request.get_json(silent=True) or {}
    entry = (data.get('entry') or '').strip()
    polarity = TextBlob(entry).sentiment.polarity if entry else 0.0

    # brightness: -1..1 -> 10..120
    brightness = int((polarity + 1) / 2 * 110) + 10

    # cozy, kid-friendly glow colors
    if polarity < -0.25:
        color = "rgba(255, 140, 80, 0.9)"    # warm orange
    elif polarity > 0.25:
        color = "rgba(150, 220, 255, 0.9)"   # soft blue-white
    else:
        color = "rgba(255, 240, 190, 0.9)"   # gentle yellow

    return jsonify({'brightness': brightness, 'color': color})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
