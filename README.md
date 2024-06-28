# Telegram Bot Answering Machine

This project is a Telegram bot that acts as an answering machine, responding to messages if the user is busy.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/TgBotAnsweringMachine.git
   cd TgBotAnsweringMachine
   ```

2. **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  
    ```
3. **Install the required packages:**
    ```bash
    pip install telethon
    ```
4. **Set up your configuration files:**

    - Create a config/config.py file with your Telegram API credentials (data for your account [my.telegram.org](https://my.telegram.org)):
    ```bash
    API_ID = 'your_telegram_api_id'
    API_HASH = 'your_telegram_api_hash'
    SESSION_NAME = 'your_session_name'
    ```
    - Create data/responses.json and data/users.json as per the examples provided.
    ```bash
    {
        "default": "Hello, this is an answering machine, I'm busy at the moment, I'll definitely answer soon",
        "special_users": {
            "6815726205": "Hi, this is an answering machine, I'm busy at the moment, I'll definitely answer soon",
            "user2": "Hello! Please wait a bit, I'll respond shortly."
        }
    }
    ```
    - Create data/users.json:
    ```bash
    {
        "special_users": ["6815726205", "user2"]
    }
    ```
## Usage

1. **Run the auth.py script to authenticate your Telegram session:**

```bash
python auth.py
```
- Enter your phone number in international format.
- Enter the verification code sent to your Telegram account.
- Enter your password if prompted (for two-factor authentication).

2. **Start the bot:**
```bash
python main.py
```

## Donating

If you don't mind donating for a meal:D

## License

You may copy, distribute and modify the software provided that modifications are described and licensed for free under LGPL-3.
