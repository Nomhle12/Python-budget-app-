class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def get_balance(self):
        return sum(i["amount"] for i in self.ledger)

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def transfer(self, amount, Category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {Category.name}')
            Category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def __str__(self):
        title = self.name.center(30, "*")
        lines = ""

        for item in self.ledger:
            desc = item["description"][:23]
            amount = f'{item["amount"]:.2f}'
            lines += f"{desc:<23}{amount:>7}\n"

        return title + '\n' + lines + f"Total: {self.get_balance():.2f}"


def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    spends = []

    for category in categories:
        spent = 0

        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])

        spends.append(spent)

    total_spent = sum(spends)

    percentages = []

    for spent in spends:
        percent = (spent / total_spent) * 100
        percentages.append(int(percent // 10) * 10)

    for level in range(100, -1, -10):
        line = f"{level:>3}| "

        for percent in percentages:
            if percent >= level:
                line += "o  "
            else:
                line += "   "

        chart += line + "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    categorie_names = []

    for category in categories:
        categorie_names.append(category.name)

    maximum_length = max(len(name) for name in categorie_names)

    for i in range(maximum_length):
        line = "     "

        for name in categorie_names:
            if i < len(name):
                line += name[i] + "  "
            else:
                line += "   "

        chart += line + "\n"

    return chart.rstrip("\n")
