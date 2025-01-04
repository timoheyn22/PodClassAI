import os

class FileTransportLib:
    def retrunAudio(self, audio_path: str) -> None:
        # Placeholder implementation for transporting audio
        print(f"Returning audio from {audio_path} to the desired destination...")
        # Simulate file transport logic
        print(f"Audio at {audio_path} returned successfully.")

    def savePDF(self, pdf_path: str) -> None:
        # Placeholder implementation for saving a PDF
        print(f"Saving PDF at {pdf_path}...")
        # Simulate saving logic
        print(f"PDF saved at {pdf_path}.")

    def delete_all_files(self,folder_path):
        """
        Deletes all files in the specified folder.

        Args:
            folder_path (str): Path to the folder where files should be deleted.
        """
        if not os.path.exists(folder_path):
            print(f"Error: The folder '{folder_path}' does not exist.")
            return

        if not os.path.isdir(folder_path):
            print(f"Error: '{folder_path}' is not a directory.")
            return

        try:
            # Iterate through files in the folder
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                if os.path.isfile(file_path):  # Check if it is a file
                    os.remove(file_path)  # Delete the file
                    print(f"Deleted: {file_path}")
            print(f"All files in '{folder_path}' have been deleted.")
        except Exception as e:
            print(f"An error occurred: {e}")