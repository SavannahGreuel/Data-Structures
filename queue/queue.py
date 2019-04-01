class Queue:
  def __init__(self):
    self.size = 0
    # start here
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    # add item into queue
    self.storage.append(item)
    self.size += 1
  
  def dequeue(self):
    if self.size == 0:
      return None

    else:
      self.size -= 1
      return self.storage.pop(0)

  def len(self):
    self.size = len(self.storage)
    return self.size
    
