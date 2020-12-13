# 周二总结

## 哈希表
1. 主要优点：能按key直接取value, O(1)
2. 考点： design a hashmap, collision resolution: 可以重新排位置，也可以使用链表
3. 一些小技巧：python里可以直接用Counter生成一个统计frequency的dict; tuple可以作为dict的key;collections.defaultdict()可以了解一下;dict.get(item, 0)可以在没找到item的情况下默认value为0

## 树，二叉树，二叉搜索树
1. 基本要点：前序，中序，后序，层次遍历(使用queue/deque)
2. 前中后序的迭代写法，可以使用stack辅助；递归写法，可以考虑traverse helper
3. 由二叉树推到N叉树的框架思想是类似的

## 堆，二叉堆
1. python里可以使用heapq
2. 特点：根节点(顶堆节点) : [0]
        索引为i的左孩子的索引为(2 * i + 1)
        索引为i的右孩子的索引为(2 * i + 2)
        索引为i的父节点的索引为(i - 1) / 2
        根据index可以找到对应的父子节点，有些题可以利用这个特点
3. 插入上浮，删除把最后一个元素提到堆顶然后下沉，与子节点比较，若均比两个子节点小，选择较大的子节点交换位置，以保证父节点比子节点大
4. Top k series
