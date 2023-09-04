import requests
import json

# Load configuration from config.json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

bot_token = config["bot_token"]
channel_ids = config["channel_ids"]

# Prompt for the message to send, including the possibility of specifying a file
user_input = input("Enter the message to send (or 'file:filename.txt' to send a formatted file): ")

# Initialize variables for the message and files
message_to_send = ""
files_to_send = []

# Check if the input starts with "file:" to handle file uploads
if user_input.startswith("file:"):
    # Extract the filename
    filename = user_input[len("file:"):].strip()
    try:
        # Read the content of the file
        with open(filename, 'r') as file:
            # Format the content with triple backticks
            formatted_content = f"```\n{file.read()}\n```"
            message_to_send = formatted_content
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        exit(1)
else:
    message_to_send = user_input

# Iterate through each channel and send the message with files if specified
for channel_id in channel_ids:
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    headers = {
        'authorization': bot_token
    }
    payload = {
        'content': message_to_send
    }
    files = []

    if files_to_send:
        # Add files to the request
        for file_name, file_content in files_to_send:
            files.append(('file', (file_name, file_content)))

    response = requests.post(url, headers=headers, data=payload, files=files)

    if response.status_code == 200:
        print(f"Message with files sent to channel {channel_id}")
    else:
        print(f"Failed to send message with files to channel {channel_id}: {response.text}")

# Wait for user input before exiting
input("Press Enter to exit...")
