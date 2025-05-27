# Mapping of file extensions to MIME types
mime_types = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip",
}

# Get the file name from the user
file_name = input("Enter the file name: ").lower().strip()

# Extract the file extension
if "." in file_name:
    file_extension = "." + file_name.split(".")[-1]  # Get the part after the last dot
else:
    file_extension = ""  # No extension found

# Check and return the MIME type
if file_extension in mime_types:
    print(mime_types[file_extension])
else:
    print("application/octet-stream")
