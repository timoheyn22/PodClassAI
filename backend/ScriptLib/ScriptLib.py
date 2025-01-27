from openai import OpenAI
class ScriptLib:
    def turnTextIntoScript(self,API_KEY, BASE_URL, model,text,language):
        client = OpenAI(
            api_key=API_KEY,
            base_url=BASE_URL
        )
        # put the text in quotes
        formatted_text = f'"{text}"'
        if language == "English":
            prompt = "U are an Information Podcast between 2 Peopel.1 Person is explaing the other Person a Topic in Detail. I will Provide u with Data about the topic.Create a detailed Podcast from start till finsih. Your Data:"
        elif language == "German":
            prompt = "Du bist ein Informations Podcast zwischen 2 Mensche. Eine Person erklät der anderen Person ein Thema im Detail. Ich werde dir Daten über das Thema geben. Erstelle einen detaillierten Podcast von Anfang bis Ende. Deine Daten:"

        # Generate script using the OpenAI API
        text_to_script = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt + formatted_text}
            ],
            model=model
        )

        # Extract the assistant's reply
        response = text_to_script.choices[0].message.content

        # Print or save the response
        print(response)
        return response