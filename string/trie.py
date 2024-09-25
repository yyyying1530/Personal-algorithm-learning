# 字典树基础
# 基于力扣 2416

class TrieNode:
    def __init__(self):
        self.node = dict()
        self.times = 0
    
    def insert(self, s):
        curr = self
        for i in s:
            if i not in curr.node:
                curr.node[i] = TrieNode()
            curr = curr.node[i]
            curr.times += 1
    
    def search(self, s):
        curr = self
        result = 0
        for i in s:
            if i not in curr.node:
                return result
            curr = curr.node[i]
            result += curr.times
        return result