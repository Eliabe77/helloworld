prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished. Thank you for your answer "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")
x = len(prompt)
