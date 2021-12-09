""" to generate the random number from given list """
import random
n = int(input("Enter number of elements : "))
a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
print("\nList is - ", a)
print(random.choice(a))

"""to generate random character from the string"""
str = input("enter the string: ")
print(random.choice(str))
