'''
In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

Hints
Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods.
Be sure to give $0 not only for “hello” but also “hello there”, “hello, Newman”, and the like.
'''

def main():
    greet = input("Greeting! ")

    True if ask(greet) else False

def ask(some_greet):
    if some_greet.strip().lower().startswith('hello'):
           return print("$0")
    elif some_greet.strip().lower().startswith('h'):
            return print("$20")
    else:
            return print("$100")
       
main()