import helper

# === Documentation of budget_delete.py ===


def run(message, bot):
    """
    run(message, bot): This is the main function used to implement the budget delete feature.
    It takes 2 arguments for processing - message which is the message from the user, and bot
    which is the telegram bot object from the main code.py function. It gets the user's chat ID
    from the message object, and reads all user data through the read_json method from the helper module.
    It then proceeds to empty the budget data for the particular user based on the user ID provided from the UI.
    It returns a simple message indicating that this operation has been done to the UI.
    """
    chat_id = message.chat.id
    user_list = helper.read_json()
    print(user_list)
    if str(chat_id) in user_list:
        user_list[str(chat_id)]["budget"]["budget"] = str(0)
        user_list[str(chat_id)]["budget"]["goal"] = {}
        user_list[str(chat_id)]["budget"]["savings"] = str(0)
        user_list[str(chat_id)]["budget"]["recurrent"] = {}
        user_list[str(chat_id)]["budget"]["currency"] = "USD"
        helper.write_json(user_list)
    bot.send_message(chat_id, "Budget deleted!")
