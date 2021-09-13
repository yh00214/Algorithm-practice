import re

N = int(input())

str_list = []
for _ in range(N):
    str_list.append(input())

for string in str_list:
    if re.match('^[ABCDEF]A*F*C*[ABCDEF]{0,1}$', string) is not None:
        print('Infected!')
    else:
        print('Good')