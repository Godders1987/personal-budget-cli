from decimal import Decimal, InvalidOperation
from datetime import date

def main():
  # Set monthly amount
  open('transactions.txt', 'a').close()
  with open('amount.txt') as x:
    if x.read(1):
      month_amt = calculate_balance()
      days_left = payday()
      print('Your remaining monthly balance is £{} and you have {} days until payday.'.format(month_amt, days_left))
    else:
      print('You have not yet set your monthly budget!')
      month_amt = set_monthly_amt()
      save_amt('amount.txt', month_amt)
  while True:
    command = input('What would you like to do? (Set, Add, Balance, History, Reset or Exit): ')
    command = command.lower()
    if command == 'exit':
      break
    elif command == 'set':
      month_amt = set_monthly_amt()
    elif command == 'add':
      while True: 
        description = input('What did you buy?: ')
        description = description.capitalize()
        spent = (input('How much have you spent?: '))
        try:
          dec_spent = check_input(spent)
          month_amt = expense(month_amt, dec_spent)
          transactions(description, dec_spent)
          break
        except InvalidOperation:
          print('Invalid input, please try again!')     
      print('Your remaining budget is £{}'.format(month_amt))
    elif command == 'reset':
      reset('amount.txt', 'transactions.txt')
      print('Your monthly balance has been reset to £0.')
      break
    elif command == 'balance':
      remaining = calculate_balance()
      days_left = payday()
      print('Your remaining monthly balance is £{} and you have {} days until payday.'.format(remaining, days_left))
    elif command == 'history':
      history()

# Checks and sets the monthly budget
def set_monthly_amt():
  while True:
      set_amt = input('What would you like to set your monthly budget at?: ')
      try:
        month_amt = check_input(set_amt)
        print('Your monthly amount has been set at £{}.'.format(month_amt))
        return month_amt
        break
      except InvalidOperation:
        print('Invalid input, please try again!')

# Check if user input is both a number and a positive number
def check_input(value):
    check = Decimal(value)
    if check > 0:
      return check
    else:
      raise InvalidOperation
    
# Minuses off spend from monthly budget and returns new amount
def expense(month_amt, value):
  return month_amt - value

def calculate_balance():
  budget = get_month_amt('amount.txt')
  total_spend = Decimal(0)
  with open('transactions.txt') as s:
    for x in s:
      details = x.strip().split(',')
      total_spend += Decimal(details[2])
    return budget - total_spend

# writes transaction to transactions file
def transactions(description, amount):
  today = date.today()
  with open('transactions.txt', 'a')as t:
    t.write(f"{today}, {description}, {amount}\n")

def history():
  with open('transactions.txt') as t:
     for x in t:
       info = x.strip().split(',')
       print("Date: {} | Description: {} | Amount: £{}".format(info[0].strip(), info[1].strip(), info[2].strip()))

# Reads the text file that has the current remaining amount saved
def get_month_amt(filepath):
   with open(filepath) as x:
      month_amt = x.read()
      month_amt = Decimal(month_amt)
      return month_amt
   
# Exit function
def save_amt(file, month_amt):
  with open(file, 'w') as x:
    x.write(str(month_amt))

# Reset function
def reset(file_one, file_two):
  with open(file_one, 'w') as x, open(file_two, 'w') as y:
    x.write('')
    y.write('')

# Calculates when the next payday is and calculates how many days till then
def payday():
  # Get todays date
  today = date.today()
  # Payday
  this_month_payday = date(today.year, today.month, 25)

  if this_month_payday > today:
    return (this_month_payday - today).days
  elif today > this_month_payday and today.month < 12:
    return (date(today.year, today.month + 1, 25) - today).days
  else: 
    return (date(today.year + 1, 1, 25) - today).days
  
    
main()