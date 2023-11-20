from jproperties import Properties
from notifier import TelegramNotifier

configs = Properties()

def notify(chat_id, cat, amount, budget_currency):
    with open("user.properties", "rb") as read_prop:
        configs.load(read_prop)
    token = str(configs.get("api_token").data)
    print(token)
    notifier = TelegramNotifier(token, parse_mode="HTML", chat_id=chat_id)
    msg = "<b>Budget for " + cat + f" exceeded by {budget_currency} " + amount + "!</b>"
    notifier.send(msg)