prompt = "How old are you?"
prompt += "\n Thank you for your answer "

while True:
    age = input(prompt)
    
    age = int(age)
    
    if age < 3:
        print("  You get in free!")
    elif age < 13:
         print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")
    
    while age >="0":
        break
    

    
          
          