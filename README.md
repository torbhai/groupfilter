

# Telegram Group Filter Bot

This bot takes a list of Telegram group usernames from a `.txt` file, checks each group's permissions, and returns a list of group usernames that allow sending media and forwarded messages.

## Dependencies

- Python 3.7+
- python-telegram-bot
- Telethon

To install these packages, run:

```bash
pip install python-telegram-bot telethon
```

## Configuring the Bot

Before running the bot, you need to replace `'your_api_id'`, `'your_api_hash'`, `'your_username'` and `'your_bot_token'` in the python script with your actual Telegram app API ID, API Hash, your username and your Bot Token.

## Running the Bot

To run the bot, execute the python script:

```bash
python bot.py
```

Once the bot is running, you can interact with it in the following way:

1. Send the `/start` command to the bot. The bot will reply with a message asking for a `.txt` file.
2. Send a `.txt` file to the bot. The file should contain a list of Telegram group usernames, one per line.
3. The bot will check each group's permissions and return a `.txt` file containing the usernames of groups which allow sending media and forwarded messages.

## Deployment

The bot can be deployed on any server that supports Python. Instructions for deploying on Render can be found [here](https://render.com/docs/deploy-python).

**Note**: The Telegram API has some limitations and requirements, such as needing to be authenticated with a phone number. Also, it's important to respect the privacy and terms of service of the Telegram API. As such, this script is provided as a general guide, and you should ensure that any use of the API is in accordance with Telegram's rules and regulations.
