import sys
import random
ans= True

while ans:
    question = input("Ask the magic 8 ball a question: ")

    answers = random.randint(1,9)

if question == " ":
 sys.exit()

elif answers== 1:
    print("Yes definetely")

elif answers == 2:
    print("It is definetely so")

elif answers == 3:
    print("Without a doubt")

elif answers == 4:
    print("Reply hazy, try again")

elif answers == 5:
    print("Ask again later.")

elif answers == 6:
    print("Better not tell you now")

elif answers == 7:
    print("My sources say no")

elif answers == 8:
    print("Outlook not so good")

elif answers == 9:
    print("Very doubtful")
