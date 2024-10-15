data_s =  open('input.txt', 'r')
data = data_s.read()
data_split = data.split()

a = int(data_split[0])
b = int(data_split[1])

if a == b:
    ans = '='
elif a > b:
    ans = '>'
else:
    ans = '<'








output_data = open('output.txt', 'w')
output_data.write(ans)
#запись

data_s.close()
output_data.close()
#ОБЯЗАТЕЛЬНО не забывать