import re

string = input()

a = re.fullmatch('(10(0)+(1)+|(01))+', string)
if a is not None:
    print('SUBMARINE')
else:
    print('NOISE')

