# import random to get a random answer to question
import random
# ask their question
q=input("Enter your yes/no question here: ")
# 20 possible answers
answer=["As I see it, yes", 
 "Ask again later.", 
 "Better not tell you now.", 
 "Cannot predict now.", 
 "Concentrate and ask again.", 
 "Don’t count on it.", 
 "It is certain.", 
 "It is decidedly so.", 
 "Most likely.", 
 "My reply is no.", 
 "My sources say no.", 
 "Outlook not so good.", 
 "Outlook good.", 
 "Reply hazy, try again.", 
 "Signs point to yes.", 
 "Very doubtful.", 
 "Without a doubt.", 
 "Yes.", 
 "Yes – definitely.", 
 "You may rely on it."]
#print answer
print(random.choice(answer))