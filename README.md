# File Metadata Management Scripts (Onedrive Metadata Fix)

Have you ever experienced frustration when using OneDrive to store your important files, only to discover that the file metadata gets modified during the upload process? If so, you're not alone! Many users encounter this issue, especially when dealing with image and video files containing crucial date and time information in their filenames.

To address this problem, I have developed a solution: the "File Metadata Management Scripts." This collection of Python scripts provides a simple and effective way to preserve the original date and time metadata of your files while uploading them to OneDrive.

## Table of Contents
- [File Metadata Management Scripts (Onedrive Metadata Fix)](#file-metadata-management-scripts-onedrive-metadata-fix)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
    - [name2meta.py](#name2metapy)
    - [now2meta.py](#now2metapy)
  - [Patterns](#patterns)
  - [License](#license)

## Introduction

This repository contains two Python scripts, `name2meta.py` and `now2meta.py`, designed to manage file metadata using regular expressions. The scripts are useful for extracting date and time from filenames and updating file metadata accordingly.

## Features

- Automatic extraction of date and time from filenames using regular expressions.
- Modification of file metadata (access and modification times) based on extracted date and time.
- Copying and organizing files based on their metadata.
- Command-line interface for ease of use.

## Installation

1. Clone the repository to your local machine.
```
    git clone https://github.com/your-username/your-repo.git
```

2. Install the required Python packages.


## Usage

### name2meta.py

The `name2meta.py` script extracts date and time from file names based on predefined patterns and modifies the file metadata accordingly. The supported patterns are:

1. `IMG20230715104904` - Basic format without underscores or prefixes.
2. `IMG_20230716_174735317_HDR` - Prefix with underscores and optional suffix.
3. `IMG_20230716_184519` - Basic format with underscores but no prefixes or suffixes.
4. `VID_20230717_093526961` - Video format with underscores and optional suffix.
5. `VID20230721085108` - Video format without underscores or prefixes.
6. `IMG_20230714_124525` - Additional pattern: Prefix with underscores and no suffix.

### now2meta.py

The `now2meta.py` script updates the metadata (access and modification times) of all files in a directory to the current date and time.

## Patterns

The scripts use regular expressions to extract date and time from file names. Here are the detailed patterns:

1. `IMG(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})`
   - Example: IMG20230715104904
   - Matches: IMG followed by 4 digits (year), 2 digits (month), 2 digits (day), 2 digits (hour), 2 digits (minute), and 2 digits (second).

2. `IMG_(\d{4})_(\d{2})(\d{2})_(\d{2})(\d{2})(\d{2})_\w+`
   - Example: IMG_20230716_174735317_HDR
   - Matches: IMG_ followed by 4 digits (year), 2 digits (month), 2 digits (day), 2 digits (hour), 2 digits (minute), 2 digits (second), underscore, and optional suffix.

3. `IMG_(\d{4})(\d{2})(\d{2})_(\d{2})(\d{2})(\d{2})`
   - Example: IMG_20230716_184519
   - Matches: IMG_ followed by 4 digits (year), 2 digits (month), 2 digits (day), 2 digits (hour), 2 digits (minute), and 2 digits (second).

4. `VID_(\d{4})(\d{2})(\d{2})_(\d{2})(\d{2})(\d{2})`
   - Example: VID_20230717_093526961
   - Matches: VID_ followed by 4 digits (year), 2 digits (month), 2 digits (day), 2 digits (hour), 2 digits (minute), and 2 digits (second).

5. `VID(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})`
   - Example: VID20230721085108
   - Matches: VID followed by 4 digits (year), 2 digits (month), 2 digits (day), 2 digits (hour), 2 digits (minute), and 2 digits (second).

6. `IMG_(\d{4})(\d{2})(\d{2})_(\d{2})(\d{2})(\d{2})`
   - Example: IMG_20230714_124525
   - Matches: IMG_ followed by 4 digits (year), 2 digits (month), 2 digits (day), 2 digits (hour), 2 digits (minute), and 2 digits (second).


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
