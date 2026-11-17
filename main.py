from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Shehroz NEXORA")
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="SHEHROZ NEXORA")

@app.get("/", response_class=HTMLResponse)
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Shehroz NEXORA | Explore Beyond Limits</title>
<style>
*{box-sizing:border-box;scroll-behavior:smooth}
body{margin:0;background:#07111f;color:#f5f7ff;font-family:Arial,sans-serif}
header{padding:20px 7%;display:flex;justify-content:space-between;align-items:center;background:#0b192b;position:sticky;top:0}
.logo{font-size:25px;font-weight:bold;color:#38d9ff}
nav a{color:white;text-decoration:none;margin:0 9px;font-size:14px}
.hero{text-align:center;padding:85px 20px;background:linear-gradient(135deg,#102c4b,#07111f)}
.hero h1{font-size:45px;margin:10px;color:#42dfff}
.hero p{font-size:18px;color:#c5d5e8}
.btn{display:inline-block;background:#16bde8;color:#04101c;padding:13px 23px;border-radius:25px;text-decoration:none;font-weight:bold;margin-top:15px}
.search{padding:13px;width:90%;max-width:500px;border:1px solid #31516e;border-radius:25px;background:#10243a;color:white;margin-top:25px}
section{padding:55px 7%;text-align:center}
section h2{font-size:30px;color:#42dfff}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:18px;margin-top:30px}
.card{background:#10243a;padding:25px;border:1px solid #244665;border-radius:15px;text-align:left}
.card h3{color:#53dfff}
.card p{color:#c3d1df;line-height:1.6}
.card a{color:#48d9ff;text-decoration:none}
footer{text-align:center;padding:30px;background:#0b192b;color:#9fb2c8}
</style>
</head>
<body>
<header>
<div class="logo">NEXORA</div>
<nav>
<a href="#home">Home</a>
<a href="#ai">AI Tools</a>
<a href="#learn">Learn & Earn</a>
<a href="#safety">Safety</a>
</nav>
</header>

<div class="hero" id="home">
<p>WELCOME TO THE NEXT GENERATION</p>
<h1>SHEHROZ NEXORA</h1>
<p>Explore Beyond Limits.</p>
<p>Discover AI, technology, digital skills and the future of online opportunities.</p>
<input class="search" id="search" placeholder="Search AI, earning, technology...">
<br>
<a class="btn" href="#ai">Explore Platform</a>
</div>

<section id="ai">
<h2>🤖 AI Tools & Innovation</h2>
<p>Discover the world of artificial intelligence.</p>
<div class="cards">
<div class="card"><h3>AI Writing Tools</h3><p>Explore tools that help with writing, ideas and productivity.</p><a href="https://chatgpt.com" target="_blank">Explore ChatGPT →</a></div>
<div class="card"><h3>AI Image Creation</h3><p>Learn how AI can turn creative ideas into images.</p><a href="https://www.canva.com" target="_blank">Explore Canva →</a></div>
<div class="card"><h3>AI Productivity</h3><p>Discover smart ways to save time and improve your workflow.</p><a href="https://www.notion.com" target="_blank">Explore Notion →</a></div>
</div>
</section>

<section id="learn">
<h2>💡 Learn & Earn</h2>
<p>Build useful digital skills and explore online work opportunities.</p>
<div class="cards">
<div class="card"><h3>Freelancing</h3><p>Understand freelancing, client communication and digital services.</p></div>
<div class="card"><h3>Content Creation</h3><p>Learn about YouTube, social media and content strategies.</p></div>
<div class="card"><h3>Digital Skills</h3><p>Explore graphic design, writing, research and online tools.</p></div>
</div>
</section>

<section id="technology">
<h2>🚀 Technology & Future</h2>
<div class="cards">
<div class="card"><h3>Future Technology</h3><p>Explore emerging technologies changing our world.</p></div>
<div class="card"><h3>Artificial Intelligence</h3><p>Understand AI concepts and their real-world uses.</p></div>
<div class="card"><h3>Science & Innovation</h3><p>Discover ideas shaping tomorrow's world.</p></div>
</div>
</section>

<section id="safety">
<h2>🛡️ Digital Safety</h2>
<div class="cards">
<div class="card"><h3>AI Scams</h3><p>Learn to recognize fake AI offers and online fraud.</p></div>
<div class="card"><h3>Deepfake Awareness</h3><p>Understand manipulated images, videos and voices.</p></div>
<div class="card"><h3>Online Protection</h3><p>Learn about passwords, privacy and safer browsing.</p></div>
</div>
</section>

<section id="about">
<h2>About NEXORA</h2>
<p>NEXORA is a digital knowledge platform focused on AI, technology, online learning and digital safety.</p>
<p>Our mission is to help people explore new ideas and build skills for the future.</p>
</section>

<footer>
<h3> SHEHROZ NEXORA </h3>
<p>Explore Beyond Limits.</p>
<p>AI • Technology • Learning • Digital Safety</p>
<p>© 2026 Shehroz NEXORA. All rights reserved.</p>
</footer>

<script>
const search=document.getElementById("search");
search.addEventListener("input",function(){
const q=this.value.toLowerCase();
document.querySelectorAll(".card").forEach(card=>{
card.style.display=card.innerText.toLowerCase().includes(q)?"block":"none";
});
});
</script>
</body>
</html>
"""

@app.get("/health")
def health():
    return {"status":"online","project":"SHEHROZ NEXORA"}
    fastapi.responses
    https://chatgpt.com
    https://www.canva.com
    https://www.notion.com
