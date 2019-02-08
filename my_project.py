from Digital_Trie_Tree import DTTree
from Red_Black_Tree import *
from Merge_Sort import *
from searches import *
import timeit
from random import randint

filename = 'C:/Users/DX/Desktop/gotta do/data structures/integers.txt'


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


with open(filename) as file:
    int_list = file.readlines()

int_list = list(map(int, [x.strip() for x in int_list]))
int_list = mergeSort(int_list)


with open(filename, 'w') as file:           # writes integer list to file
    for i in range(len(int_list)):
        file.write(str((int_list[i])) + '\n')


rbTree = RBTree()                                                                 # creation of red black tree from file
with open('C:/Users/DX/Desktop/gotta do/data structures/integers.txt', 'r') as file: #
    for line in file.readlines():                                                    #
        rbTree.insert(int(line.strip()))                                             #

option = 999
while option != '99':
    option = input('What would you like to do?\n1: Search file for integer\n'
                   '2: Use Red-Black tree on file\n3: Time all available search algorithms\n'
                   '4: Use Digital-Trie tree on file\n')
    if option == '1':

        search_type = input("How would you like to search?\n1: Linear search\n"
                            "2: Binary search\n3: Interpolation search\n")
        item = input('What to search for?\n')
        if search_type == '1':
            print(linearSearch(int_list, int(item)))
        elif search_type == '2':
            print(binarySearch(int_list, item))
        elif search_type == '3':
            print(interpolationSearch(int_list, int(item)))

    if option == '2':

        while option != 'exit':
            option = input('What would you like to do?(type \'exit\' to go back to the main program)\n'
                           '1: Search for a node\n2: Insert a new node\n')
            if option == '1':
                num = int(input('What to search for?\n'))
                print(rbTree.findNode(num))
            elif option == '2':
                node = int(input('What to insert?\n'))
                rbTree.insert(node)
                print('\nInserted successfully!\n')

    if option == '3':

        lst = []
        for i in range(10000):
            rnd = randint(0, len(int_list))
            wrapped = wrapper(binarySearch, int_list, rnd)
            lst.append(timeit.timeit(wrapped, number=1))
        avg = sum(lst)/len(lst)
        print('Binary search: avg= %s    max= %s' % (avg, max(lst)))

        lst = []
        for i in range(10000):
            rnd = randint(0, len(int_list))
            wrapped = wrapper(interpolationSearch, int_list, rnd)
            lst.append(timeit.timeit(wrapped, number=1))
        avg = sum(lst) / len(lst)
        print('Interpolatiton search: avg= %s    max= %s' % (avg, max(lst)))

        lst = []
        for i in range(10000):
            rnd = randint(0, len(int_list))
            wrapped = wrapper(rbTree.findNode, rnd)
            lst.append(timeit.timeit(wrapped, number=1))
        avg = sum(lst) / len(lst)
        print('Red-black tree search: avg= %s    max= %s' % (avg, max(lst)))

        lst = []
        for i in range(10000):
            rnd = randint(0, len(int_list))
            wrapped = wrapper(linearSearch, int_list, rnd)
            lst.append(timeit.timeit(wrapped, number=1))
        avg = sum(lst) / len(lst)
        print('Linear search: avg= %s    max= %s' % (avg, max(lst)))

    if option == '4':

        dtTree = DTTree()  # creation of digital trie tree from file
        with open('C:/Users/DX/Desktop/gotta do/data structures/words.txt', 'r') as file:  #
            for line in file.readlines():  #
                line = line.strip()  #
                dtTree.insert(line)  #

        while option != 'exit':
            option = input('What would you like to do?(type \'exit\' to go back to the main program)\n'
                           '1: Search for a word\n2: Insert a new word\n3: Delete a word\n')
            if option == '1':
                word = input('What to search for?\n')
                print(dtTree.search(word))
            elif option == '2':
                word = input('What to insert?\n')
                dtTree.insert(word)
                print('\nInserted successfully!\n')
            elif option == '3':
                word = input('What to delete?\n')
                dtTree.delete(word)
                print('\nDeleted successfully!\n')
        #treeX.inspect()  # this is just to help in debugging




