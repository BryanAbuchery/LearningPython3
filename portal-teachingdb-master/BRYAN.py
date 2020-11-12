#These are my self created modules from different exercises
def fibonacci():
    """Fibonacci numbers generator"""
    a = int(input("Please Enter number of fibonacci sequence: "))
    b = firstnumber = 0
    c = 1
    while firstnumber < a:
        print(b, end=",")
        firstnumber = firstnumber + 1
        newtotal = b + c
        b = c
        c = newtotal



def random_word():
    """Downloads and Picks a Random Word"""
    import urllib.request
    url = "http://norvig.com/ngrams/sowpods.txt"
    response = urllib.request.urlopen(url)
    data = response.read()
    f = open('SOWPODS', 'wb')
    f.write(data)
    f.close
    text = [word for line in open('SOWPODS', 'r') for word in line.split()]
    import random
    word = random.choice(text)
    return word




def reverse_order():
    """Requests for a string, and returns it as a list in reverse order"""
    a = input("Please type a sentence of ANY length: ")
    list1 = list(a.split(" "))
    #print(list1) if you want to print your new list
    a = list1[::-1]
    return a





def game():
    """Introduces a guessing game for you to guess the correct random number generated"""
    import random
    n = int(input("Guess any number between 1 to 9, enter 0 to exit: "))
    a = random.randint(1,9)
    guess = 0
    while n != a:
        if n < a and n > 0:
            print("You are getting colder, out of range!")
            n = int(input("Guess any number between 1 to 9, enter 0 to exit: "))
            a = random.randint(1,9)
            guess +=1
            total = guess + 1
            if n==0:
                break
        elif n > a:
            print("You are getting hotter, out of range!")
            n = int(input("Guess any number between 1 to 9, enter 0 to exit: "))
            a = random.randint(1,9)
            guess +=1
            total = guess + 1
            if n==0:
                break
        elif n == a:
            print("You are right, congrtulations!")
            guess +=1
            total = guess + 1
            break
    else:
        print("You are right, congratulations!")
    print("You have had %d guesses" %total)





def common_list1():
    """Checks for a common items in two lists"""
    print("This function checks and brings a common list between any of your two lists")
    a = input("Enter the first list of numbers separated by space: ")
    b = input("Enter the second list of numbers separated by space: ")
    a_list = a.split()
    b_list = b.split()
    set_a = set(a_list)
    set_b = set(b_list)
    intersection = set_a.intersection(set_b)
    common_list = list(intersection)
    return common_list




def prime_numbers():
    """Prints out a sequence of prime numbers limited by your input"""
    a = 0
    n = int(input("Please enter any integer: "))
    print("Prime numbers between", a, "and", n, "are:")
    for num in range(a, n + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num, end=",")




def prime_checker():
    """Checks if your input is a prime number"""
    b = int(input("Please enter any integer to check if it is a Prime Number: "))
    if b > 1:
        for i in range(2, b // 2):
            if (b % i) == 0:
                print(b, "is not a Prime Number")
                break
            else:
                print(b, "is a Prime Number")
        else:
            print(b, "is not a Prime Number")



def passwords():
    """Generates for you the strongest passwords for use"""
    import random
    import string
    random_word = string.ascii_letters + string.digits + string.punctuation
    password = random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)
    for i in range(9):
        password += random.choice(random_word)
    password_list = list(password)
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return ("Your strong password option is", password)




def remove_duplicates():
    """Removes all duplicates from your list"""
    a = input("Please enter any item list here, including numbers: ")
    print("I will now eliminate any duplicates from your list")
    list_a = list(a.split(" "))
    set_a = set(list_a)
    b = list(set_a)
    return b




def future_you():
    """Tells you the year you turn 100 years old"""
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    total = 2020
    a = 100 - age
    new_total = total + a
    return ("You will turn 100 years old in the year;", new_total)





def check_palindrome():
    """Checks if your input word is a palindrome"""
    a = input("Please enter a word that you think is palindromic: ")
    rev_a = reversed(a)
    if list(a) == list(rev_a):
        print("%s IS a palindrome" %(a))
    else:
        print("%s is NOT a Palindrome" %(a))

