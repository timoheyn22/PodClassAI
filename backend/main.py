from backend.TextLib.TextLib import TextLib
from backend.ScriptLib.ScriptLib import ScriptLib
from backend.AudioLib.AudioLib import AudioLib
from backend.FileTransportLib.FileTransportLib import FileTransportLib
import os
from dotenv import load_dotenv
from flask import Flask


#get the API_KEY and BASE_URL from the .env file
load_dotenv()
API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')
model = "internvl2-8b"












#called from the templates starting the pipeline form PDF to Podcast
def pipelinePDFtoPodcast():

    text_lib = TextLib()
    script_lib = ScriptLib()
    audio_lib = AudioLib()
    file_transporter = FileTransportLib()

    file_transporter.delete_all_files("Uploads/PNG")
    file_transporter.delete_all_files("Uploads/MP3")
    text = text_lib.getTextFromPDF(API_KEY, BASE_URL, model)
    script = script_lib.turnTextIntoScript(API_KEY,BASE_URL,model,text)
    audio_lib.turnScriptIntoAudio(script,150,1.0,1)


#called from the templates when a pdf is uploaded
#def savePDF(pdf_path):
   # file_transporter = FileTransportLib()
    #file_transporter.delete_all_files("Uploads/PDF")
   # file_transporter.savePDF(pdf_path"Uploads/PDF")



app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Podclass!"

if __name__ == '__main__':
    # Bind to all IPs and port 5005
    app.run(host='0.0.0.0', port=5005)