from flask import Flask, render_template, jsonify, request
from backend.main import pipelinePDFtoPodcast
from backend.FileTransportLib.FileTransportLib import FileTransportLib
import os
import logging
logging.basicConfig(level=logging.DEBUG)

# from backend import app  # Import the Flask app
app = Flask(__name__, template_folder='../templates', static_folder='../static')

# Set the upload folder
UPLOAD_FOLDER = 'Uploads/PDF'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/') # Home page
def home():
    return render_template('home.html')

@app.route('/upload') # Upload page
def upload():
    return render_template('upload.html')

@app.route('/create_podcast', methods=['POST']) #Starts the PDF to Podcast pipeline
def create_podcast():
    try:
        data = request.get_json()
        language = data.get('language')
        speed = data.get('speed')
        #call the start of the pipeline
        pipelinePDFtoPodcast(language, speed)
        return jsonify({"message": "Podcast created successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/upload_pdf', methods=['POST']) #Uploads the PDF file
def savePDF():
    # Delete all old files before creating new ones
    logging.debug("Received a request for /upload_pdf")
    file_transporter = FileTransportLib()
    file_transporter.delete_all_files("Uploads/PDF")

    # Check if the POST request has the file part
    if 'pdf' not in request.files:
        logging.error("No PDF file in request")
        return jsonify({'error': 'No file uploaded'}), 400
    # Get the file
    file = request.files['pdf']
    # If the user does not select a file, the browser submits an empty file without a filename
    if not file.filename.endswith('.pdf'):
        logging.error(f"Unsupported file type: {file.filename}")
        return jsonify({'error': 'File type not supported. Please upload a PDF file.'}), 400
    # Save the file
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    logging.debug(f"Saving file to {file_path}")
    file.save(file_path)

    return jsonify({'success': True, 'message': 'PDF uploaded successfully!'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5020)