import helper
import logging

def run(message, bot):
    """
    This file adds savings
    """
    chat_id = message.chat.id
    user_list = helper.read_json()

    current_budget = user_list[str(chat_id)]['budget']['budget']
    current_savings = user_list[str(chat_id)]['budget']['savings']

    bot.send_message(chat_id, "Add savings amount. \n Numberical values only")
    bot.send_message(chat_id, f"Current amount in budget {current_budget}")
    bot.send_message(chat_id, f"Current amount in savings {current_savings}")
    bot.register_next_step_handler(message, post_overall_savings_input, bot)

def post_overall_savings_input(message,bot):
    user_list = helper.read_json()
    chat_id = message.chat.id

    if str(chat_id) not in user_list:
            user_list[str(chat_id)] = helper.createNewUserRecord()

    overall_budget = float(user_list[str(chat_id)]['budget']['budget'])
    savings = float(user_list[str(chat_id)]['budget']['savings'])
    savings_entered = float(message.text)

    if overall_budget < savings_entered:
        helper.throw_exception(f"Savings cannot be more than budget: {overall_budget}", message, bot, logging)
        return
    
    user_list[str(chat_id)]["budget"]["savings"] = str(savings + savings_entered)
    user_list[str(chat_id)]["budget"]["budget"] = str(overall_budget - savings_entered)
    
    helper.write_json(user_list)
    bot.send_message(chat_id, "Budget Updated!")