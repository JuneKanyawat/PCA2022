import math
from week8_UnorderedList import Node, UnorderedList

class Hashtable:
    expansions = 0
    collisions = 0
    load_factor = 0
    similar = []

    def __init__(self, dic, approach):
        self.approach = approach
        self.dic = dic
        self.table = []
        self.linked_list = []
        self.create_table()
        if approach == "chaining":
            self.chaining(dic)
        elif approach == "linear probing":
            self.linear_probe(dic)

    def create_table(self):
        self.table = [[] for i in range(self.table_size())]
        self.linked_list = [UnorderedList() for i in range(len(self.table))]

    def chaining(self, l):
        #print("table size >>", self.table_size())
        for ele in l:
            key = self.hash(ele) % self.table_size()
            if ele not in self.table[key]:
                if self.table[key] != []:
                    self.collisions += 1
                self.table[key].append(ele)
                self.linked_list[key].add(ele)
            self.check_load_factor()
            if self.load_factor >= 0.5:
                #self.print_table()
                self.rehash()

    def linear_probe(self, l):
        #print("table size >>", self.table_size())
        for ele in l:
            next = False
            key = self.hash(ele) % self.table_size()
            for i in self.table:
                if ele in i:
                    next = True
            if not next:
                while self.table[key] != []:
                    key += 1
                    key = key % self.table_size()
                    self.collisions += 1
                self.table[key].append(ele)
                self.check_load_factor()
                if self.load_factor >= 0.5:
                    #self.print_table()
                    self.rehash()

    def hash(self, str):
        h = 0
        for ch in str:
            h *= 37
            h += ord(ch)
        return h

    def rehash(self):
        self.longest_chain = 0
        self.collisions = 0
        self.expansions += 1
        self.create_table()
        if self.approach == "chaining":
            self.chaining(dic)
        elif self.approach == "linear probing":
            self.linear_probe(dic)

    def check_load_factor(self):
        cnt = 0
        for i in self.table:
            if i != []:
                cnt += 1
        self.load_factor = cnt / self.table_size()
        return self.load_factor

    def print_table(self):
        if self.approach == "chaining":
            for i in range(len(self.linked_list)):
                self.linked_list[i].print()
        return print(*self.table, sep='\t')

    def spell_check(self):
        word = input('Enter your word : ')
        if self.find_in_table(word) :
            print(f"\"{word}\" is correctly spelled")
        else:
            print(f"\"{word}\" is not in the dictionary")
            if self.similar != []:
                print("Possible corrections are : ", end='')
                print(*self.similar, sep=' ')

    def find_in_table(self, word):
        for i in self.table:
            for j in i:
                if word == j:
                    return True
                if len(word) == len(j):
                    cnt = 0
                    for k in range(len(word)):
                       if j[k] == word[k]:
                           cnt += 1
                    if cnt == len(word) - 1:
                        self.similar.append(j)
        return False

    def table_size(self):
        n = len(self.dic)
        size = math.floor(n * 0.2) * (2 ** self.expansions)
        new_size = self.check_prime(size)
        return new_size

    def check_prime(self, n):
        if n < 2:
            return self.check_prime(n + 1)
        for i in range(2, n):
            if n % i == 0:
                return self.check_prime(n+1)
        return n

    def find_longest_chain(self):
        max = 0
        for i in self.table:
            if len(i) > max:
                max = len(i)
        return max

    def statistics(self):
        longest_chain = self.find_longest_chain()
        print(f"Collision resolution : [{self.approach}]")
        print(f"Total words : {len(self.dic)}")
        print(f"Table size : {self.table_size()}")
        print(f"{self.expansions} expansions, load factor {round(self.load_factor, 3)}, {self.collisions} collisions, longest chain {longest_chain}")

file = "small.txt"
#file = "full.txt"
#file = "dic.txt"
dic = []
with open(file) as f:
    for word in f.read().split():
        dic.append(word)

print('-'*70)
table1 = Hashtable(dic, "chaining")
#table1.print_table()
#print('-'*70)
table1.statistics()
print('-'*70)
table2 = Hashtable(dic, "linear probing")
#table2.print_table()
#print('-'*70)
table2.statistics()
print('-'*70)
table1.spell_check()
table2.spell_check()
