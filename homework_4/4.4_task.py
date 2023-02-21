import re

camel_case_list = ['FirstItem', 'FriendsList', 'MyTuple']
camel_case_str = " ".join(camel_case_list)
snake_case_str = re.sub(r'(?<!^)(?<!\s)(?=[A-Z])', '_', camel_case_str).lower()
snake_case_list = snake_case_str.split(' ')
print(snake_case_list)
