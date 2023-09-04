import requests
import json

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

bot_token = config["bot_token"]
channel_ids = config["channel_ids"]

message_to_send = input("Enter the message to send: ")

for channel_id in channel_ids:
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    headers = {
        'authorization': bot_token,
        'content-type': 'application/json'
    }
    payload = {
        'content': message_to_send
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        print(f"Message sent to channel {channel_id}")
    else:
        print(f"Failed to send message to channel {channel_id}: {response.text}")

input("Press Enter to exit...")
