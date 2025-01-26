from flask import Flask, render_template, jsonify, request
from backend.main import pipelinePDFtoPodcast
from backend.FileTransportLib.FileTransportLib import FileTransportLib
import os
import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__, template_folder='../templates', static_folder='../static')

UPLOAD_FOLDER = 'Uploads/PDF'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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

@app.route('/upload_pdf', methods=['POST'])
def savePDF():
    logging.debug("Received a request for /upload_pdf")
    file_transporter = FileTransportLib()
    file_transporter.delete_all_files("Uploads/PDF")

    if 'pdf' not in request.files:
        logging.error("No PDF file in request")
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['pdf']

    if not file.filename.endswith('.pdf'):
        logging.error(f"Unsupported file type: {file.filename}")
        return jsonify({'error': 'File type not supported. Please upload a PDF file.'}), 400

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    logging.debug(f"Saving file to {file_path}")
    file.save(file_path)

    return jsonify({'success': True, 'message': 'PDF uploaded successfully!'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5020)