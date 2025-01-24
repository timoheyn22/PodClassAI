from flask import render_template, jsonify, request
from backend import app
from backend.main import pipelinePDFtoPodcast

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/create_podcast', methods=['POST'])
def create_podcast():
    try:
        data = request.get_json()
        language = data.get('language')
        speed = data.get('speed')
        pipelinePDFtoPodcast(language, speed)
        return jsonify({"message": "Podcast created successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500