class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount) is True:
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.check_funds(amount) is True:
            #Transfer to
            self.withdraw(amount, f"Transfer to {category.name}")
            #Tranfer from
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True

    def __repr__(self):
        first_line = ""
        stuff_line = ""
        last_line = ""

        first_line = self.name.center(30, "*") + "\n"

        for itm in self.ledger:
            stuff_line += "{:23.23s}{:7.2f}".format((itm.get("description")), (itm.get("amount"))) + '\n'

        last_line = f'Total: {self.balance}'
        return first_line + stuff_line + last_line

def create_spend_chart(categories):
    #conting spendings, self.balance include deposits 
    cat_spendings_list = []
    for category in categories:
        total = 0
        for spendings in category.ledger:
            if spendings.get("amount") < 0:
                total += spendings.get("amount")
        cat_spendings_list.append(total)
    catrgories_total = sum(cat_spendings_list)                                 #helps to count precentages

    #counting the precentages by category
    category_precentage = []
    for spends in cat_spendings_list:
        category_precentage.append(int(spends/catrgories_total * 10))

    headline = "Percentage spent by category\n"
    stuff_lines = ""
    wejscia = 0
    for i in range(-10,1):
        i = -i
        precentages = "{:>3}".format(str(10 * i))
        stuff_lines += precentages + "|"
        q = 0                                                                  #helps to descibe index
        for prc in category_precentage:
            if prc != i:
                if q == len(category_precentage) - 1:
                    wejscia += 1
                    stuff_lines += '    \n'
                else:
                    stuff_lines += '   '
            else:
                if q == len(category_precentage) - 1:
                    wejscia += 1
                    stuff_lines += ' o ' + " \n"
                    category_precentage[q] = category_precentage[q] - 1
                else:
                    stuff_lines += ' o '
                    category_precentage[q] = category_precentage[q] - 1
            q += 1
    dashes = '    ' + "---" * len(category_precentage) + '-'

    category_des = ''
    names = []
    for name in categories:
        names.append(name.name)
    round = 0
    longest_word = len(max(names, key= len))
    while longest_word != round:
        for cat_nam in names:
            if cat_nam == names[-1]:
                try:
                    if round == longest_word - 1:
                        category_des += f" {cat_nam[round]} " + ' '
                    else:
                        category_des += f" {cat_nam[round]} " + ' \n'
                except:
                    if round == longest_word - 1:
                        category_des += ' '
                    else:
                        category_des += "\n"
                continue
            elif cat_nam == names[0]:
                try:
                    category_des += '    ' + f" {cat_nam[round]} "
                except:
                    category_des += '       '
            else:
                try:
                    category_des += f" {cat_nam[round]} "
                except:
                    category_des += "   "
        round += 1

    return headline + stuff_lines + dashes + "\n" + category_des
# food = Category("Food")
# food.deposit(1000, "initial deposit")
# food.withdraw(10.15, "groceries")
# food.withdraw(15.89, "restaurant and more food for dessert")
# print(food.get_balance())
# clothing = Category("Clothing")
# food.transfer(50, clothing)
# clothing.withdraw(25.55)
# clothing.withdraw(100)
# auto = Category("Auto")
# auto.deposit(1000, "initial deposit")
# auto.withdraw(15)

# # print(food)
# # print(clothing)
# # print(auto)

# print(create_spend_chart([food, clothing, auto]))
