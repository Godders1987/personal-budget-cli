from decimal import Decimal
from datetime import date

def main():
  # Set monthly amount
  month_amt = get_month_amt('amount.txt')
  # Keeps loop open
  while True:
    command = input('What would you like to do? (Set, Add, Balance, Reset or Exit): ')
    command = command.lower()
    if command == 'exit':
      file = open('amount.txt', 'w')
      file.write(str(month_amt))
      file.close()
      break
    elif command == 'set':
      month_amt = set_month_amt()
      print('Your monthly amount has been set at £{}.'.format(month_amt))
    elif command == 'add':
      month_amt = expense(month_amt)
      print('Your remaining budget is £{}'.format(month_amt))
    elif command == 'reset':
      file = open('amount.txt', 'w')
      file.write('0')
      file.close()
      print('Your monthly balance has been reset to £0.')
      break
    elif command == 'balance':
      days_left = payday()
      print('Your remaining monthly balance is £{} and you have {} days until payday.'.format(month_amt, days_left))
      

# Sets the monthly spend limited decidied by user
def set_month_amt():
  amt = input('What would you like to set your monthly budget at?: ')
  amt = Decimal(amt)
  return amt

# Minuses off spend from monthly budget and returns new amount
def expense(value):
  spend = input('How much have you spent?: ')
  spend = Decimal(spend)
  new_amt = value - spend
  return new_amt

# Reads the tex file that has the current remaining amount saved
def get_month_amt(filepath):
   with open(filepath) as x:
      month_amt = x.read()
      month_amt = Decimal(month_amt)
      return month_amt

# Calculates when the next payday is and calculates how many days till then
def payday():
  # Get todays date
  today = date.today()
  # Payday
  payday_day = 25
  if today.day <= payday_day:
    days_remaining = payday_day - today.day
    return days_remaining
  elif today.day > payday_day and today.month + 1 >= 12:
    next_payday = date(today.year + 1, 1, 25)
    return next_payday - today
  else:
    next_payday = date(today.year, today.month + 1, 25)
    return(next_payday - today).days
    
main()