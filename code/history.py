import helper
import logging

# === Documentation of history.py ===

def run(message, bot):
    """
    run(message, bot): This is the main function used to implement the delete feature.
    It takes 2 arguments for processing - message which is the message from the user, and bot which
    is the telegram bot object from the main code.py function. It calls helper.py to get the user's
    historical data and based on whether there is data available, it either prints an error message or
    displays the user's historical data.
    """
    try:
        helper.read_json()
        chat_id = message.chat.id
        user_history = helper.getUserHistory(chat_id)
        spend_total_str = ""
        if user_history is None:
            raise Exception("Sorry! No spending records found!")
        spend_total_str = "Here is your spending history : \nDATE, CATEGORY, AMOUNT\n----------------------\n"
        if len(user_history) == 0:
            spend_total_str = "Sorry! No spending records found!"
        else:
            for rec in user_history:
                temp = rec.split(',')
                curr = ''
                user_currency = helper.getOverallCurrency(chat_id)
                if(user_currency == 'USD'):
                    curr = '$'
                elif(user_currency == 'INR'):
                    curr = '₹'
                elif(user_currency == 'EUR'):
                    curr = '€'
                elif(user_currency == 'GBP'):
                    curr = '£'
                    
                spend_total_str += str(f"{temp[0]} {temp[1]} {curr}{temp[2]}") + "\n"
        bot.send_message(chat_id, spend_total_str)
    except Exception as e:
        logging.exception(str(e))
        bot.reply_to(message, "Oops!" + str(e))