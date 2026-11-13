#training on functions and inputs
f_name = input("What is your name ?")
f_age = int(input("What is your age ?"))
def format_name(name,age):
    return f"hello {name}, you are {age} years old."
print(format_name(f_name.title(),f_age))

#trying to create title 
def function(text):
    return text.title()
print(function("hello_worlD"))

#challenge Leap Year
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

print(is_leap_year(2000))