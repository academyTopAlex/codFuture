def foo(x, y):
    z = x + y
    return z


# print(foo(30, 9))

# l = lambda num: num + 10
# print(l(9))
def pl10():
    return 10


# lst = [i for i in range(100)]
# f = lambda : 10
# print(f())
# lst = list(map(lambda s, f,  : 10, lst))
# print(lst)


# with open("compres.txt", "r", encoding="utf-8") as file:
#     # x = file.read(5)
#     x = file.readlines()
#     # for item in file:
#     #     print(item)
# print(x)


# with open(r"C:\Users\Взрослая академия\Desktop\28.11.txt", "w", encoding="utf-8") as f:
#     f.write("phfkjhkjphkjpkhkjo'[")

'''
import os

with open("28.11.txt", "w", encoding="utf-8") as f:
    f.write("hfdefudhef\ndjdehjdi\njhfdef\n")

with open("28.11.txt", "r", encoding="utf-8") as f:
    lst = f.readlines()

print(lst[0])
os.rename("28.11.txt", "pokox3Pro.txt")
'''

import json

# d = {
#     1: "23",
#     2: "fjirfj",
#     3: [1, 2, 3, 3, 4],
#     4: {
#         5: 89,
#         6: 98
#     }
# }
#
# with open("myJson.json", "w", encoding="utf-8") as f:
#     json.dump(d, f, indent=4)
#
# with open("myJson.json", 'r', encoding="utf-8") as f:
#    new_d = f.read()
#
# print(type(new_d))
# print(new_d["1"])
#

d = {}


def get_info_from_user():
    return input("введите ключ\n"), input("введите значение\n")


for i in range(3):
    k, v = get_info_from_user()
    d[k] = v

with open("../myJson.json", "w", encoding="utf-8") as f:
    json.dump(d, f, indent=4)
