import re
import json
import os
from datetime import datetime
from notify import notify
from forex_python.converter import CurrencyRates

spend_categories = [
    "Food",
    "Groceries",
    "Utilities",
    "Transport",
    "Shopping",
    "Miscellaneous",
]
transaction_type = [
    "New",
    "Old",
    "Repeat existing"
]

day = {
    '1' :  1,
    '2' :  2,
    '3' :  3,
    '4' :  4,
    '5' :  5,
    '6' :  6,
    '7' :  7,
    '8' :  8,
    '9' :  9,
    '10' : 10,
    '11' : 11,
    '12' : 12,
    '13' : 13,
    '14' : 14,
    '15' : 15,
    '16' : 16,
    '17' : 17,
    '18' : 18,
    '19' : 19,
    '20' : 20,
    '21' : 21,
    '22' : 22,
    '23' : 23,
    '24' : 24,
    '25' : 25,
    '26' : 26,
    '27' : 27,
    '28' : 28,
    '29' : 29,
    '30' : 30,
    '31' : 31,
}

months = {
    'Jan' : 'Jan',
    'Feb' : 'Feb',
    'Mar' : 'Mar',
    'Apr' : 'Apr',
    'May' : 'May',
    'Jun' : 'Jun',
    'Jul' : 'Jul',
    'Aug' : 'Aug',
    'Sep' : 'Sep',
    'Oct' : 'Oct',
    'Nov' : 'Nov',
    'Dec' : 'Dec'
}
year = {
        '2023' : '2023',
        '2022' : '2022',
        '2021' : '2021',
        '2020' : '2020',
        '2019' : '2019',
        '2018' : '2018',
        '2017' : '2017'
    }
choices = ["Date", "Category", "Cost"]
spend_display_option = ["Day", "Month"]
spend_estimate_option = ["Next day", "Next month"]
update_options = {"continue": "Continue", "exit": "Exit"}
budget_options = {"update": "Add/Update", "view": "View", "delete": "Delete"}
budget_types = {"goal": "Category-Wise Goal", "recurrent": "Recurrent spendings"}
data_format = {"expense": [], "income": [], "budget": {"budget": 0, "currency": "USD", "goal": {}, "recurrent": {}, "savings": 0}}
analytics_options = {"overall": "Overall budget split", "spend": "Split of current spend", "remaining": "Remaining value", "history": "Time series graph of spend history"}

# set of implemented commands and their description
commands = {
    "menu": "Display commands with their descriptions.",
    "help": "Display the list of commands.",
    "pdf": "Save history as PDF.",
    "add": "This option is for adding your expenses \
       \n 1. It will give you the list of categories to choose from. \
       \n 2. You will be prompted to enter the amount corresponding to your spending \
       \n 3.The message will be prompted to notify the addition of your expense with the amount,date, time and category ",
    "advisor": "Your friendly budgetting AI",
    "analytics": "This option gives user a graphical representation of their expenditures \
        \n You will get an option to choose the type of data you want to see.",
    "predict": "This option analyzes your recorded spendings and gives you a budget that will accommodate for them.",
    "history": "This option is to give you the detailed summary of your expenditure with Date, time ,category and amount. A quick lookup into your spendings",
    "delete": "This option is to Clear/Erase all your records",
    "edit": "This option helps you to go back and correct/update the missing details \
        \n 1. It will give you the list of your expenses you wish to edit \
        \n 2. It will let you change the specific field based on your requirements like amount/date/category",
    "budget": "This option is to set/update/delete the budget. \
        \n 1. The Add/update category is to set the new budget or update the existing budget \
        \n 2. The view category gives the detail if budget is exceeding or in limit with the difference amount \
        \n 3. The delete category allows to delete the budget and start afresh!  ",
    
}

dateFormat = "%d-%b-%Y"
timeFormat = "%H:%M"
monthFormat = "%b-%Y"

# === Documentation of helper.py ===

# function to load .json expense record data
def read_json():
    """
    read_json(): Function to load .json expense record data
    """
    try:
        if not os.path.exists("expense_record.json"):
            with open("expense_record.json", "w") as json_file:
                json_file.write("{}")
            return json.dumps("{}")
        elif os.stat("expense_record.json").st_size != 0:
            with open("expense_record.json") as expense_record:
                expense_record_data = json.load(expense_record)
            return expense_record_data

    except FileNotFoundError:
        print("---------NO RECORDS FOUND---------")

def write_json(user_list):
    """
    write_json(user_list): Stores data into the datastore of the bot.
    """
    try:
        with open("expense_record.json", "w") as json_file:
            json.dump(user_list, json_file, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        print("Sorry, the data file could not be found.")

def validate_entered_amount(amount_entered):
    """
    validate_entered_amount(amount_entered): Takes 1 argument, amount_entered.
    It validates this amount's format to see if it has been correctly entered by the user.
    """
    if amount_entered is None:
        return 0
    if re.match("^[1-9][0-9]{0,14}\\.[0-9]*$", amount_entered) or re.match(
        "^[1-9][0-9]{0,14}$", amount_entered
    ):
        amount = round(float(amount_entered), 2)
        if amount > 0:
            return str(amount)
    return 0

def currency_convertor(chat_id, expense_currency, value):
    budget_currency = getOverallCurrency(chat_id)
    c = CurrencyRates()
    exchange_rate = c.get_rate(expense_currency, budget_currency)
    return round(value * exchange_rate, 2)

def getOverallCurrency(chat_id):
    data = getUserData(chat_id)  
    if not data:
        return 'USD'
    return data["budget"]["currency"]

def getUserHistory(chat_id):
    """
    getUserHistory(chat_id): Takes 1 argument chat_id and uses this to get the relevant user's historical data.
    """
    data = getUserData(chat_id)
    if data is not None:
        return data["expense"]
    return None

def getUserHistoryByCategory(chat_id, category):
    data = getUserHistory(chat_id)
    previous_expenses = []
    for record in data:
        if f",{category}," in record:
            previous_expenses.append(record)
    return previous_expenses

def getUserHistoryDateExpense(chat_id):
    data = getUserHistory(chat_id)
    cat_spend_dict = {}
    for record in data:
        split_vals = record.split(",")
        cat_spend_dict[split_vals[0]] = split_vals[2]
    return cat_spend_dict

def getUserData(chat_id):
    user_list = read_json()
    if user_list is None:
        return None
    if str(chat_id) in user_list:
        return user_list[str(chat_id)]
    return None

def throw_exception(e, message, bot, logging):
    logging.exception(str(e))
    bot.reply_to(message, "Oh no! " + str(e))

def createNewUserRecord():
    return data_format

def getOverallBudget(chatId):
    data = getUserData(chatId)
    if data is None or data == {}:
        return None
    return data["budget"]["budget"]

def getCategoryBudget(chatId):
    data = getUserData(chatId)
    if data is None:
        return None
    return data["budget"]["goal"]

def getRecurrentBudget(chatId):
    data = getUserData(chatId)
    if data is None:
        return None
    return data["budget"]["recurrent"]

def getCategoryBudgetByCategory(chatId, cat):
    if not isCategoryBudgetByCategoryAvailable(chatId, cat):
        return None
    data = getCategoryBudget(chatId)
    return data[cat]

def getRecurrentBudgetByCategory(chatId, cat):
    if not isRecurrentBudgetByCategoryAvailable(chatId, cat):
        return None
    data = getRecurrentBudget(chatId)
    return data[cat]

def canAddBudget(chatId):
    overall_budget = getOverallBudget(chatId)
    category_budget = getCategoryBudget(chatId)
    return (overall_budget is None and overall_budget != '0') and (category_budget is None and category_budget != {})

def isOverallBudgetAvailable(chatId):
    overall_budget = getOverallBudget(chatId)
    if overall_budget is not None and overall_budget != '0':
        return True
    return False

def isCategoryBudgetAvailable(chatId):
    category_budget = getCategoryBudget(chatId)
    if category_budget is not None and category_budget != {}:
        return True
    return False

def isCategoryBudgetByCategoryAvailable(chatId, cat):
    data = getCategoryBudget(chatId)
    if data is None or data == {}:
        return False
    return cat in data.keys()

def isRecurrentBudgetByCategoryAvailable(chatId, cat):
    data = getRecurrentBudget(chatId)
    if data is None or data == {}:
        return False
    return cat in data.keys()

def get_uncategorized_amount(chatId, amount):
    overall_budget = float(amount)
    category_budget_data = getCategoryBudget(chatId)
    if category_budget_data is None or category_budget_data == {}:
        return amount
    category_budget = 0
    for c in category_budget_data.values():
        category_budget += float(c)
    uncategorized_budget = overall_budget - category_budget
    return str(round(uncategorized_budget,2))

def display_remaining_budget(message, bot, cat):
    chat_id = message.chat.id
    display_remaining_category_budget(message, bot, cat)
    display_remaining_overall_budget(message, bot)

def display_remaining_overall_budget(message, bot):
    chat_id = message.chat.id
    remaining_budget = calculateRemainingOverallBudget(chat_id)
    budget_currency = getOverallCurrency(chat_id)
    print("here", remaining_budget)
    if remaining_budget >= 0:
        msg = f"\nRemaining Overall Budget is {budget_currency} " + str(remaining_budget)
    else:
        msg = (
            f"\nBudget Exceded!\nExpenditure exceeds the budget by {budget_currency} " + str(remaining_budget)[1:]
        )
    bot.send_message(chat_id, msg)

def calculateRemainingOverallBudget(chat_id):
    budget = getOverallBudget(chat_id)
    history = getUserHistory(chat_id)
    query = datetime.now().today().strftime(getMonthFormat())
    queryResult = [value for _, value in enumerate(history) if str(query) in value]
    return round(float(budget) - calculate_total_spendings(queryResult), 2)
    
def calculate_total_spendings(queryResult):
    total = 0
    for row in queryResult:
        s = row.split(",")
        total = total + float(s[2])
    return total

def display_remaining_category_budget(message, bot, cat):
    chat_id = message.chat.id
    budget_currency = getOverallCurrency(chat_id)
    # if not getCategoryBudgetByCategory(chat_id,cat):
    #     updateBudgetCategory(chat_id, cat)
    remaining_budget = calculateRemainingCategoryBudget(chat_id, cat)
    if remaining_budget!=None:
        if remaining_budget >= 0:
            msg = "\nRemaining Goal amount for " + cat + f" is {budget_currency} " + str(remaining_budget)
            bot.send_message(chat_id, msg)
        else:
            rem_amount = ""
            rem_amount = str(abs(remaining_budget))
            notify(chat_id, cat, rem_amount, budget_currency)
    

def calculateRemainingCategoryBudget(chat_id, cat):
    budget = getCategoryBudgetByCategory(chat_id, cat)
    if budget!=None:
        history = getUserHistory(chat_id)
        query = datetime.now().today().strftime(getMonthFormat())
        queryResult = [value for _, value in enumerate(history) if str(query) in value]
        return round(float(budget) - calculate_total_spendings_for_category(queryResult, cat), 2)
    else:
        return budget
def calculateRemainingCateogryBudgetPercent(chat_id, cat):
    budget = getCategoryBudgetByCategory(chat_id, cat)
    history = getUserHistory(chat_id)
    query = datetime.now().today().strftime(getMonthFormat())
    queryResult = [value for _, value in enumerate(history) if str(query) in value]
    return (calculate_total_spendings_for_category(queryResult, cat)/float(budget))*100

def calculate_total_spendings_for_category(queryResult, cat):
    total = 0
    for row in queryResult:
        s = row.split(",")
        if cat == s[1]:
            total = total + float(s[2])
    return total

def calculate_total_spendings_for_cateogory_chat_id(chat_id, cat):
    history = getUserHistory(chat_id)
    query = datetime.now().today().strftime(getMonthFormat())
    queryResult = [value for _, value in enumerate(history) if str(query) in value]
    return calculate_total_spendings_for_category(queryResult, cat)

def updateBudgetCategory(chatId, category):
    user_list = read_json()
    user_list[str(chatId)]["budget"]["goal"][category] = str(0)
    write_json(user_list)

def getAvailableCategories(history):
    available_categories = set()
    for record in history:
        available_categories.add(record.split(',')[1])
    return available_categories

def getCategoryWiseSpendings(available_categories, history):
    category_wise_history = {}
    for cat in available_categories:
        for record in history:
            if cat in record:
                if cat in category_wise_history.keys():
                    category_wise_history[cat].append(record)
                else:
                    category_wise_history[cat] = [record]
    return category_wise_history

def getFormattedPredictions(category_predictions):
    category_budgets = ""
    for key,value in category_predictions.items():
        if type(value) == float:
            category_budgets += str(key) + ": $" + str(value) + "\n"
        else:
            category_budgets += str(key) + ": " + value + "\n"
    predicted_budget = "Here are your predicted budgets"
    predicted_budget += " for the next month \n"
    predicted_budget += category_budgets
    return predicted_budget

#getters
def getSpendCategories():
    """
    getSpendCategories(): This functions returns the spend categories used in the bot. These are defined the same file.
    """
    return spend_categories

def getSpendDisplayOptions():
    """
    getSpendDisplayOptions(): This functions returns the spend display options used in the bot. These are defined the same file.
    """
    return spend_display_option

def getSpendEstimateOptions():
    return spend_estimate_option

def getCommands():
    """
    getCommands(): This functions returns the command options used in the bot. These are defined the same file.
    """
    return commands

def getDateFormat():
    """
    getCommands(): This functions returns the command options used in the bot. These are defined the same file.
    """
    return dateFormat

def getTimeFormat():
    """
    def getTimeFormat(): This functions returns the time format used in the bot.
    """
    return timeFormat

def getMonthFormat():
    """
    def getMonthFormat(): This functions returns the month format used in the bot.
    """
    return monthFormat

def getChoices():
    return choices

def getBudgetOptions():
    return budget_options

def getBudgetTypes():
    return budget_types

def getUpdateOptions():
    return update_options

def getTransactionTypes():
    return transaction_type

def getDaysList():
    return day

def getMonthsList():
    return months

def getYearList():
    return year

def getAnalyticsOptions():
    return analytics_options