import os
from datetime import datetime
from tqdm import tqdm

def change_metadata_to_current_time(directory_path):
    current_time = datetime.now()
    unprocessed_files = []

    files = os.listdir(directory_path)

    with tqdm(total=len(files), desc="Processing Files", unit="file") as pbar:
        for filename in files:
            file_path = os.path.join(directory_path, filename)
            if os.path.isfile(file_path):
                try:
                    # Convert the current datetime object to timestamp (seconds since the epoch).
                    timestamp = current_time.timestamp()

                    # Set the access and modification times of the file to the current timestamp.
                    os.utime(file_path, (timestamp, timestamp))
                except Exception as e:
                    unprocessed_files.append(filename)

            pbar.update(1)

    # Print the list of files that were not processed
    if unprocessed_files:
        print("\nFiles not processed:")
        for file in unprocessed_files:
            print(file)

if __name__ == "__main__":
    target_directory = "./"  # Replace with the path to the target directory.

    change_metadata_to_current_time(target_directory)
