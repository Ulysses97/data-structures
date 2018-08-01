import time

class Node :
  def __init__(self, data) :
    self.data = data
    self.next = None

class LinkedList :
  def __init__(self) :
    self.first = None
    self.last = None

    self.insertionTime = []
    self.searchTime = []

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

  def getAvgInsertionTime(self) :
    if len(self.insertionTime) == 0 :
      return 0

    else :
      return format(sum(self.insertionTime) / float(len(self.insertionTime)),'.10f')

  def insert(self, data) :
    start = time.time()

    if self.first is None :
      self.first = Node(data)
      self.last = self.first

      self.insertionTime.append(time.time() - start)

    else :
      self.last.next = Node(data)
      self.last = self.last.next

      self.insertionTime.append(time.time() - start)

  def getAvgSearchTime(self) :
    if len(self.searchTime) == 0 :
      return 0

    else : 
      return format(sum(self.searchTime) / float(len(self.searchTime)),'.10f')

  def find(self, data) :
    start = time.time()

    if self.first is not None :
      temp = self.first

      while True :
        if temp.data == data :
          self.searchTime.append(time.time() - start)
          return temp

        else :
          if temp is self.last :
            return None

          else :
            temp = temp.next
