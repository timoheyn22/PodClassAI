from openai import OpenAI
class ScriptLib:
    def turnTextIntoScript(self,API_KEY, BASE_URL, model,text):
        client = OpenAI(
            api_key=API_KEY,
            base_url=BASE_URL
        )
        # Generate script using the OpenAI API
        text_to_script = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "I have the Summary of Lecture Slides. Please create a Podcast script about all the important topics in the Slides: Here are the key points from the image:"+ text}
            ],
            model=model
        )

        # Extract the assistant's reply
        response = text_to_script.choices[0].message.content

        # Print or save the response
        print(response)
        return response