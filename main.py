from decimal import Decimal, InvalidOperation
from datetime import date

def main():
  # Set monthly amount
  month_amt = get_month_amt('amount.txt')
  if month_amt == 0:
    print('You have not yet set your monthly budget!')
    set_amt = input('What would you like to set your monthly budget at?: ')
    month_amt = check_input(set_amt)
  else:
    days_left = payday()
    print('Your remaining monthly balance is £{} and you have {} days until payday.'.format(month_amt, days_left))
  # Keeps loop open
  while True:
    command = input('What would you like to do? (Set, Add, Balance, Reset or Exit): ')
    command = command.lower()
    if command == 'exit':
      save_amt('amount.txt', month_amt)
      break
    elif command == 'set':
      while True:
        set_amt = input('What would you like to set your monthly budget at?: ')
        try:
          month_amt = check_input(set_amt)
          print('Your monthly amount has been set at £{}.'.format(month_amt))
          break
        except InvalidOperation:
          print('Invalid input, please try again!') 
    elif command == 'add':
      while True: 
        spent = (input('How much have you spent?: '))
        try:
          dec_spent = check_input(spent)
          month_amt = expense(month_amt, dec_spent)
          break
        except InvalidOperation:
          print('Invalid input, please try again!')     
      print('Your remaining budget is £{}'.format(month_amt))
    elif command == 'reset':
      reset('amount.txt')
      print('Your monthly balance has been reset to £0.')
      break
    elif command == 'balance':
      days_left = payday()
      print('Your remaining monthly balance is £{} and you have {} days until payday.'.format(month_amt, days_left))

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
def reset(file):
  with open(file, 'w') as x:
    x.write('0')

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