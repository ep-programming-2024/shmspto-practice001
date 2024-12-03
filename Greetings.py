def Greet():
    print("Hello",end=" ")
    print("world")

def GermanGreet():
    print("Gesundeit")

def FrenchGreet():
    print("Bon Jour")

def ToHindi(actualword):
    if(actualword == "hello"):
        print("Hindi word is " + "Namaste")
    elif(actualword == "bye"):
        print("Hindi word is " + "Alvidaa")
    elif(actualword == "Whats up?"):
        print("Hindi word is " + "Kya chal rahaa hain?")
    else:
        print("Hindi word is " + actualword)