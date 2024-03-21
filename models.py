def make_model(size, *data):
 """Summarize the pizza we are about to make."""
 print(f"\nMaking a {size}-inch screw with the following data:")
 for data in data:
  print(f"- {data}")