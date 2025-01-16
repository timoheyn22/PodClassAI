from gtts import gTTS
import os


class AudioLib:
    def turnScriptIntoAudio(self, speed, language, script):
        # Define the output folder
        output_folder = 'backend/Uploads/MP3'
        # Ensure the output folder exists
        os.makedirs(output_folder, exist_ok=True)

        # Generate the audio file
        try:
            # Define the language and TLD
            if language == "English":
                tld = "co.uk"
                language = "en"
            elif language == "english":
                language = "en"
                tld = "com"
                if language == "German":
                    language = "de"
                    tld = "com"


            # Create a gTTS object
            tts = gTTS(text=script, lang=language, slow=speed, tld=tld)

            # Define the output file path
            output_file = os.path.join(output_folder, 'output.mp3')

            # Save the audio file
            tts.save(output_file)

            print(f"Audio file saved at: {output_file}")
            return output_file  # Return the path to the generated file
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


