from flask import render_template, jsonify, request
from backend import app
from backend.main import pipelinePDFtoPodcast
from backend.FileTransportLib.FileTransportLib import FileTransportLib
import os
import logging

app.config['UPLOAD_FOLDER'] = 'Uploads/PDF'
@app.route('/')#This is the home page
def home():
    return render_template('home.html')

@app.route('/upload')#This is the upload page
def upload():
    return render_template('upload.html')

@app.route('/datenschutzinformationen')#This is the Datenschutzinformationen page
def datenschutzinformationen():
    return render_template('datenschutzinformationen.html')

@app.route('/create_podcast', methods=['POST'])#This is the create_podcast button
def create_podcast():
    try:
        data = request.get_json()
        language = data.get('language')
        speed = data.get('speed')
        # Call the pipeline to create the podcast
        pipelinePDFtoPodcast(language, speed)
        return jsonify({"message": "Podcast created successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/upload_pdf', methods=['POST']) #This is the upload_pdf button
def upload_pdf():
    # Delete all old files before creating new ones
    logging.debug("Received a request for /upload_pdf")
    file_transporter = FileTransportLib()
    file_transporter.delete_all_files("Uploads/PDF")
    # Check if the post request has the file part
    if 'pdf' not in request.files:
        logging.error("No PDF file in request")
        return jsonify({'error': 'No file uploaded'}), 400
    # Get the file from the request
    file = request.files['pdf']
    # If the user does not select a file, the browser submits an empty part without a filename.
    if not file.filename.endswith('.pdf'):
        logging.error(f"Unsupported file type: {file.filename}")
        return jsonify({'error': 'File type not supported. Please upload a PDF file.'}), 400
    # Save the file
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    logging.debug(f"Saving file to {file_path}")
    file.save(file_path)

    return jsonify({'success': True, 'message': 'PDF uploaded successfully!'})