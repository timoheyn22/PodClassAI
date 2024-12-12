from backend.TextLib.TextLib import TextLib
from backend.ScriptLib.ScriptLib import ScriptLib
from backend.AudioLib.AudioLib import AudioLib
from backend.FileTransportLib.FileTransportLib import FileTransportLib
import os
from dotenv import load_dotenv

#get the API_KEY and BASE_URL from the .env file
load_dotenv()
API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')

text_lib = TextLib()
text_lib.getTextFromPDF(API_KEY,BASE_URL)

#called from the Frontend starting the pipeline form PDF to Podcast
def pipelinePDFtoPodcast():

    text_lib = TextLib()
    script_lib = ScriptLib()
    audio_lib = AudioLib()
    file_transporter = FileTransportLib()
    #parameters are still missing
    text_lib.getTextFromPDF()
    script_lib.turnTextIntoScript("path/to/text")
    audio_lib.turnScriptIntoAudio("path/to/script")
    file_transporter.retrunAudio("path/to/audio")

#called from the Frontend when a pdf is uploaded
def savePDF():
    file_transporter = FileTransportLib()
    file_transporter.savePDF("path/to/pdf")

# Example usage
#pipelinePDFtoPodcast()
#savePDF()