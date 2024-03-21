def greet_users(names):
 """Print a simple greeting to each user in the list."""
 for name in names:
   msg = f"Hi, {name.title()}!"
   print(msg)
   msg = f"Welcome, {name.title()}!"
   print(msg)
   msg = f"How are you?, {name.title()}!"
   print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)