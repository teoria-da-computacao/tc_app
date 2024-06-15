import zipfile
import os

def unzip_file(zip_path, extract_to):
    """
    Unzips a file to the specified directory.

    :param zip_path: Path to the zip file
    :param extract_to: Directory where files should be extracted
    """
    # Check if the zip file exists
    if not os.path.isfile(zip_path):
        print(f"The file {zip_path} does not exist.")
        return

    # Create the directory if it does not exist
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)

    # Unzipping the file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        print(f"Files extracted to {extract_to}")

# Example usage
zip_file_path = 'computacao.zip'
output_directory = os.getcwd()

unzip_file(zip_file_path, output_directory)