# regex means find one or more digits between 0 and 9 then converts each string to int, then sum all numbers

# import re
#
# handler = open("actual_data.txt")
#
# numbers = list()
# for line in handler:
#     list_int = re.findall('[0-9]+', line)
#     if len(list_int) == 0 : continue
#     else:
#         for i in list_int:
#             numbers.append(int(i))
# sum_numbers = sum(numbers)
# print(sum_numbers)

#same code above, but with list comp
import re

print(sum([int(i) for i in re.findall('[0-9]+', open("actual_data.txt").read())]))
