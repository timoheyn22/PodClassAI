from backend.TextLib.TextLib import TextLib
from backend.ScriptLib.ScriptLib import ScriptLib
from backend.AudioLib.AudioLib import AudioLib
from backend.FileTransportLib.FileTransportLib import FileTransportLib
import os
from dotenv import load_dotenv
from backend import app  # Import the Flask app

# Get the API_KEY and BASE_URL from the .env file
load_dotenv()
API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')
model = "internvl2-8b"

# Called from the templates starting the pipeline from PDF to Podcast
def pipelinePDFtoPodcast(language, speed):
    print(language)
    print(speed)

    text_lib = TextLib()
    script_lib = ScriptLib()
    audio_lib = AudioLib()
    file_transporter = FileTransportLib()

    file_transporter.delete_all_files("Uploads/PNG")
    file_transporter.delete_all_files("Uploads/MP3")
    text = text_lib.getTextFromPDF(API_KEY, BASE_URL, model, language)
    print(text)
    script = script_lib.turnTextIntoScript(API_KEY, BASE_URL, model, text, language)
    audio_lib.turnScriptIntoAudio(speed, language, script)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5020)