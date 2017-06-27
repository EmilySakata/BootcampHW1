#homework 1, rps.py

#initial veriable definition
balance = 50
wins = 0
losses = 0
ties= 0

computerHand = ["r"]
computerWin = ["p"]
computerLose =["s"]

#print the initial balance
print("you have $"+ str(balance))

# get the input from player

player = input ("Chose r, p or s")

# print result of the game
if (player in computerHand):
	print("you tied with the computer!")
	ties = ties +1

if(player in computerLose):
	print ("Computer beat you")
	losses = losses +1
	balance = balance -10

if (player in computerWin):
	wins= wins+1
	balance = balance +10

# print current balance
print ("you have $" +str(balance))
print("wins :" + str(wins))
print("losses :" + str(losses))
print("ties :" + str(ties))

#check if you have enough balance
while(balance >0):

# play again or not
	PlayAgain = input("play again ? y or n")
	if(PlayAgain =="y"):

#print the current balance
		print("you have $"+ str(balance))

# get the input from player

		player = input ("Chose r, p or s")

# print result of the game
		if (player in computerHand):
			print("you tied with the computer!")
			ties = ties +1

		if(player in computerLose):
			print ("Computer beat you")
			losses = losses +1
			balance = balance -10

		if (player in computerWin):
			wins= wins+1
			balance = balance +10

# print current balance
		print ("you have $" +str(balance))
		print("wins :" + str(wins))
		print("losses :" + str(losses))
		print("ties :" + str(ties))
	else:
		print("thanks for playing the game.")
		exit()

	if (balance ==0):
		print ("You do not have enough money! You are done.")
# play until your balance is 0 or you end the game
