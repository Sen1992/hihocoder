# import datetime
# timestate = datetime.datetime.now()
import gc
import collections
gc.disable()
#期初的思路是将对象作为key，因此在节点的类里面实现了equal和hash两个函数,但发现这样的时间消耗太高，无法通过，故采用下面字典嵌套的方法
# class TrieNode:
#     def __init__(self,char,value=1):
#         self.char = char
#         self.count = value
#     def __hash__(self):
#         return hash(self.char)
#     def __eq__(self, other):
#         if self.char == other.char:
#             return True
#         else:
#             return False
#     # def get(self):
#     #     return self.char
#     # def __repr__(self):
#     #     return self.char
#
# class Trie:
#     def __init__(self):
#         self.trie={}
#     def add(self,word):
#         tree = self.trie
#         for char in word:
#             l = tree.keys()
#             tmp = TrieNode(char)
#             for i in xrange(len(l)):
#                 if tmp == l[i]:
#                     l[i].count+=1
#                     tree = tree[l[i]]
#                     break
#             else:
#                 char = TrieNode(char)
#                 tree[char]={}
#                 tree=tree[char]
#     def search(self,word):
#         tree = self.trie
#         times=0
#         for char in word:
#             l = tree.keys()
#             tmp = TrieNode(char)
#             for i in xrange(len(l)):
#                 if tmp==l[i]:
#                     times=l[i].count
#                     tree=tree[l[i]]
#                     break
#             else:
#                 print 0
#                 return
#         print times
'''
主要用于处理海量数据，统计出现最频繁的单词，以前根据前缀显示单词，通过共享前缀的方式节省空间和提升效率使用,
查找单词的时间复杂度为O(nlength),空间复杂度小于O(nlength),在建立树的过程中，我们使用count来记录每个字
符出现的次数
'''
class TrieNode:
    def __init__(self):
        self.nodes = collections.defaultdict(TrieNode)
        self.count = 1
        self.isword = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self,word):
        curr = self.root
        for char in word:
            if char in curr.nodes:
                curr.nodes[char].count+=1
            curr = curr.nodes[char]
        curr.isword = True

    def search(self,word):
        curr = self.root
        for char in word:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        return curr.isword

    def startWith(self,prefix):
        curr = self.root
        for char in prefix:
            if char not in curr.nodes:
                return 0
            curr = curr.nodes[char]
        return curr.count

trie = Trie()
while True:
    try:
        N = int(raw_input())
        for i in xrange(N):
            trie.add(raw_input())
        N = int(raw_input())
        for i in xrange(N):
            print trie.startWith(raw_input())
    except EOFError:
        gc.enable()
        break
