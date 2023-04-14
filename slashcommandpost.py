import requests
import os


APP_ID = os.getenv('APP_ID')
TOKEN = os.getenv('TOKEN')

url = f"https://discord.com/api/v10/applications/{APP_ID}/commands"

json = {
    "name": "permissions",
    "description": "Get or edit permissions for a user or a role",
    "options": []
}
# For authorization, you can use either your bot token
headers = {
    "Authorization": f"Bot {TOKEN}"
}

# or a client credentials token for your app with the applications.commands.update scope
headers = {
    "Authorization": f"Bearer <my_credentials_token>"
}

r = requests.post(url, headers=headers, json=json)