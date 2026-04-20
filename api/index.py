
from flask import Flask, render_template

app = Flask(__name__, template_folder="../templates")

posts = [
    {"id": 1, "title": "첫 번째 글", "content": "Hello Vercel + Flask!"},
    {"id": 2, "title": "두 번째 글", "content": "이건 블로그 테스트입니다."}
]

@app.route("/")
def home():
    return render_template("index.html", posts=posts)

@app.route("/post/<int:post_id>")
def post(post_id):
    post = next((p for p in posts if p["id"] == post_id), None)
    return render_template("post.html", post=post)

# Vercel용 entrypoint
def handler(environ, start_response):
    return app(environ, start_response)
