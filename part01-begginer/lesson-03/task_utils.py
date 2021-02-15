"""
methods to use in this assignment
"""
import re


def get_int(message='Enter an integer digital: '):
    while True:
        digital = input(message)
        try:
            digital = int(digital)
            return digital
        except ValueError:
            print('NOT INT. Try again')


def get_email():
    while True:
        email = input('Enter email: ')
        result = re.fullmatch(r'[a-zA-Z]{3,}\w*@[a-zA-Z0-9]{2,}\.(com|ru)', email)
        if result:
            return email
        else:
            print("Incorrect email. Try again")


def get_phone():
    while True:
        phone = input("Enter phone number: ").replace("-", "").replace(" ","")
        result = re.fullmatch(r'\+?\d{3,20}', phone)
        if result:
            return phone
        else:
            print("Incorrect phone number. Try again")
