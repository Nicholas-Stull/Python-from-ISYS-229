userName = input("what is your name? ")
userAge = input("And how old are you? ")

print("Hello " + userName)

if int(userAge) >= 18:
	print("You are old enough to vote in the U.S.")
else:
	print("Wait until you turn 18 years of age before you can vote in the U.S.")
