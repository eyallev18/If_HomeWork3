"""
This is Excersise #3
written by Eyal Lev
Date March 23rd 2019
Function That get three parameters and  check if two or more parameters are equal (True) others return False
"""



def two_or_more_equal(parameter1,parameter2,parameter3):

    if int(parameter1) == int(parameter2) or int(parameter1)== int(parameter3) or int(parameter2) == int(parameter3):
        return True

    else:
        return False




print (two_or_more_equal(1,"3",3))
print (two_or_more_equal(5,"5",7))
print (two_or_more_equal(4,"5",7))
print (two_or_more_equal(4,"5","5"))










