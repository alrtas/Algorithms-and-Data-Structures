import linkedlist

my_list = linkedlist.LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.display()
print my_list.length()
print my_list.get(2)

my_list.erase(0)
my_list.display()
my_list.prepend(1)
my_list.display()

del my_list

