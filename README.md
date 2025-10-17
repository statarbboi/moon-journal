# Moonlight Journal 🌙

A tiny, privacy-first night journal. Words aren't stored. The server receives only a short mood score and discards it.

## Local run
```bash
python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m textblob.download_corpora
python app.py
```
Open http://localhost:5000

## Deploy on Render
- Push this folder to a GitHub repo.
- In Render, click New -> Blueprint -> connect the repo (uses render.yaml).
- That's it. It will build and serve at a public URL.

## Privacy
- No databases, files, or logs of entries.
- `/analyze` accepts a text string, computes a sentiment score, and returns a glow value.
- Flask logging is minimized and content is never printed.
