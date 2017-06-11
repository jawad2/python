import random
import string

print("Welcome to Password Generating script!")
print("Created by ------------ (Jawad Ali) ---------------- email >> jawadali565@yahoo.com")
print("                                                                                 ")
print("                                                                                 ")
print("Please enter the number of characters you want to be your password, please enter an integer number")



small_letters = string.ascii_lowercase[:]
capital_letters = string.ascii_uppercase[:]
digits = string.digits[:]
punc = string.punctuation[:]

lst = small_letters + capital_letters + str(digits) + punc


def selection():
    user = int(input("Please select a number >> "))
    password_gernator(user)


def password_gernator(n):
    password = ""
    length = len(lst)

    while len(password) != n:
        r = random.randint(0, length - 1)
        for p in lst[r]:
             password += p

    print(password)

selection()