# 字典树
1. 应用于统计和排序大量的字符, 能最大限度地减少无谓的字符串比较，查询效率比哈希表高  
-> why? 空间换时间，利用字符串的公共前缀来降低查询时间的开销  
2. 基本操作： insert(s)、search(s)、searchPrefix(s)  
Python 模板：
```
# Python 
class Trie(object):
 
def __init__(self): 
  self.root = {} 
  self.end_of_word = "#" 

def insert(self, word): 
  node = self.root 
  for char in word: 
    node = node.setdefault(char, {}) 
    node[self.end_of_word] = self.end_of_word 

def search(self, word): 
  node = self.root 
  for char in word: 
    if char not in node: 
      return False 
    node = node[char] 
  return self.end_of_word in node 

def startsWith(self, prefix): 
  node = self.root 
  for char in prefix: 
    if char not in node: 
      return False 
    node = node[char] 
  return True

```
# 并查集
1. 适用场景：组团配对问题  
2. 基本操作：makeSet(s), unionSet(x, y), find(x)  
记一个Surrounded Regions的union find精妙解法方便理解：
```
class unionFind:
    def __init__(self, n):
        self.father = [i for i in range(n)]
    
    def find(self, x):
        if x == self.father[x]:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
    
    def connect(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.father[min(root_x, root_y)] = max(root_x, root_y)

class Solution:
    """
    @param: board: board a 2D board containing 'X' and 'O'
    @return: nothing
    """
    def surroundedRegions(self, board):
        # write your code here
        if board is None or len(board) == 0 or len(board[0]) == 0:
            return
        m, n = len(board), len(board[0])
        if m <= 2 or n <= 2:
            return
        total = m * n
        uf = unionFind(total + 1)
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        for x in range(m):
            for y in range(n):
                if board[x][y] == "X":
                    continue
                if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                    uf.connect(x * n + y, total)
                else:
                    for k in range(4):
                        newx = x + dx[k]
                        newy = y + dy[k]
                        if board[newx][newy] == "O":
                            uf.connect(x * n + y, newx * n + newy)
        for x in range(m):
            for y in range(n):
                if board[x][y] == "O" and uf.find(x * n + y) != total:
                    board[x][y] = "X"
```
# 高级搜索
搜索的优化方式：  
1. 不重复 (memo)
2. 剪枝
3. 双向bfs模板：
```
def dBFS(graph, start, end):
    visited = set()
    front = []
    back = []
    front.append(start)
    back.append(end)
    while front and back:
        nodes = set()
        for node in front:
            visited.add(node) # add to visited
            process(node) # process current node
            nodes.append(generate_related_nodes(node)) 
        front = nodes
        # 从较小的set开始
        if len(back) < len(front):
            front, back = back, front
    ...
        
```
不过，以word ladder 2 来看，也可以搞出另一个思路，先来一遍bfs再来一遍dfs
```
from collections import deque

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        dict.add(start)
        dict.add(end)
        distance = {}
        
        self.bfs(end, distance, dict)
        
        results = []
        self.dfs(start, end, distance, dict, [start], results)
        
        return results

    def bfs(self, start, distance, dict):
        distance[start] = 0
        queue = deque([start])
        while queue:
            word = queue.popleft()
            for next_word in self.get_next_words(word, dict):
                if next_word not in distance:
                    distance[next_word] = distance[word] + 1
                    queue.append(next_word)
    
    def get_next_words(self, word, dict):
        words = []
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i + 1:]
                if next_word != word and next_word in dict:
                    words.append(next_word)
        return words
                        
    def dfs(self, curt, target, distance, dict, path, results):
        if curt == target:
            results.append(list(path))
            return
        
        for word in self.get_next_words(curt, dict):
            if distance[word] != distance[curt] - 1:
                continue
            path.append(word)
            self.dfs(word, target, distance, dict, path, results)
            path.pop()
```
# AVL树和红黑树
## 面试可能考点
1. AVL树比红黑树查找速度快 -> 因为完全平衡
2. 红黑树比AVL树更快的插入和删除 -> 因为近似平衡  
3. AVL存放平衡因子（或高度信息）要求一个整型，而红黑树只需要一个1bit存放红黑信息  
4. 红黑树应用于C++的map, multimap, multiset, 而AVL树用于数据库 -> 因为对查询要求较高
