# Write a program that asks the user to enter a mass in medieval units:
# talents (leiviskä), pounds (naula), and lots (luoti).
# The program converts the input to full kilograms and grams and outputs the result to the user:
# One talent is 20 pounds.
# One pound is 32 lots.
# One lot is 13,3 grams.
import math


def talent_gram_convertor(talent) :
    return talent*20*32*13.3
def pound_gram_convertor(pound) :
    return pound*32*13.3
def lots_gram_convertor(lots) :
    return lots*13.3


m_talent= float(input("Enter a mass in talent: "))
m_talent = talent_gram_convertor(m_talent)
m_pound = float(input("Enter a mass in pound: "))
m_pound = pound_gram_convertor(m_pound)
m_lots= float(input("Enter a mass in lots: "))
m_lots = lots_gram_convertor(m_lots)
sum = (m_talent+m_pound+m_lots)/1000
print("The sum is", int( sum), "kilograms and" ,sum%1, "gram")

