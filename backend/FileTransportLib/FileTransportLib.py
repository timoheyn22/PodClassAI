
import os


class FileTransportLib:
    #delete all files in a given folder
    def delete_all_files(self, folder_path):
        """
        Deletes all files in the specified folder.

        Args:
            folder_path (str): Path to the folder where files should be deleted.
        """
        # Check if the folder exists
        if not os.path.exists(folder_path):
            print(f"Error: The folder '{folder_path}' does not exist.")
            return
        # Check if the folder is a directory
        if not os.path.isdir(folder_path):
            print(f"Error: '{folder_path}' is not a directory.")
            return
        # Delete all files in the folder
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