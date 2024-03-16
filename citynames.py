from name_function import get_formatted_name
print("Enter 'q' at any time to quit.")
while True:
 first = input("\nPlease give me a city name: ")
 if first == 'q':
  break
 last = input("Please give me a country name: ")
 if last == 'q':
  break
 formatted_name = get_formatted_name(first, last)
 print(f"\tNeatly formatted name: {formatted_name}.")