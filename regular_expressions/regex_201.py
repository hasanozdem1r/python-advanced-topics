import re

name_list=["�zcan", "mehmet", "s�leyman", "selim","kemal", "�zkan", "esra", "d�ndar", "esin","esma", "�zhan", "�zlem"]

print(re.search('�z[chk]an',name_list))