from flask import Flask, render_template, jsonify
from backend.main import pipelinePDFtoPodcast

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/create_podcast', methods=['POST'])
def create_podcast():
    try:
        pipelinePDFtoPodcast()
        return jsonify({"message": "Podcast created successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5008

            )
