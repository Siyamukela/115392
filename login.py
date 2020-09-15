# Get users from textfile
with open('data.txt') as f:
    users = [line.rstrip() for line in f]
# create a database
database = {}
for user in users:
    username,password = user.split(' === ')
    database[username] = password

guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
name = input("please enter your name:")


if name in database.keys():
    password = database[name]
else:
    print('Enter a valid name')
    exit()
while guess != password and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter password:")
        guess_count = guess_count + 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You have been locked out. Try again in 5 min!")
else:
    print("Welcome " + name )

