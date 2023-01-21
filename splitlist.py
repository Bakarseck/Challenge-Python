a = int(input())

tab = []

str_number = input()

for element in str_element:
  if element != ' ':
    tab.append(element)
    
 tab.sort()

print(tab[-1] * tab[-2])
