print("Please provide a password that contains at least 2 digits and is 10 characters long or more.")
user_input = input('\nYour password: ')
digit_count = 0
alpha_count = 0
alnum_count = 0

for i in user_input:
  if i.isnumeric() == True:
    digit_count += 1

for i in user_input:
  if i.isalpha() == True:
    alpha_count += 1

for i in user_input:
  if i.isalnum() == True:
    alnum_count += 1

if alnum_count >= 10 and digit_count >= 2:
  print("Password accepted")
else:
  print("Password not accepeted")
  print(f'\nYour password contains {digit_count} digits and {alpha_count} letters. \n\nPlease provide a password that meets the criteria mentioned above')

