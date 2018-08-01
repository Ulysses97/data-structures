import time

class Node :
  def __init__(self, data) :
    self.data = data
    self.left = None
    self.right = None

class BinaryTree :
  def __init__(self) :
    self.root = None

    self.insertionTime = []
    self.searchTime = []

  def printInOrder(self) :
    if self.root is not None :
      self._printInOrder(self.root)
  
  def _printInOrder(self, node) :
    if node is None :
      return
    
    else :
      self._printInOrder(node.left)
      print(node.data)
      self._printInOrder(node.right)

  def getAvgSearchTime(self) :
    if len(self.searchTime) == 0 :
      return 0

    else :
      return format(sum(self.searchTime) / float(len(self.searchTime)),'.10f')

  def getAvgInsertionTime(self) :
    if len(self.insertionTime) == 0 :
      return 0

    else :
      return format(sum(self.insertionTime) / float(len(self.insertionTime)),'.10f')

  def find(self, data) :
    start = time.time()

    if self.root is None :
      return None

    else :
      return self._find(data, self.root, start)

  def _find(self, data, node, startTime) :
    if node is not None :
      if node.data == data :
        self.searchTime.append(time.time() - startTime)
        return node

      else :
        if node.data > data :
          if node.left is None :
            return None

          else :
            return self._find(data, node.left, startTime)

        else :
          if node.right is None :
            return None

          else :
            return self._find(data, node.right, startTime)

  def insert(self, data) :
    start = time.time()

    if self.root is None :
      self.root = Node(data)
      self.insertionTime.append(time.time() - start)

    else :
      self._insert(data, self.root, start)

  def _insert(self, data, node, startTime) :
    if node.data > data :
      if node.left is None :
        node.left = Node(data)
        self.insertionTime.append(time.time() - startTime)

      else :
        self._insert(data, node.left, startTime)

    else :
      if node.right is None :
        node.right = Node(data)
        self.insertionTime.append(time.time() - startTime)

      else :
        self._insert(data, node.right, startTime)

    self.balanceTree(self.root, None)

  def treeDepth(self) :
    if self.root is None :
      return 0

    else :
      return self._treeDepth(self.root)

  def _treeDepth(self, node) :
    if node is None :
      return 0

    else :
      leftDepth = self._treeDepth(node.left)
      rightDepth = self._treeDepth(node.right)

      if leftDepth > rightDepth :
        return leftDepth + 1

      else :
        return rightDepth + 1

  def balanceFactor(self, node) :
    if node is None :
      return 0

    else :
      return self._treeDepth(node.right) - self._treeDepth(node.left)

  def isLeaf(self, node) :
    if node is not None :
      if node.left is None and node.right is None :
        return True

      else :
        return False

    else :
      return False

  def balanceTree(self, node, prevNode) :
    if node is None or self.isLeaf(node) :
      return
    
    else :
      if self.balanceFactor(node) < -1 : # Left sub-tree is unbalanced.
        if node.left.left is not None : # Right-Right rotation.
          aux = node
          node = node.left
          node.right = Node(aux.data)

          if aux is self.root :
            self.root = node
          
          else :
            prevNode.left = node

        else : # Left-Right rotation.
          aux = node.left
          node.left = node.left.right
          node.left.left = Node(aux.data)

          if node is self.root :
            self.root = node
          
          else :
            prevNode.left = node

          aux = node
          node = node.left
          node.right = Node(aux.data)

          if aux is self.root :
            self.root = node
          
          else :
            prevNode.left = node

      elif self.balanceFactor(node) > 1 : # Right sub-tree is unbalanced.
        if node.right.right is not None : # Left-Left rotation.
          aux = node
          node = node.right
          node.left = Node(aux.data)

          if aux is self.root :
            self.root = node
          
          else :
            prevNode.right = node

        else : # Right-Left rotation.
          aux = node.right
          node.right = node.right.left
          node.right.right = Node(aux.data)

          if node is self.root :
            self.root = node
          
          else :
            prevNode.right = node

          aux = node
          node = node.right
          node.left = Node(aux.data)

          if aux is self.root :
            self.root = node
          
          else :
            prevNode.right = node

      else :
        self.balanceTree(node.left, node)
        self.balanceTree(node.right, node)
