import helper
import graphing
from telebot import types
import os
from collections import defaultdict

def viewOverallBudget(chat_id, bot):
    if not helper.isCategoryBudgetAvailable(chat_id):
        bot.send_message(chat_id, "No category budget available", reply_markup=types.ReplyKeyboardRemove())
        return
    category_budget = {}
    for cat in helper.getCategoryBudget(chat_id):
        if helper.isCategoryBudgetByCategoryAvailable(chat_id, cat):
            cat_budget = helper.getCategoryBudgetByCategory(chat_id,cat)
            if cat_budget != '0':
                category_budget[cat] = cat_budget
    graphing.overall_split(category_budget)
    bot.send_photo(chat_id, photo=open("overall_split.png", 'rb'), reply_markup=types.ReplyKeyboardRemove())
    os.remove("overall_split.png")

def viewSpendWise(chat_id, bot):
    category_spend = defaultdict(int)
    
    data = helper.getUserData(chat_id)
    expenses = data['expense']
    
    for i in expenses:
        _, category, amount  = i.split(",")
        category_spend[category] += float(amount)

    if category_spend == {}:
        bot.send_message(chat_id, "No category spend available", reply_markup=types.ReplyKeyboardRemove())
        return
    graphing.spend_wise_split(category_spend)
    bot.send_photo(chat_id, photo=open("spend_wise.png", 'rb'), reply_markup=types.ReplyKeyboardRemove())
    os.remove("spend_wise.png")

def viewRemaining(chat_id, bot):
    if not helper.isCategoryBudgetAvailable(chat_id):
        bot.send_message(chat_id, "No category budget available", reply_markup=types.ReplyKeyboardRemove())
        return
    category_spend_percent = {}
    for cat in helper.spend_categories:
        if helper.isCategoryBudgetByCategoryAvailable(chat_id, cat):
            percent = helper.calculateRemainingCateogryBudgetPercent(chat_id, cat)
            category_spend_percent[cat] = percent
    graphing.remaining(category_spend_percent)
    bot.send_photo(chat_id, photo=open("remaining.png", 'rb'), reply_markup=types.ReplyKeyboardRemove())
    os.remove("remaining.png")

def viewHistory(chat_id, bot):
    if not helper.getUserHistory(chat_id):
        bot.send_message(chat_id, "No history available", reply_markup=types.ReplyKeyboardRemove())
        return

    cat_spend_dict = helper.getUserHistoryDateExpense(chat_id)

    graphing.time_series(cat_spend_dict)
    bot.send_photo(chat_id, photo=open("time_series.png", 'rb'), reply_markup=types.ReplyKeyboardRemove())
    os.remove("time_series.png")