@Client.on_message(Filters.command(["start", "help"]))
async def my_handler(client, message):
    print(message)
