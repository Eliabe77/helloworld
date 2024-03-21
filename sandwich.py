def make_sandwich(size, *toppings):
 """Summarize the sandwich we are about to make."""
 print(f"\nMaking a {size}-inch sandwich with the following toppings:")
 for topping in toppings:
  print(f"- {topping}")
make_sandwich(16, 'pepperoni')
make_sandwich(12, 'mushrooms', 'green peppers', 'extra cheese')