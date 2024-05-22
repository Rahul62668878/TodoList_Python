# list =   [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# count = 0
# for i in list:
#     if len(i)>0 and i[0] == i[-1]:
#         count+=1
# print(count)
def remove_duplicates(list):
    new_list = []
    for item in list:
        if item not in new_list:
            new_list.append(item)
    return new_list
def is_empty(list):
    if len(list)>0:
        return list
    else:
        return "List is empty"
def clone_list(list):
    clone_list = []
    for i in range(len(list)):
        clone_list.append(list[i])
    return clone_list
def long_word(str,n):
    word_len = []
    text = str.split(" ")
    for i in text:
        if len(i) > n:
            word_len.append(i)
    print(word_len)
def flattend_list(list):
    new_list = []
    for i in list:
        for j in i:
            new_list.append(j)
    print(new_list)

# Example usage:
from random import shuffle
import itertools
# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
# flattend_list = [j for i in original_list for j in i]
# sorted_list = sorted([1, 1, 0, 0, 2, -2, -2])
# new_set = set(sorted_list)
# new_set = list(new_set)
# print(new_set)
# flattend_list(original_list)
# array = [[["x" for x in range(6)]for i in range(4)] for x in range(3)]
# print(shuffle(color))
# print(list(itertools.permutations(numb)))

original_list =  [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]  
def count_fecuency(list):
    dict = {}
    for i in list:
        if i in dict:
            dict[i]+=1
        else:
            dict[i] = 1
    return dict
def count_numberitems(list,min,max):
    count = 0
    mylist = []
    for i in list:
        if min <= i <=max:
            count+=1
            mylist.append(i)
    return count,mylist
Sample_list =['p', 'q']
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
new_list = []

# for i in range(5):
#     for j in range(2):
#         new_list.append(Sample_list[j]+str(i+1))
# print(count_numberitems(original_list,6,10))

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4= {**dic1,**dic2,**dic3}
if 5 in dic4:
    print("Yes")
# d[2] = 30
print(dic4)
# print(dict(sorted(d.items(), key=lambda x: x[1])))