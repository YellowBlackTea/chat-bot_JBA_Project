# greeting the user
def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


# remind the name of the user
def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


# guess the age of the user
def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


# counting program
def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


# to test the user knowledge
def test():
    print("Let's test your programming knowledge.")
    question = "Why do we use methods?"
    print(question)
    if question[-1] == "?":
        print("1. To repeat a statement multiple times.")
        print("2. To decompose a program into several small subroutines.")
        print("3. To determine the execution time of a program.")
        print("4. To interrupt the execution of a program.")
    correct = "2"
    new_test = input()
    if new_test != correct:
        print("Please, try again.")
    else:
        pass


# end message
def end():
    print('Congratulations, have a nice day!')

