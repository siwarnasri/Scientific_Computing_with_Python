class Category:

  # Instantiate objects based on different budget categories
  def __init__(self, category):
    self.category = category
    self.ledger = []

  # Displaying the budget object
  def __str__(self):
    # A line of 30 characters where the name of the category is centered in a line of * characters
    s = self.category.center(30, "*") + "\n"

    # Dislay the list of items in the ledger
    for item in self.ledger:

      # Show, the 23 firt characters of the description and then the amount, of each item
      temp = f"{item['description'][:23]:23}{item['amount']:7.2f}" # "7.2f" means to schow a maximum of 7 characters and two decimal places
      s += temp + "\n"
    # Display the category total
    s += "Total: " + str(self.get_balance())
    return s

  # Deposit method accepts an amount and a description
  def deposit(self, amount, description=""):
    # Append an object to the ledger list
    self.ledger.append({'amount': amount,'description': description})

  # Withdraw method accepts an amount and a desription
  def withdraw(self, amount, description=""):

    # Checking if the withdrawal took place, store it in the ledger as a negative number and return "true"
    if self.check_funds(amount):
      self.ledger.append({'amount': 0 - amount,'description': description})
      return True

    # If there is not enough funds, return "False" and nothing to add to the ledger
    return False

  # Get_balance method returns the balance of the budget category
  def get_balance(self):
    balance = 0
    for item in self.ledger:
      balance += item['amount']
    return balance

  # Transfer method accepts an amount and a budget category
  def transfer(self, amount, budget_cat):
    # This method will return "True" if there is an amount to be transfered from source budget category using the deposit method, to the destination budget category using the withdraw method
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to " + budget_cat.category)
      budget_cat.deposit(amount, "Transfer from " + self.category)
      return True
    # Return "False" and nothing should be added if there are not enough funds
    return False

  # Check_funds method returns "False" if the amount (accepted as an argument) is greater than the balance of the budget category
  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    # Return "True" if the balance of the budget category is greater then the amount passed as argumnt
    return True

# Create_spend_chart is a function that takes a list of categories as an argument
def create_spend_chart(categories):
  spend = []
  for category in categories:
    temp = 0
    for item in category.ledger:
      if item['amount'] < 0:
        temp += abs(item['amount'])
    spend.append(temp)
  
  total = sum(spend)
  # Calculate the percentage spent in each category passed in to the function
  percentage = [i/total * 100 for i in spend]
  # A title at the top
  s = "Percentage spent by category"
  # Down the left side of the chart should be labels 0 - 100
  for i in range(100, -1, -10):
    s += "\n" + str(i).rjust(3) + "|"
    # The "bars" in the bar chart should be made out of the "o" character
    for j in percentage:
      if j > i:
        s += " o "
      # The horizontal line below the bars should go two spaces past the final bar
      else:
        s += "   "
    # Spaces
    s += " "
  s += "\n    ----------"

  cat_length = []
  for category in categories:
    cat_length.append(len(category.category))
  max_length = max(cat_length)

  for i in range(max_length):
    s += "\n    "
    for j in range(len(categories)):
      if i < cat_length[j]:
        s += " " + categories[j].category[i] + " "
      else:
        s += "   "
    # Spaces
    s += " "
  # Return a bar chart string that show the percentage spent in each category passed in to the function
  return s