class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.funds = 0

    def __str__(self):
        return self.ledger_layout()


    def deposit(self, amount, description=""):
        new_deposit = {"amount":amount, "description":description}
        self.ledger.append(new_deposit)
        self.funds = self.funds + amount

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        else:
            new_withdrawal = {"amount":(amount*-1),
                              "description":description}
            self.ledger.append(new_withdrawal)
            self.funds = self.funds - amount
            return True
    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        else:
            self.withdraw(amount, "Transfer to %s" % (category.category))
            category.deposit(amount, "Transfer from %s" % (self.category))
            return True

    def get_balance(self):
        return self.funds

    def check_funds(self, amount):
        if self.funds - amount < 0:
            return False
        else:
            return True

    def ledger_layout(self):
        layout = self.category
        side = 0
        while len(layout) != 30:
            if side == 0:
                layout = "*" + layout
                side = 1
            else:
                layout = layout + "*"
                side = 0
        for i in self.ledger:
            amount = str(i["amount"])
            if "." not in amount:
                amount = amount + ".00"
            description = i["description"]
            if len(description) > 23:
                description = description[:23]
            space = 30 - (len(description) + len(amount))
            layout = layout + "\n" + description
            while space > 0:
                layout = layout + " "
                space = space - 1
            layout = layout + amount
        layout = "%s\nTotal: %s" % (layout, str(self.get_balance()))
        return layout

def create_spend_chart(budget_list):
    chart = "\nPercentage spent by category"
    spending_chart = [[]]
    cat_totals = []
    total = 0
    names = []
    for i in budget_list:
        for j in i.ledger:
            if j["amount"] < 0:
                total = total + j["amount"]*-1
    for i in range(100, -1, -10):
        if i == 100:
            spending_chart[0].append( "%i|" % (i))
        elif i == 0:
            spending_chart[0].append("  %i|" % (i))
        else:
            spending_chart[0].append(" %i|" % (i))
    
    for i in budget_list:
        spending_total = 0
        for j in i.ledger:
            if j["amount"] < 0:
                spending_total = spending_total + (j["amount"] * -1)
        cat_totals.append({i.category:(spending_total/total)*100})
        names.append(i.category)
    for i in cat_totals:
        temp = []
        for j in i:
            for k in range(100, -1, -10):
                if i[j] >= k:
                    temp.append(" o ")
                else:
                    temp.append("   ")
        spending_chart.append(temp)
    
    for i in range(0, 11):
        temp = ""
        for j in range(len(spending_chart)):
            temp = temp + spending_chart[j][i]
        chart = chart + "\n" + temp
    temp = "    "
    for i in range(len(spending_chart)-1):
        temp = temp + "---"
    temp = temp + "-"
    chart = chart + "\n" + temp
    done = False
    counter = 0
    while done == False:
        temp = "    "
        done = True
        for i in range(len(names)):
            if counter  < len(names[i]):
                done  = False
                if i == len(names) - 1:
                    temp = temp + " %s  " %(names[i][counter])
                else:
                    temp = temp + " %s " %(names[i][counter])
            else:
                if i == len(names) - 1:
                    temp = temp + "    "
                else:
                    temp = temp + "   "
        counter = counter + 1
        chart = chart + "\n" + temp
    return chart
            
print("Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  ")
food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(create_spend_chart([business, food, entertainment]))
