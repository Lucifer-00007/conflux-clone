from telethon import TelegramClient, events
from settings import TELEGRAM_API_ID, TELEGRAM_API_HASH, COMBINATIONS

client = TelegramClient('session', api_id=TELEGRAM_API_ID, api_hash=TELEGRAM_API_HASH)


# create a new function to receive NewMessage events
@client.on(events.NewMessage)
async def handle_new_message(event):
    # check if message is received form specific sender
    sender_chat_id = event.sender_id
    if sender_chat_id in list(COMBINATIONS.keys()):
        msg_text = event.raw_text
        # check if message has any blacklisted word
        contains_blacklisted_word = False
        blacklisted_words = COMBINATIONS.get(sender_chat_id).get("blacklists")
        for word in blacklisted_words:
            if word in msg_text:
                contains_blacklisted_word = True

        # check if message has any whitelisted word
        contains_whitelisted_word = False
        whitelisted_words = COMBINATIONS.get(sender_chat_id).get("whitelists")
        for word in whitelisted_words:
            if word in msg_text:
                contains_whitelisted_word = True

        # and process the message only if there is no blacklisted word and
        # have at least 1 whitelisted word
        if not contains_blacklisted_word and contains_whitelisted_word:

            # send the message to destination chat
            destination_chat_ids = COMBINATIONS.get(sender_chat_id).get("destinations")
            for chat_id in destination_chat_ids:
                await client.send_message(chat_id, event.raw_text)


client.start()
client.run_until_disconnected()
