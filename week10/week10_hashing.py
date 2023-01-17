import math

class Hashtable:
    def __init__(self):
        self.table = [[] for i in range(26)]

    def insert_list(self, l):
        for ele in l:
            key = (ord(ele[0]) - 97) % 26
            self.table[key].append(ele)

    def print_table(self):
        return print(*self.table, sep='\n')

    def spell_check(self):
        word = input('Enter your word : ')
        if self.find_in_table(word) :
            return print(f"\"{word}\" is correctly spelled")
        else:
            return print(f"\"{word}\" is not in the dictionary")

    def find_in_table(self, word):
        key = (ord(word[0]) - 97) % 26
        return word in self.table[key]


def hash(str):
    h = 0
    for ch in str:
        h *= 37
        h += ord(ch)
    return h


file = "small.txt"
#file = "full.txt"
dic = []
with open(file) as f:
    for word in f.read().split():
        dic.append(word)

n = len(dic)
table_size = math.floor(0.2 * n)
print(n)
print(table_size)

#table = Hashtable()
#table.insert_list(dic)
#table.print_table()
#table.spell_check()

print(hash('about'))