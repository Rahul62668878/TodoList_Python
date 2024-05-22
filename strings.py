import random
import string
result = string.ascii_letters
myinput = string.digits
# print(myinput)
def check(value):
    for i in value:
        if i not in string.ascii_letters:
            return False
    return True
# let use real life application
def ran_pass(size):
    genratepass=''.join([random.choice(string.ascii_letters+string.digits) for i in range(size)])
    return genratepass
# result  = check(myinput)
# result  = ran_pass(10)
# print(string.ascii_uppercase)
# print(string.ascii_lowercase)
# print(string.ascii_letters)
# print(string.lowercase)
name = "rahul sharma"
def string_reverse(str):
    str = ''
    for i in str:
        str = i+str
    return str
# reversename = string_reverse(name)
import itertools
import operator
gfg = [1,2,3,4,5]
result = itertools.accumulate(gfg, operator.add)
for i in result:
    print(i)
# print('reverse string is:',result)