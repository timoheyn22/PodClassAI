from openai import OpenAI
class ScriptLib:
    def turnTextIntoScript(self,API_KEY, BASE_URL, model,text,language):
        client = OpenAI(
            api_key=API_KEY,
            base_url=BASE_URL
        )
        if language == "English":
            prompt = "I have the Summary of Lecture Slides. Please create a Podcast script about all the important topics in the Slides:"
        elif language == "english":
            prompt = "I have the Summary of Lecture Slides. Please create a Podcast script about all the important topics in the Slides:"
        elif language == "German":
            prompt = "Ich habe die Zusammenfassung von Vorlesungsfolien. Bitte erstellen Sie ein Podcast-Skript über alle wichtigen Themen in den Folien:"

        # Generate script using the OpenAI API
        text_to_script = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt + text}
            ],
            model=model
        )

        # Extract the assistant's reply
        response = text_to_script.choices[0].message.content

        # Print or save the response
        print(response)
        return response