from random import Random, randrange

print("WELCOME TO BAND NAME GENERATOR[FIRST PYTHON PROJECT]")
question=["What's Your Name :","What's your city name : ","Your favorate fruit's name : "]
name=input(question[randrange(0,len(question)-1)])
#geting first name of user

pet_name =input("What's Your Pet name : \n")
#user's pet name 

print(f"Your band name should be {name} {pet_name}")
#generate band name combining username and user's pet name

