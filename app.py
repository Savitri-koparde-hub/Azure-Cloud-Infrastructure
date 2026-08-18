from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
from pathlib import Path

app = Flask(__name__)
DB_PATH = Path("database/vision.db")
DB_PATH.parent.mkdir(exist_ok=True)

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS visions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            image_url TEXT,
            status TEXT NOT NULL DEFAULT 'Planned'
        )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def home():
    conn = get_db()
    visions = conn.execute("SELECT * FROM visions ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("index.html", visions=visions)

@app.route("/add", methods=["GET", "POST"])
def add_vision():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        image_url = request.form.get("image_url", "").strip()
        if title:
            conn = get_db()
            conn.execute(
                "INSERT INTO visions (title, description, image_url) VALUES (?, ?, ?)",
                (title, description, image_url)
            )
            conn.commit()
            conn.close()
        return redirect(url_for("home"))
    return render_template("add.html")

@app.post("/complete/<int:vision_id>")
def complete_vision(vision_id):
    conn = get_db()
    conn.execute("UPDATE visions SET status = 'Completed' WHERE id = ?", (vision_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("home"))

@app.post("/delete/<int:vision_id>")
def delete_vision(vision_id):
    conn = get_db()
    conn.execute("DELETE FROM visions WHERE id = ?", (vision_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("home"))

@app.get("/health")
def health():
    return jsonify(status="healthy", application="vision-board")

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
else:
    init_db()
