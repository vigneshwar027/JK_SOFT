import re

a = ['yes','no']

hh= 'hi how are you'


if 'yes' in a or re.search('hi',hh):
    print('yes')

else:
    print('no')
