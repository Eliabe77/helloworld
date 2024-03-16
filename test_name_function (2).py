from name_function import get_formatted_name
1 def test_first_last_name():
 """Do names like 'Janis Joplin' work?"""
2 formatted_name = get_formatted_name('janis', 'joplin')
3 assert formatted_name == 'Janis Joplin'