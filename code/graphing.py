import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use("Agg")

# === Documentation of graphing.py ===

def viewBudget(data):
    sorted_data = {}
    sorted_data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1])}
    values = []
    labels = []
    for k, v in sorted_data.items():
        values.append(v)
        labels.append(k)
    plt.pie(values, labels=values, counterclock=False, shadow=True)
    plt.title("Category Wise Budget")
    plt.legend(labels, loc="center")
    plt.savefig("budget.png", bbox_inches="tight")
    plt.close()

def addlabels(x, y):
    """
    addlabels(x, y): This function is used to add the labels to the graph.
    It takes the expense values and adds the values inside the bar graph for each expense type
    """
    for i in range(len(x)):
        plt.text(i, y[i] // 2, y[i], ha="center")

def visualize(total_text, monthly_budget):
    """
    visualize(total_text): This is the main function used to implement the graphing
    part of display feature. This file is called from display.py, and takes the user
    expense as a string and creates a dictionary which in turn is fed as input matplotlib to create the graph
    """
    n1 = len(monthly_budget)
    r1 = np.arange(n1)
    print(n1)
    print(r1)
    width = 0.45
    total_text_split = [line for line in total_text.split("\n") if line.strip() != ""]
    monthly_budget_str = ""
    for key, value in monthly_budget.items():
        monthly_budget_str += str(key) + " $" + str(value) + "\n"
    monthly_budget_split = [
        line for line in monthly_budget_str.split("\n") if line.strip() != ""
    ]
    categ_val = {}
    for i in total_text_split:
        a = i.split(" ")
        a[1] = a[1].replace("$", "")
        categ_val[a[0]] = float(a[1])

    monthly_budget_categ_val = {}
    for j in monthly_budget_split:
        x = j.split(" ")
        x[1] = x[1].replace("$", "")
        monthly_budget_categ_val[x[0]] = float(x[1])

    x = list(categ_val.keys())
    y = list(categ_val.values())
    n2 = len(x)
    r2 = np.arange(n2)

    plt.bar(r2, categ_val.values(), width=width, label="your spendings")
    plt.bar(
        r1 + width, monthly_budget_categ_val.values(), width=width, label="your budget"
    )
    addlabels(x, y)

    plt.ylabel("Expenditure")
    plt.xlabel("Categories")
    plt.xticks(r1 + width / 2, monthly_budget_categ_val.keys(), rotation=90)
    plt.legend()
    plt.savefig("expenditure.png", bbox_inches="tight")
    plt.close()

def overall_split(category_budget):
    _, ax = plt.subplots()
    ax.pie(category_budget.values(), labels=category_budget.keys(), autopct='%1.1f%%')
    ax.set_title("Goals split")
    img_name = "overall_split.png"
    plt.savefig(img_name)
    plt.close()

def spend_wise_split(category_spend):
    _, ax = plt.subplots()
    ax.pie(category_spend.values(), labels=category_spend.keys(), autopct='%1.1f%%')
    ax.set_title("Category-wise spend")
    img_name = "spend_wise.png"
    plt.savefig(img_name)
    plt.close()

def remaining(category_spend_percent):
    labels = tuple(category_spend_percent.keys())
    remaining_val_list = [100 - x for x in list(category_spend_percent.values())]

    weight_counts = {
        "Used": list(category_spend_percent.values()),
        "Remaining": remaining_val_list,
    }
    width = 0.5
    _, ax = plt.subplots()
    bottom = np.zeros(len(list(category_spend_percent.values())))

    for boolean, weight_count in weight_counts.items():
        print(boolean, weight_count)
        ax.bar(labels, weight_count, width, label=boolean, bottom=bottom)
        bottom += weight_count

    ax.set_title("Category-wise budget consumed")
    plt.xlabel("Categories")
    plt.ylabel("Percentage")
    ax.legend(loc="upper right")

    img_name = "remaining.png"
    plt.savefig(img_name)
    plt.close()

def time_series(cat_spend_dict):
    plt.plot(cat_spend_dict.keys(), cat_spend_dict.values(), marker='o')
    plt.title("Time-series of expenses")
    plt.xlabel("Time")
    plt.ylabel("Expense")
    img_name = "time_series.png"
    plt.savefig(img_name)
    plt.close()