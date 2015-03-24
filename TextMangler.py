__author__ = 'Tyler Price'

import sys

header = """

TextMangler.py

By: Tyler Price

Usage: TextMangler.py {Number1 of Range} {Number 2 of Range} {Year1 of Range} {Year2 or Range}

Example: ./TextMangler.py 0 10 1990 2000

"""

def Numbers(text, num1, num2):

    for x in text.split():

        for i in range(num1, num2):
            
            print ("%s" + "%s") % (x, i)
            print ("%s" + "%s") % (i, x)


def Years(text, year1, year2):

    for x in text.split():

        for i in range(year1, year2):
            
            print ("%s" + "%s") % (x, i)
            print ("%s" + "%s") % (i, x)


def Unique(text, special1, special2, special3):

    for x in text.split():
        print x + x + special1
        print x + x + special2
        print x + x + special3
        print x + x


def UniqueNum(text, num1, num2):
    
      for x in text.split():
          
          for i in range(num1, num2):

              print ("%s" + "%s" + "%s") % (x, x, i)


def UniqueYears(text, year1, year2):

    for x in text.split():
          
          for i in range(year1, year2):

              print ("%s" + "%s" + "%s") % (x, x, i)



def FirstLetterCapNum(text, num1, num2):

    for x in text.split():

        for i in range(num1, num2):
            
            print ("%s" + "%s") % (x.capitalize(), i)
            print ("%s" + "%s") % (i, x.capitalize())

def Caps(text):

    for x in text.split():

        print x.capitalize()


def UniqueCaps(text):

    for x in text.split():

        print ("%s" + "s") % (x.capitalize(), x.capitalize())
    


def CapandYears(text, year1, year2):

    for x in text.split():

        for i in range(year1, year2):
            
            print ("%s" + "%s") % (x.capitalize(), i)
            print ("%s" + "%s") % (i, x.capitalize())
        
    
def Leet(text):

    for x in text.split():
        print x.replace("e", "3").replace("i", "1").replace("O", "0").replace("I", "1").replace("E", "3").replace("o", "0").replace("l", "1").replace("L", "1").replace("g", "9").replace("G", "6").replace("b", "8").replace("B", "8")



def LeetCap(text):

    for x in text.split():
        print x.capitalize().replace("e", "3").replace("i", "1").replace("O", "0").replace("I", "1").replace("E", "3").replace("o", "0").replace("l", "1").replace("L", "1").replace("g", "9").replace("G", "6").replace("b", "8").replace("B", "8")



def LeetYears(text, year1, year2):

    for x in text.split():

        for i in range(year1, year2):

            print ("%s" + "%s") % (x.replace("e", "3").replace("i", "1").replace("O", "0").replace("I", "1").replace("E", "3").replace("o", "0").replace("l", "1").replace("L", "1").replace("g", "9").replace("G", "6").replace("b", "8").replace("B", "8"), i)
            print ("%s" + "%s") % (i, x.replace("e", "3").replace("i", "1").replace("O", "0").replace("I", "1").replace("E", "3").replace("o", "0").replace("l", "1").replace("L", "1").replace("g", "9").replace("G", "6").replace("b", "8").replace("B", "8"))


def LeetNumbers(text, num1, num2):

    for x in text.split():

        for i in range(num1, num2):

            print ("%s" + "%s") % (x.replace("e", "3").replace("i", "1").replace("O", "0").replace("I", "1").replace("E", "3").replace("o", "0").replace("l", "1").replace("L", "1").replace("g", "9").replace("G", "6").replace("b", "8").replace("B", "8"), i)
            print ("%s" + "%s") % (i, x.replace("e", "3").replace("i", "1").replace("O", "0").replace("I", "1").replace("E", "3").replace("o", "0").replace("l", "1").replace("L", "1").replace("g", "9").replace("G", "6").replace("b", "8").replace("B", "8"))


def UniqueLeet(text):

    for x in text.split():

        print ("%s" + "%s") % (x.replace("e", "3").replace("i", "1").replace("O", "0").replace("I", "1").replace("E", "3").replace("o", "0").replace("l", "1").replace("L", "1").replace("g", "9").replace("G", "6").replace("b", "8").replace("B", "8"),(x.replace("e", "3").replace("i", "1").replace("O", "0").replace("I", "1").replace("E", "3").replace("o", "0").replace("l", "1").replace("L", "1").replace("g", "9").replace("G", "6").replace("b", "8").replace("B", "8")))



def Reverse(text):

    for x in text.split():

        print x[::-1]


def ReverseCap(text):

    for x in text.split():
        print x[::-1].capitalize()



def ReverseNum(text, num1, num2):

    for x in text.split():

        for i in range(num1, num2):

            print ("%s" + "%s") % (x[::-1], i)
            print ("%s" + "%s") % (i, x[::-1])



def ReverseYears(text, year1, year2):

    for x in text.split():

        for i in range(year2, year2):

            print ("%s" + "%s") % (x[::-1], i)
            print ("%s" + "%s") % (i, x[::-1])


def ReverseUnique(text):

    for x in text.split():

        print x[::-1] + x[::-1]


def Main():

    if len(sys.argv) < 4:

        print header
        sys.exit()

    special1 = "123"
    special2 = "321"
    special3 = "567"

    text = raw_input("Enter Words to Generate: ")
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2]) + 1
    year1 = int(sys.argv[3])
    year2 = int(sys.argv[4]) + 1
        
  
    Numbers(text, num1, num2)
    Years(text, year1, year2)
    Unique(text, special1, special2, special3)
    FirstLetterCapNum(text, num1, num2)
    Caps(text)
    Leet(text)
    LeetCap(text)
    CapandYears(text, year1, year2)
    LeetYears(text, year1, year2)
    LeetNumbers(text, num1, num2)
    UniqueNum(text, num1, num2)
    UniqueYears(text, year1, year2)
    Reverse(text)
    ReverseCap(text)
    ReverseNum(text, num1, num2)
    ReverseYears(text, year1, year2)
    ReverseUnique(text)

Main()




