from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get('/health')
def health():
    return jsonify({'status': 'ok'})


@app.post('/v1/translate')
def translate():
    payload = request.get_json(force=True, silent=True) or {}
    text = payload.get('text', '')
    source = (payload.get('source_language') or '').lower()
    target = (payload.get('target_language') or '').lower()

    lexicon = {
        ('i ni', 'susu', 'en'): 'hello',
        ('hello', 'en', 'susu'): 'i ni',
    }

    translated = lexicon.get((text.strip().lower(), source, target), text)
    return jsonify({'translation': translated, 'engine': 'rule_based_stub'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
