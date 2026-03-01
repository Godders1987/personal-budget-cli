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
      exit('amount.txt', month_amt)
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

# Reads the text file that has the current remaining amount saved
def get_month_amt(filepath):
   with open(filepath) as x:
      month_amt = x.read()
      month_amt = Decimal(month_amt)
      return month_amt
   
# Exit function
def exit(file, month_amt):
  with open(file, 'w') as x:
    x.write(str(month_amt))
    x.close()


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