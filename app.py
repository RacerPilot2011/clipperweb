from flask import Flask, request, jsonify, send_from_directory
from pathlib import Path

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")
    if not file:
        return jsonify({"success": False, "error": "No file provided"}), 400

    filepath = UPLOAD_DIR / file.filename
    file.save(filepath)
    return jsonify({"success": True, "url": f"{request.host_url}uploads/{file.filename}"})

@app.route("/uploads/<path:filename>")
def serve_file(filename):
    return send_from_directory(UPLOAD_DIR, filename)
