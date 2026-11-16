
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from urllib.request import Request, urlopen
from urllib.parse import quote
import json

app = FastAPI(title="NEXORA")

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>NEXORA</title>
    <style>
    body{background:#080d1c;color:white;text-align:center;font-family:Arial;padding:60px 15px}
    h1{font-size:45px;color:#70a5ff}
    input{padding:15px;border-radius:30px;width:65%;max-width:400px}
    button{padding:15px;background:#2868ed;color:white;border:0;border-radius:25px}
    a{color:#83aaff}
    </style>
    </head>
    <body>
    <h1>NEXORA</h1>
    <p>Explore Beyond Limits.</p>
    <form action="/search">
    <input name="q" placeholder="Search anything..." required>
    <button>Search</button>
    </form>
    </body>
    </html>
    """

@app.get("/search", response_class=HTMLResponse)
def search(q: str = ""):
    url = "https://en.wikipedia.org/w/api.php?action=opensearch&search=" + quote(q) + "&format=json"
    try:
        req = Request(url, headers={"User-Agent": "NEXORA/1.0"})
        data = json.loads(urlopen(req, timeout=10).read())
        results = "".join(
            f'<p><a href="{link}">{title}</a><br>{desc}</p>'
            for title, desc, link in zip(data[1], data[2], data[3])
        )
        return f"<h1>NEXORA Results</h1>{results}<a href='/'>Home</a>"
    except Exception:
        return "Search unavailable. Please try again."

@app.get("/health")
def health():
    return {"status": "online", "project": "NEXORA"}
  
