
def mathMod1(theNumber):
    reverseNumber = 0
    while(theNumber > 0):
        remainder = theNumber %10
        reverseNumber = (reverseNumber *10) + remainder
        theNumber = theNumber //10
    return reverseNumber


def mathMod2(MyNumber):
    Reverse_Number = 0
    temp = ReverseNumber
    Reminder = 1
    for i in range (Reminder+2):
        Reminder = MyNumber %10
        Reverse_Number = (ReverseNumber *10) + Reminder
        MyNumber = MyNumber //10
    print("Reverse of the provided number is = %d" %ReverseNumber)