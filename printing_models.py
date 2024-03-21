def make_pizza(size, *features):
 """Summarize the model we are about to make."""
 print(f"\nMaking a {size}-inch model with the following features:")
 for feature in features:
  print(f"- {feature}")