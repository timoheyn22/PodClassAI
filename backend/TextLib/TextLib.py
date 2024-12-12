import os
import fitz
import requests

class TextLib:
    def getTextFromPDF(self,API_KEY,BASE_URL):
        print("getTextFromPDF method called")
        pdf_to_png("Uploads/PDF","Uploads/PNG")
        send_images_and_save_responses(API_KEY,BASE_URL,"Uploads/PNG","Uploads/TXT")




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


def send_images_and_save_responses(api_key, base_url, image_dir, output_dir):
    # Endpoint for interacting with the LLM
    model_endpoint = f"{base_url}/models/intern-vl2-8b"

    # Headers for the request
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    # Collect all PNG files from the image directory
    png_files = [f for f in os.listdir(image_dir) if f.endswith('.png')]

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Accumulate all responses
    all_responses = []

    # Process each PNG file
    for image_file in png_files:
        image_path = os.path.join(image_dir, image_file)

        # Read the image file
        with open(image_path, "rb") as img_file:
            image_data = img_file.read()

        # Construct the payload (Check API documentation for the correct structure)
        payload = {
            "inputs": {
                "text": "Extract all information from the image",  # This can be adjusted based on the model's requirements
            },
            "parameters": {
                "model": "Intern VL2 8B"
            }
        }

        # Files to send
        files = {
            "image": ("image.png", image_data, "image/png"),
            "payload": (None, str(payload)),  # Convert payload to a string for sending
        }

        # Send the POST request
        try:
            response = requests.post(model_endpoint, headers=headers, files=files)
            response.raise_for_status()  # Raises an exception for HTTP error responses
        except requests.exceptions.RequestException as e:
            text_response = f"Request failed for {image_file}: {str(e)}"
            all_responses.append(f"Response for {image_file}:\n{text_response}\n\n")
            continue

        # Process the response and accumulate
        if response.status_code == 200:
            result = response.json()
            text_response = result.get("text", "No text response found")
        else:
            text_response = f"Error: {response.status_code} - {response.text}"

        # Append the response to the list
        all_responses.append(f"Response for {image_file}:\n{text_response}\n\n")

    # Save all responses in a single text file
    output_file_path = os.path.join(output_dir, "all_responses.txt")
    with open(output_file_path, "w") as output_file:
        output_file.writelines(all_responses)

    print(f"All responses saved to {output_file_path}")