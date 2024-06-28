import json
import asyncio
from telethon import TelegramClient, events
from config.config import API_ID, API_HASH, SESSION_NAME

# Initialize Telegram client
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

# Load responses and users
with open('data/responses.json', 'r') as f:
    responses = json.load(f)

with open('data/users.json', 'r') as f:
    users = json.load(f)

def get_response(user_id):
    special_users = users.get('special_users', [])
    user_id_str = str(user_id)  # Преобразуем user_id в строку для сравнения
    if user_id_str in special_users:
        return responses['special_users'].get(user_id_str, responses['default'])
    else:
        return responses['default']

@client.on(events.NewMessage)
async def auto_responder(event):
    user_id = event.sender_id
    print(f"New message from: {user_id}")  # Debug information
    response = get_response(user_id)
    
    # Wait for a specific time (e.g., 5 minutes) before responding
    await asyncio.sleep(3)  # 3 seconds for testing purposes, change back to 300 for 5 minutes
    
    if not event.is_reply:
        print(f"Responding to: {user_id} with message: {response}")  # Debug information
        await event.respond(response)

def start_bot():
    print("Starting bot...")  # Debug information
    client.start()
    client.run_until_disconnected()
