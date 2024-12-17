import os
import fitz
import requests


class TextLib:
    def getTextFromPDF(self,API_KEY,BASE_URL):
        print("getTextFromPDF method called")
        pdf_to_png("Uploads/PDF","Uploads/PNG")
        #send_images_and_save_responses(API_KEY,BASE_URL,"Uploads/PNG","Uploads/TXT")
        send_request_and_save_response(API_KEY, 'Uploads/PNG', 'Uploads/TXT')




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

def send_request_and_save_response(api_key, input_folder, output_folder):
    url = 'https://chat-ai.academiccloud.de/v1/chat/completions'

    headers = {
        'Authorization': 'Bearer {}'.format(api_key),
    }

    # Loop over all files in the input_folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):  # Only process PNG files
            file_path = os.path.join(input_folder, filename)

            # Open the file in binary mode
            with open(file_path, 'rb') as f:
                # Define the data for the request
                files = {
                    'model': (None, "internvl2-8b"),
                    'file': f,
                }

                # Send the request
                response = requests.post(url, headers=headers, files=files)

            response_text = response.text

            # Output filename is the same as input but with .txt extension
            output_filename = os.path.splitext(filename)[0] + ".txt"
            output_path = os.path.join(output_folder, output_filename)

            # Write the response to a txt file
            with open(output_path, 'w') as f:
                f.write(response_text)



