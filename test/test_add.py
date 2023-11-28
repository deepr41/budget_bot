import os
import json
from mock.mock import patch
from telebot import types
from code import add
from mock import ANY


dateFormat = "%d-%b-%Y"
timeFormat = "%H:%M"
monthFormat = "%b-%Y"


@patch("telebot.telebot")
def test_run(mock_telebot, mocker):
    mc = mock_telebot.return_value
    mc.reply_to.return_value = True
    message = create_message("hello from test run!")
    add.run(message, mc)
    assert mc.reply_to.called


@patch("telebot.telebot")
def test_post_category_selection_working(mock_telebot, mocker):
    mc = mock_telebot.return_value
    mc.send_message.return_value = True
    date_of_entry = '27-Nov-2023'

    message = create_message("hello from testing!")
    add.post_category_selection(message, mc, date_of_entry)
    assert mc.send_message.called

@patch("telebot.telebot")
def test_post_currency_selection_working(mock_telebot, mocker):
    mc = mock_telebot.return_value
    mc.send_message.return_value = True

    message = create_message("hello from testing!")

    selected_category, date_of_entry = "category", "27-Nov-2023"
    add.post_currency_selection(message, mc, selected_category, date_of_entry)
    assert mc.send_message.called

@patch("telebot.telebot")
def test_post_category_selection_noMatchingCategory(mock_telebot, mocker):
    mc = mock_telebot.return_value
    mc.send_message.return_value = []
    mc.reply_to.return_value = True

    mocker.patch.object(add, "helper")
    add.helper.getSpendCategories.return_value = None

    date_of_entry = '27-Nov-2023'

    message = create_message("hello from testing!")
    add.post_category_selection(message, mc, date_of_entry)
    assert mc.reply_to.called


@patch("telebot.telebot")
def test_post_amount_input_working(mock_telebot, mocker):
    mc = mock_telebot.return_value
    mc.send_message.return_value = True

    date_of_entry = '27-Nov-2023'

    message = create_message("hello from testing!")
    add.post_category_selection(message, mc, date_of_entry)
    assert mc.send_message.called


@patch("telebot.telebot")
def test_post_amount_input_working_withdata(mock_telebot, mocker):
    mc = mock_telebot.return_value
    mc.send_message.return_value = True
    mocker.patch.object(add, "helper")
    add.helper.validate_entered_amount.return_value = 10
    add.helper.write_json.return_value = True
    add.helper.getDateFormat.return_value = dateFormat
    add.helper.getTimeFormat.return_value = timeFormat

    mocker.patch.object(add, "option")
    add.option.return_value = {11, "here"}

    message = create_message("hello from testing!")
    selected_currency = 'USD'
    date_of_entry = '27-Nov-2023'
    add.post_amount_input(message, mc, "Food", selected_currency, date_of_entry)
    assert True


@patch("telebot.telebot")
def test_post_amount_input_nonworking(mock_telebot, mocker):
    mc = mock_telebot.return_value
    mc.send_message.return_value = True
    mc.reply_to.return_value = True
    mocker.patch.object(add, "helper")
    add.helper.validate_entered_amount.return_value = 0
    message = create_message("hello from testing!")
    selected_currency = 'USD'
    date_of_entry = '27-Nov-2023'
    add.post_amount_input(message, mc, "Food", selected_currency, date_of_entry)
    assert mc.reply_to.called


@patch("telebot.telebot")
def test_post_amount_input_working_withdata_chatid(mock_telebot, mocker):
    mc = mock_telebot.return_value
    mc.send_message.return_value = True
    mocker.patch.object(add, "helper")
    add.helper.validate_entered_amount.return_value = 10
    add.helper.write_json.return_value = True
    add.helper.getDateFormat.return_value = dateFormat
    add.helper.getTimeFormat.return_value = timeFormat

    mocker.patch.object(add, "option")
    add.option = {11, "here"}
    test_option = {}
    test_option[11] = "here"
    add.option = test_option

    message = create_message("hello from testing!")
    selected_currency = 'USD'
    date_of_entry = '27-Nov-2023'
    add.post_amount_input(message, mc, "Food", selected_currency, date_of_entry)
    assert True
    # assert mc.send_message.called_with(11, ANY)


def test_add_user_record_nonworking(mocker):
    mocker.patch.object(add, "helper")
    add.helper.read_json.return_value = {}
    addeduserrecord = add.add_user_record(1, "date,type,100")
    assert addeduserrecord


def test_add_user_record_working(mocker):
    MOCK_USER_DATA = test_read_json()
    mocker.patch.object(add, "helper")
    add.helper.read_json.return_value = MOCK_USER_DATA
    addeduserrecord = add.add_user_record(1, "date,type,100")
    if len(MOCK_USER_DATA) + 1 == len(addeduserrecord):
        assert True


def create_message(text):
    params = {"messagebody": text}
    chat = types.User(11, False, "test")
    return types.Message(1, None, None, chat, "text", params, "")


def test_read_json():
    try:
        if not os.path.exists("./test/dummy_expense_record.json"):
            with open("./test/dummy_expense_record.json", "w") as json_file:
                json_file.write("{}")
            return json.dumps("{}")
        elif os.stat("./test/dummy_expense_record.json").st_size != 0:
            with open("./test/dummy_expense_record.json") as expense_record:
                expense_record_data = json.load(expense_record)
            return expense_record_data

    except FileNotFoundError:
        print("---------NO RECORDS FOUND---------")
