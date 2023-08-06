import os
import shutil
import re
from datetime import datetime
from tqdm import tqdm, TqdmSynchronisationWarning
import pyfiglet
import warnings

# Suppressing warning caused by tqdm printing new lines in certain environments
warnings.filterwarnings("ignore", category=TqdmSynchronisationWarning)

def extract_datetime_from_filename(filename):
    # Define regular expressions to extract date and time from the file name.
    patterns = [
        r"IMG(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})",
        r"IMG_(\d{4})_(\d{2})(\d{2})_(\d{2})(\d{2})(\d{2})_\w+",
        r"VID(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})",
        r"IMG_(\d{4})(\d{2})(\d{2})_(\d{2})(\d{2})(\d{2})",
        r"VID_(\d{4})(\d{2})(\d{2})_(\d{2})(\d{2})(\d{2})",
        r"PXL_(\d{4})(\d{2})(\d{2})_(\d{2})(\d{2})(\d{2})",
        r"VID_(\d{4})(\d{2})(\d{2})_(\d{2})(\d{2})(\d{2})_HL"
    ]

    for pattern in patterns:
        match = re.search(pattern, filename)
        if match:
            groups = match.groups()
            date_str = "-".join(groups[:3])
            time_str = ":".join(groups[3:6])
            return datetime.strptime(f"{date_str}_{time_str}", "%Y-%m-%d_%H:%M:%S")

    return None

def modify_file_metadata(file_path, date_time):
    # Convert the datetime object to timestamp (seconds since the epoch).
    timestamp = date_time.timestamp()

    # Set the access and modification times of the file to the specified timestamp.
    os.utime(file_path, (timestamp, timestamp))

def main(source_directory, destination_directory):
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    unprocessed_files = []  # List to store filenames of files not processed
    files = os.listdir(source_directory)

    # Create a header using pyfiglet
    header = pyfiglet.figlet_format("Name2Meta")
    print(header)

    # Force tqdm to adjust progress bar width dynamically
    tqdm_kwargs = {
        "total": len(files),
        "desc": "Processing Files",
        "unit": "file",
        "dynamic_ncols": True
    }

    with tqdm(**tqdm_kwargs) as pbar:
        for filename in files:
            source_file_path = os.path.join(source_directory, filename)
            if os.path.isfile(source_file_path):
                # Extract date and time from the file name.
                date_time = extract_datetime_from_filename(filename)
                if date_time:
                    # Copy the file to the destination directory.
                    destination_file_path = os.path.join(destination_directory, filename)
                    shutil.copy2(source_file_path, destination_file_path)

                    # Modify the file's metadata in the destination directory.
                    modify_file_metadata(destination_file_path, date_time)
                else:
                    unprocessed_files.append(filename)

            pbar.update(1)

    # Print the list of files that were not processed
    if unprocessed_files:
        print("\nFiles not processed:")
        for file in unprocessed_files:
            print(file)

if __name__ == "__main__":
    source_directory = "./"  # Replace with the path to the source directory.
    destination_directory = "./MODDED"  # Replace with the path to the destination directory.

    main(source_directory, destination_directory)
