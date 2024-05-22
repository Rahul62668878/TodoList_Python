class CustomList:
    def __init__(self):
        self.items = []
        self.len = 0

    def append(self, item):
        new_items = [None] * (len(self.items) + 1)
        for i in range(len(self.items)):
            new_items[i] = self.items[i]
        new_items[len(self.items)] = item
        self.len += 1
        self.items = new_items
        # print(f'{item} added to list')
        # print(f'Current List is {self.items}')

    def clear(self):
        self.items = []

    def copy(self):
        new_list = []
        for i in range(len(self.items)):
            new_list.append(self.items[i])
        return new_list

    def extend(self, list):
        for i in range(len(list)):
            self.items.append(list[i])
            self.len += 1

    def index(self, item):
        for i in range(len(self.items)):
            if self.items[i] == item:
                return i
        raise ValueError(f"{item} not found")

    def insert(self, index, item):
        new_items = [None] * (len(self.items) + 1)
        for i in range(len(self.items)):
            if i < index:
                new_items[i] = self.items[i]
            elif i == index:
                new_items[i] = item
            else:
                new_items[i] = self.items[i - 1]
        self.items = new_items

    def pop(self, index=None):
        if not self.items:
            raise IndexError("pop from empty list")
        if index is None:
            index = len(self.items) - 1
        item = self.items[index]
        new_items = [None] * (len(self.items) - 1)
        for i in range(len(self.items)):
            if i < index:
                new_items[i] = self.items[i]
            elif i > index:
                new_items[i - 1] = self.items[i]
        self.items = new_items
        self.len -= 1
        return item

    def __str__(self):
        return f"{self.items}"

    def __len__(self):
        return self.len


# list = CustomList()
# print(dir(list.items))
# print(list)
# list.append("mango")
# list.append('apple')
# list.append('apple')
# list.append('apple')

# list.clear()
# print(list,id(list))
# list.copy()
# print(list,id(list))

# list.extend(["banana", "grapes"])
# list.pop(2)
# print(list.index("watermaleon"))
# list.insert(1, "watermelon")
# list.insert(2, "watermelon")
# print(len(list))
# print(list)

# lst = ['a', 'b', 'c']
lst = []
# my_dict = {i:lst[i] for i in range(1,len(lst))}
# my_dict = {}
# for i in range(len(lst)):``
#     my_dict[i] = lst[i]
my_dict = {0: 'a', 1: 'b', 2: 'c'}
my_dict1 = {0: 'a', 1: 'b', 2: 'c'}
# using list comprehension
lst = [ i for i in my_dict.values()]

lst2 = list(my_dict.values())
print(my_dict.values())
# for i in my_dict.values():
#     lst.append(i)

#     print(i)
# print(my_dict)
print(lst)
print(lst2)