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
model = "internvl2-8b"


#example ussage until the Frontend is implemented
file_transporter = FileTransportLib()
text_lib = TextLib()
audio_lib = AudioLib()
script_lib = ScriptLib()

file_transporter.delete_all_files("Uploads/PNG")
file_transporter.delete_all_files("Uploads/MP3")
#text_lib.getTextFromPDF(API_KEY,BASE_URL)
#audio_lib.turnScriptIntoAudio("Hello World",150,1.0,1)
text = text_lib.getTextFromPDF(API_KEY,BASE_URL,model)
script = script_lib.turnTextIntoScript(API_KEY,BASE_URL,model,text)
audio_lib.turnScriptIntoAudio(script,150,1.0,1)








#called from the Frontend starting the pipeline form PDF to Podcast
def pipelinePDFtoPodcast():

    text_lib = TextLib()
    script_lib = ScriptLib()
    audio_lib = AudioLib()
    file_transporter = FileTransportLib()
    #parameters are still missing
    file_transporter.delete_all_files("Uploads/PNG")
    text_lib.getTextFromPDF(API_KEY, BASE_URL, model)


#called from the Frontend when a pdf is uploaded
def savePDF():
    file_transporter = FileTransportLib()
    file_transporter.savePDF("path/to/pdf")

# Example usage
#pipelinePDFtoPodcast()
#savePDF()