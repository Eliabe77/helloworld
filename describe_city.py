def get_formatted_name(city_name, country_name):
 """Return a full name, neatly formatted."""
 full_name = f"{city_name} {country_name}"
 return full_name.title()
while True:
 print("\nPlease tell me city and country name:")
 print("(enter 'q' at any time to quit)")
 f_name = input("City name: ")
 if f_name == 'q':
  break
 l_name = input("Country name: ")
 if l_name == 'q':
  break
 formatted_name = get_formatted_name(f_name, l_name)
 print(f"\nHello, {formatted_name}!")