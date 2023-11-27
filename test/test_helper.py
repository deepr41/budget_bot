from code import helper
from code.helper import isCategoryBudgetByCategoryAvailable, throw_exception
from mock import ANY
from telebot import types
from mock.mock import patch
import logging
import mock

MOCK_CHAT_ID = 894127939
MOCK_USER_DATA = {
    '894127939': {
        'expense': ["correct_mock_value"],
        "data": {
            'currency':'USD'
        },
        "budget": {"overall": None, "category": None},
    },
    "102": {
        "data": {
            'currency':'USD',
            'expense': []
        },
        "budget": {"overall": None, "category": None},
    },
}


def test_validate_entered_amount_none():
    result = helper.validate_entered_amount(None)
    if result:
        assert False, "None is not a valid amount"
    else:
        assert True


def test_validate_entered_amount_int():
    val = "101"
    result = helper.validate_entered_amount(val)
    if result:
        assert True
    else:
        assert False, val + " is valid amount"


def test_validate_entered_amount_int_max():
    val = "999999999999999"
    result = helper.validate_entered_amount(val)
    if result:
        assert True
    else:
        assert False, val + " is valid amount"


def test_validate_entered_amount_int_outofbound():
    val = "9999999999999999"
    result = helper.validate_entered_amount(val)
    if result:
        assert False, val + " is not a valid amount(out of bound)"
    else:
        assert True


def test_validate_entered_amount_float():
    val = "101.11"
    result = helper.validate_entered_amount(val)
    if result:
        assert True
    else:
        assert False, val + " is valid amount"


def test_validate_entered_amount_float_max():
    val = "999999999999999.9999"
    result = helper.validate_entered_amount(val)
    if result:
        assert True
    else:
        assert False, val + " is valid amount"


def test_validate_entered_amount_float_more_decimal():
    val = "9999999999.999999999"
    result = helper.validate_entered_amount(val)
    if result:
        assert True
    else:
        assert False, val + " is valid amount"


def test_validate_entered_amount_float_outofbound():
    val = "9999999999999999.99"
    result = helper.validate_entered_amount(val)
    if result:
        assert False, val + " is not a valid amount(out of bound)"
    else:
        assert True


def test_validate_entered_amount_string():
    val = "agagahaaaa"
    result = helper.validate_entered_amount(val)
    if result:
        assert False, val + " is not a valid amount"
    else:
        assert True


def test_validate_entered_amount_string_with_dot():
    val = "agaga.aaa"
    result = helper.validate_entered_amount(val)
    if result:
        assert False, val + " is not a valid amount"
    else:
        assert True


def test_validate_entered_amount_special_char():
    val = "$%@*@.@*"
    result = helper.validate_entered_amount(val)
    if result:
        assert False, val + " is not a valid amount"
    else:
        assert True


def test_validate_entered_amount_alpha_num():
    val = "22e62a"
    result = helper.validate_entered_amount(val)
    if result:
        assert False, val + " is not a valid amount"
    else:
        assert True


def test_validate_entered_amount_mixed():
    val = "a14&^%.hs827"
    result = helper.validate_entered_amount(val)
    if result:
        assert False, val + " is not a valid amount"
    else:
        assert True


def test_getUserHistory_without_data(mocker):
    mocker.patch.object(helper, "read_json")
    helper.read_json.return_value = {}
    result = helper.getUserHistory(MOCK_CHAT_ID)
    if result is None:
        assert True
    else:
        assert False, "Result is not None when user data does not exist"


def test_getUserHistory_with_data(mocker):
    mocker.patch.object(helper, "read_json")
    helper.read_json.return_value = MOCK_USER_DATA
    result = helper.getUserHistory(MOCK_CHAT_ID)
    print('------->', result)
    print(MOCK_USER_DATA[str(MOCK_CHAT_ID)]["expense"])
    if result == MOCK_USER_DATA[str(MOCK_CHAT_ID)]["expense"]:
        assert True
    else:
        assert False, "User data is available but not found"


def test_getUserHistory_with_none(mocker):
    mocker.patch.object(helper, "read_json")
    helper.read_json.return_value = None
    result = helper.getUserHistory(MOCK_CHAT_ID)
    if result is None:
        assert True
    else:
        assert False, "Result is not None when the file does not exist"


def test_getSpendCategories():
    result = helper.getSpendCategories()
    if result == helper.spend_categories:
        assert True
    else:
        assert False, "expected spend categories are not returned"


def test_getSpendDisplayOptions():
    result = helper.getSpendDisplayOptions()
    if result == helper.spend_display_option:
        assert True
    else:
        assert False, "expected spend display options are not returned"


def test_getCommands():
    result = helper.getCommands()
    if result == helper.commands:
        assert True
    else:
        assert False, "expected commands are not returned"


def test_getDateFormat():
    result = helper.getDateFormat()
    if result == helper.dateFormat:
        assert True
    else:
        assert False, "expected date format are not returned"


def test_getTimeFormat():
    result = helper.getTimeFormat()
    if result == helper.timeFormat:
        assert True
    else:
        assert False, "expected time format are not returned"


def test_getMonthFormat():
    result = helper.getMonthFormat()
    if result == helper.monthFormat:
        assert True
    else:
        assert False, "expected month format are not returned"


def test_getChoices():
    result = helper.getChoices()
    if result == helper.choices:
        assert True
    else:
        assert False, "expected choices are not returned"


def test_write_json(mocker):
    mocker.patch.object(helper, "json")
    helper.json.dump.return_value = True
    user_list = ["hello"]
    helper.write_json(user_list)
    helper.json.dump.assert_called_with(user_list, ANY, ensure_ascii=ANY, indent=ANY)


@patch("telebot.telebot")
def test_throw_exception(mock_telebot, mocker):
    mc = mock_telebot.return_value
    mc.reply_to.return_value = True

    message = create_message("message from testing")

    throw_exception("hello, exception from testing", message, mc, logging)
    mc.reply_to.assert_called_with(message, "Oh no! hello, exception from testing")


def test_createNewUserRecord():
    data_format_call = helper.createNewUserRecord()
    data_format = {"expense": [], "income": [], "budget": {"budget": 0, "currency": "USD", "goal": {}, "recurrent": {}, "savings": 0}}
    assert sorted(data_format_call) == sorted(data_format)


def test_getOverallBudget_none_case():
    helper.getUserData.return_value = None
    overall_budget = helper.getOverallBudget(11)
    assert overall_budget is None


def test_getOverallBudget_working_case():
    helper.getUserData = mock.Mock(return_value={"budget": {"budget": 10}})
    overall_budget = helper.getOverallBudget(11)
    assert overall_budget == 10


def test_getCategoryBudget_none_case():
    helper.getUserData.return_value = None
    overall_budget = helper.getCategoryBudget(11)
    assert overall_budget is None


def test_getCategoryBudget_working_case():
    helper.getUserData = mock.Mock(return_value={"budget": {"goal": {"Food": 10}}})
    overall_budget = helper.getCategoryBudget(11)
    assert overall_budget is not None


def test_getCategoryBudgetByCategory_none_case():
    helper.isCategoryBudgetByCategoryAvailable = mock.Mock(return_value=False)
    testresult = helper.getCategoryBudgetByCategory(10, "Food")
    assert testresult is None


def test_getCategoryBudgetByCategory_normal_case():
    helper.isCategoryBudgetByCategoryAvailable = mock.Mock(return_value=True)
    helper.getCategoryBudget = mock.Mock(return_value={"Food": 10})
    testresult = helper.getCategoryBudgetByCategory(10, "Food")
    assert testresult is not None


def test_canAddBudget():
    helper.getOverallBudget = mock.Mock(return_value=None)
    helper.getCategoryBudget = mock.Mock(return_value=None)
    testresult = helper.canAddBudget(10)
    assert testresult


def test_isOverallBudgetAvailable():
    helper.getOverallBudget = mock.Mock(return_value=True)
    testresult = helper.isOverallBudgetAvailable(10)
    assert testresult is True


def test_isCategoryBudgetAvailable():
    helper.getCategoryBudget = mock.Mock(return_value=True)
    testresult = helper.isCategoryBudgetAvailable(10)
    assert testresult is True


def test_isCategoryBudgetByCategoryAvailable_working():
    helper.getCategoryBudget = mock.Mock(return_value={"Food": 10})
    testresult = isCategoryBudgetByCategoryAvailable(10, "Food")
    assert testresult


def test_isCategoryBudgetByCategoryAvailable_none_case():
    helper.getCategoryBudget = mock.Mock(return_value=None)
    testresult = isCategoryBudgetByCategoryAvailable(10, "Food")
    assert testresult is False


def test_calculate_total_spendings():
    pass


def test_calculate_total_spendings_for_category():
    pass


def test_calculateRemainingOverallBudget():
    pass


@patch("telebot.telebot")
def test_display_remaining_overall_budget(mock_telebot, mocker):
    mc = mock_telebot.return_value
    mc.send_message.return_value = True
    helper.calculateRemainingOverallBudget = mock.Mock(return_value=100)
    message = create_message("hello from testing")
    helper.getOverallCurrency = mock.Mock(return_value='USD')
    helper.display_remaining_overall_budget(message, mc)


    # mc.send_message.assert_called_with(11, "\nRemaining Overall Budget is $100")


@patch("telebot.telebot")
def test_display_remaining_overall_budget_exceeding_case(mock_telebot, mocker):
    mc = mock_telebot.return_value
    mc.send_message.return_value = True
    helper.calculateRemainingOverallBudget = mock.Mock(return_value=-10)
    message = create_message("hello from testing")
    helper.getOverallCurrency = mock.Mock(return_value='USD')
    helper.display_remaining_overall_budget(message, mc)

    # mc.send_message.assert_called_with(
    #     11, "\nBudget Exceded!\nExpenditure exceeds the budget by $10"
    # )

@patch("telebot.telebot")
def test_display_remaining_budget_category_case(mock_telebot, mocker):
    mc = mock_telebot.return_value
    message = create_message("hello from testing")

    helper.isOverallBudgetAvailable = mock.Mock(return_value=False)
    helper.isCategoryBudgetByCategoryAvailable = mock.Mock(return_value=True)
    helper.display_remaining_category_budget = mock.Mock(return_value=True)
    helper.display_remaining_overall_budget = mock.Mock(return_value=True)


    helper.display_remaining_budget(message, mc, "Food")
    helper.display_remaining_category_budget.assert_called_with(message, mc, "Food")


def test_getBudgetTypes():
    testresult = helper.getBudgetTypes()
    localBudgetTypes = {"goal": "Category-Wise Goal", "recurrent": "Recurrent spendings"}
    assert sorted(testresult) == sorted(localBudgetTypes)


def create_message(text):
    params = {"messagebody": text}
    chat = types.User(11, False, "test")
    return types.Message(1, None, None, chat, "text", params, "")
