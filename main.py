#imports#
import time, math, sys, random

#functions#

def ans(x = ">>> "):
    return input(x)

def text(*string, speed = 0.038):
    for j in string:
        for i in str(j): 
            print(i, end = "")
            time.sleep(speed)
    print()

def lifeDecider():
    text("What would you like your name to be?")
    name = ans()
    while True:
        text("Are you\n1.Male\n2.Female")
        x = ans()
        if x == "1":
        	gender = "male"
        	break
        elif x == "2":
        	gender = "female"
        	break
        else:
        	text("You have failes this menial task.\nPlease do better next time")
    global character
    character = player(name, gender)

#objects#

class player:
    def __init__(self, name, gender, descriptor = None):
        #stores the 'identity' informaion#
        self.general = {
            "name" : name,
            "gender" : gender,
            "age" : 13,
            "degree" : "None",
            "money" : 200,
            "health" : 0,
            "happyness" : 100,
            "total earnings" : 10,
            "days" : 0
            }

        self.parents = {
            "descriptor" : descriptor,
            "relationship" : 200,
            "relationship descriptor" : "ok",
            "allowance" : 10
            }
    
    def day(self):
    	self.general["days"] += 1
    	self.general["money"] += self.general["total earnings"]
    	for i in range(10):
    		if self.general["age"] < i * 10:
    			self.general["health"] -= i - 4
    			break
    	if self.general["health"] > 100:
    		self.general["health"] = 100
    	if self.general["health"] == 0:
    			text("you loose")
    	text("what would you like to do")
    	x = ans()
    	if x == "end":
    		character.day()
    	elif x == "info":
    	    character.you()
    			
    		

    def you(self):
        for i in self.general:
            text(i, " : ", self.general[i])

    def help(self):
    	pass

#testing#
lifeDecider()
character.you()
character.day()
character.you()
