from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetFullChannelRequest

api_id = '26304154'  # Substitute with your API ID
api_hash = '6298b78a280ec618df1440410e10ad68'  # Substitute with your API Hash
username = 'swaps_up'  # Substitute with your username
bot_token = '7123753669:AAHN-iuUJUFKTRF_BVzewRH3t_OE2682nrw'  # Substitute with your Bot Token

# Create an instance of the Telegram client
client = TelegramClient(username, api_id, api_hash)


async def filter_groups(group_usernames):
    filtered_groups = []
    for group in group_usernames:
        try:
            full = await client(GetFullChannelRequest(group))
            chat = full.full_chat
            # Check if users can send media and forward messages
            if chat.permissions.send_media and chat.permissions.forward_messages:
                filtered_groups.append(group)
        except Exception as e:
            print(f"Could not fetch details for group {group}: {str(e)}")
    return filtered_groups


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! Send me a .txt file with Telegram group usernames, one per line.')


def handle_document(update: Update, context: CallbackContext) -> None:
    """Handle incoming document."""
    file = context.bot.getFile(update.message.document.file_id)
    # Download file to local storage
    file.download('usernames.txt')
    # Read the file and get the list of usernames
    with open('usernames.txt', 'r') as f:
        group_usernames = [line.strip() for line in f.readlines()]
    # Filter groups
    with client:
        filtered_groups = client.loop.run_until_complete(filter_groups(group_usernames))
    # Save the filtered groups to a file
    with open('filtered_usernames.txt', 'w') as f:
        for group in filtered_groups:
            f.write(f'{group}\n')
    # Send the file to the user
    with open('filtered_usernames.txt', 'rb') as f:
        update.message.reply_document(f)


def main() -> None:
    """Start the bot."""
    updater = Updater(bot_token, use_context=True)  # Note the change here
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.document.mime_type("text/plain"), handle_document))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
