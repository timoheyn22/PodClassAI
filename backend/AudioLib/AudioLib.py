import pyttsx3
import os

class AudioLib:
    def turnScriptIntoAudio(self, text, speech_rate, volume, voice_id):
        output_folder = 'backend/Uploads/MP3'
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        output_path = os.path.join(output_folder, 'test.mp3')

        engine = pyttsx3.init()

        # Set speech rate (optional)
        engine.setProperty('rate', speech_rate)  # Set rate based on function argument

        # Set volume (optional)
        engine.setProperty('volume', volume)  # Set volume based on function argument

        # Set voice (optional)
        voices = engine.getProperty('voices')
        if voice_id < len(voices):  # Check if the requested voice_id is valid
            engine.setProperty('voice', voices[voice_id].id)  # Set voice based on function argument
        else:
            print("Invalid voice_id, using default voice.")
        # Save the speech to file
        engine.save_to_file(text, output_path)
        engine.runAndWait()
        print("done")


