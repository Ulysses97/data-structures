import time

class Node :
  def __init__(self, data, key) :
    self.data = data
    self.key = key
    self.next = None

class LinkedList :
  def __init__(self) :
    self.first = None
    self.last = None

  def empty(self) :
    return self.first is None

  def getLast(self) :
    return self.last

  def pop(self) :
    if not self.empty() :
      temp = self.first

      if self.first is self.last :
        self.first = None
        self.last = None

      else :
        while True :
          if temp.next is self.last :
            last = self.last
            aux = temp.next
            temp.next = None
            aux = None
            self.last = temp
            return last

          else :
            temp = temp.next

  def insert(self, data, key) :
    if self.first is None :
      self.first = Node(data, key)
      self.last = self.first

    else :
      self.last.next = Node(data, key)
      self.last = self.last.next

class HashTable :
  def __init__(self, length) :
    self.table = list()

    for i in range(length) :
      self.table.append(LinkedList())

    self.insertionTime = []
    self.searchTime = []

  def getAvgInsertionTime(self) :
    if len(self.insertionTime) == 0 :
      return 0

    else :
      return format(sum(self.insertionTime) / float(len(self.insertionTime)),'.10f')

  def getAvgSearchTime(self) :
    if len(self.searchTime) == 0 :
      return 0

    else :
      return format(sum(self.searchTime) / float(len(self.searchTime)),'.10f')


  def hashFunction(self, key, length) :
    intKey = 0

    for char in key :
      intKey += ord(char)

    return intKey % length

  def insert(self, data, key) :
    start = time.time()

    index = self.hashFunction(key, len(self.table))
    self.table[index].insert(data, key)

    self.insertionTime.append(time.time() - start)

    if self.loadFactor() >= 0.75 :
      self.rehash()

  def loadFactor(self) :
    notEmptyRows = 0

    for row in self.table :
      if not row.empty() :
        notEmptyRows += 1

    return notEmptyRows / len(self.table)

  def rehash(self) :
    newTable = list()

    for i in range(2 * len(self.table)) :
      newTable.append(LinkedList())

    for row in self.table :
      while not row.empty() :
        node = row.getLast()
        index = self.hashFunction(node.key, len(newTable))
        newTable[index].insert(node.data, node.key)

    self.table = newTable

  def find(self, key) :
    start = time.time()
    index = self.hashFunction(key, len(self.table))
    row = self.table[index]

    while not row.empty() :
      if row.getLast().key == key :
        self.searchTime.append(time.time() - start)
        return row.getLast()

      else :
        row.pop()
