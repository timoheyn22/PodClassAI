import os
import fitz
import base64
from openai import OpenAI


class TextLib:
    def getTextFromPDF(self, API_KEY, BASE_URL,model,language):
        print("getTextFromPDF method called")
        pdf_to_png("Uploads/PDF", "Uploads/PNG")
        result = send_images_and_save_responses(API_KEY, BASE_URL, model,language)
        print("got text from PDFs")
        return result

def send_images_and_save_responses(api_key, base_url, model, language):
    # Start OpenAI client
    client = OpenAI(
        api_key=api_key,
        base_url=base_url,
    )
    image_dir = "Uploads/PNG"

    # Define prompt
    if language == "English":
        prompt = "Describe the key information of the picture thoroughly"
    elif language == "German":
        prompt = "Beschreiben Sie die wichtigsten Informationen des Bildes ausführlich"


    print (prompt+ "prompt1"+language)
    # Initialize a string to collect all responses
    all_responses = ""

    # Loop through all PNG files in the directory
    # Sort filenames to ensure correct order
    png_files = sorted(
        [f for f in os.listdir(image_dir) if f.lower().endswith(".png")],
        key=lambda x: (x.split("_page_")[0], int(x.split("_page_")[1].split(".png")[0]))
    )

    for file_name in png_files:
        image_path = os.path.join(image_dir, file_name)
        print(f"Processing file: {file_name}")

        try:
            # Encode the image to base64
            base64_image = encode_image(image_path)
            print(f"Encoded {file_name} to base64.")

            # Send the image to the API and get the response
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": prompt},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{base64_image}"
                                },
                            },
                        ],
                    }
                ],
            )
            message_content = response.choices[0].message.content

            # Append to all_responses
            all_responses += f"Response for {file_name}: {message_content}\n"

        except Exception as e:
            print(f"Error processing {file_name}: {e}")

    return all_responses

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def pdf_to_png(input_folder="Uploads/PDF", output_folder="Uploads/PNG"):
    """
    Converts each page of PDF files in a folder to PNG format.

    Args:
        input_folder (str): Path to the folder containing PDF files.
        output_folder (str): Path to the folder to store PNG files.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for pdf_file in os.listdir(input_folder):
        if pdf_file.lower().endswith(".pdf"):
            pdf_path = os.path.join(input_folder, pdf_file)
            pdf_name = os.path.splitext(pdf_file)[0]

            # Open the PDF file
            pdf_document = fitz.open(pdf_path)
            for page_num in range(len(pdf_document)):
                page = pdf_document[page_num]

                # Render page to an image
                pix = page.get_pixmap()

                # Generate output file name
                output_file = os.path.join(output_folder, f"{pdf_name}_page_{page_num + 1}.png")

                # Save image as PNG
                pix.save(output_file)

            pdf_document.close()
            print(f"Converted: {pdf_file} -> PNGs stored in {output_folder}")