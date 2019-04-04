class Heap:
  def __init__(self, comparator):
    self.storage = []
    self.comparator = comparator

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    removed_item = self.storage[0]
    del self.storage[0]
    self._sift_down(0)
    return removed_item

  def get_priority(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    parent = (index - 1) // 2
    if index <= 0:
      return
    elif self.storage[index] > self.storage[parent]:
      self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
      self._bubble_up(parent)
  
  def _sift_down(self, index):
     while index * 2 + 1 <= len(self.storage) - 1:
      if index * 2 + 2 > len(self.storage) - 1:
        maxSize = index * 2 + 1
      elif self.storage[index * 2 + 1] > self.storage[index * 2 + 2]:
        maxSize = index * 2 + 1
      else:
        maxSize = index * 2 + 2
      if self.storage[maxSize] > self.storage[index]:
        self.storage[maxSize], self.storage[index] = self.storage[index], self.storage[maxSize]
      index = maxSize