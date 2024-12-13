import os
import fitz
import requests
import json

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

        # Check if the image exists
        if not os.path.exists(image_path):
            all_responses.append(f"Error: Image {image_file} does not exist\n")
            continue

        # Read the image file
        with open(image_path, "rb") as img_file:
            image_data = img_file.read()

        # Check the image data size (ensure it is not empty)
        if not image_data:
            all_responses.append(f"Error: Image {image_file} is empty\n")
            continue

        # Construct the payload
        payload = {
            "inputs": {
                "text": "Extract all information from the image",  # Ensure this is the correct prompt
            },
            "parameters": {
                "model": "intern-vl2-8b"
            }
        }

        # Files to send
        files = {
            "image": ("image.png", image_data, "image/png"),
            "payload": (None, json.dumps(payload)),  # Ensure payload is properly serialized
        }

        # Debugging: Log the payload being sent
        all_responses.append(f"Sending request for {image_file} with payload: {json.dumps(payload)}\n")

        # Send the POST request
        try:
            response = requests.post(model_endpoint, headers=headers, files=files)
            response.raise_for_status()  # Raises an exception for HTTP error responses
        except requests.exceptions.RequestException as e:
            all_responses.append(f"Request failed for {image_file}: {str(e)}\n")
            continue

        # Debugging: Check the raw response
        if response.status_code != 200:
            all_responses.append(f"Error: Received HTTP {response.status_code} for {image_file}\n")
            all_responses.append(f"Response content: {response.text}\n")
            continue

        # Debugging: Check the response content and structure
        try:
            result = response.json()
        except ValueError as e:
            all_responses.append(f"Error parsing JSON for {image_file}: {str(e)}\n")
            all_responses.append(f"Raw response: {response.text}\n")
            continue

        # Log the response to inspect its structure
        all_responses.append(f"Response for {image_file}: {json.dumps(result, indent=2)}\n")

        # Process the response
        text_response = result.get("text", "No text response found")

        # If no text found, log the entire response for further analysis
        if text_response == "No text response found":
            all_responses.append(f"Warning: No text found for {image_file}\n")

        # Append the response to the list
        all_responses.append(f"Response for {image_file}:\n{text_response}\n\n")

    # Save all responses in a single text file
    output_file_path = os.path.join(output_dir, "all_responses.txt")
    with open(output_file_path, "w") as output_file:
        output_file.writelines(all_responses)

    print(f"All responses saved to {output_file_path}")