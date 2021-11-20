import re

name_list=["özcan", "mehmet", "süleyman", "selim","kemal", "özkan", "esra", "dündar", "esin","esma", "özhan", "özlem"]

print(re.search('öz[chk]an',name_list))