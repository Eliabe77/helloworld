def build_profile(brand, model, **user_info):
 """Build a dictionary containing everything we know about a car."""
 user_info['brand_name'] = brand
 user_info['model_name'] = model
 return user_info
user_profile = build_profile('Mazda', 'cx30',
 engine='hibryd',
 wheels='4'), 
year='2017'
grade='8/10',
print(user_profile),
