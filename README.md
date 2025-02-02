# PodClassAI

PodClassAI is a Python-based application that converts PDF documents into podcasts. It uses various libraries to extract text from PDFs, generate scripts, and convert those scripts into audio files.

## Table of Contents



## Features

- Extracts text from PDF files
- Converts extracted text into a script
- Generates audio files from the script
- Supports multiple language

## Requirements (you can also see all Requirements in the requirements.txt file)

- Python 3.x
- pip
- Flask
- PyMuPDF (fitz)
- OpenAI API
- python-dotenv


## LLM Model 
- internvl2-8b

## Installation

Ensure you have the necessary packages installed. Run the following command:

```bash
pip install -r requirements.txt

```
## Usage

1. Run the Flask application:
    ```sh
    python backend/main.py
    ```

2. Access the application in your web browser at the adress listed in terminal

3. When you land on the landing page, click on the "Go to Upload Page" button to upload a PDF file.
4. You will be redirected to the upload page where you can upload a PDF file by clicking on the "Upload File" button.
5. Once the file is uploaded, choose the language and speed for the podcast and click on the "Create Podcast" button
6. The application will then create a podcast. Once you get the message that the podcast is ready, you can download it by clicking on the "Download Podcast" button.



## Project Structure

- `backend/`: Contains the backend code for the application.
  - `main.py`: The main entry point for the Flask application and starpoint for the pipeline
  - `TextLib/`: Library for extracting text from PDFs.
  - `ScriptLib/`: Library for generating Podcst scripts from extracted text.
  - `AudioLib/`: Library for converting scripts into MP§ Podcast files.
  - `FileTransportLib/`: Library for handling file operations.
- `static/`: Contains static files for the frontend. css and js for the home and upload page
  - `css/`: CSS files for styling.
  - `js/`: JavaScript files for frontend logic.
- `templates/`: Contains HTML templates for the frontend.
  - `home.html`: The  HTML file for the landing page
  - `upload.html`: HTML file for the upload page.
- `uploads/`: Directory for storing uploaded files.
  - `PDF/`: Directory for storing uploaded PDF files.
  - `PNG/`: Directory for storing converted PNG files.
  - `MP3/`: Directory for storing generated MP3 files.
## Environment Variables

Set the following environment variables to configure the application:
API_KEY=*your API key*
BASE_URL=https://chat-ai.academiccloud.de/v1

## Demo 
A Demo Video of how to use the Application uploaded on GitHub.

## Reflection
As a Group we are very happy with how we planed and executed the Projekt. Our main challenges were sending a API request with both a prompt and a PNG file and the Server Hosting. 


