def findMaxNum(arr):
    max_num = arr[0]
    for i in arr[1:]:
        if i >max_num:
            max_num = i
    return max_num
def findMinNum(arr):
    min_num = arr[0]
    for i in arr[1:]:
        if i < min_num:
            min_num = i
    return min_num
arr = [-11, 2, 3, 44, 5, 6, 7, 8, 9, 10]
resut = findMaxNum(arr)
resutmin = findMinNum(arr)
# print(resut)
# print(resutmin)

# reverse number in python with builin str method
def reverseNumber(num):
    num_str = str(num)
    rev = num_str[::-1] #reverse string 
    rev_num  = int(rev)
    return rev_num

print(reverseNumber(12345))