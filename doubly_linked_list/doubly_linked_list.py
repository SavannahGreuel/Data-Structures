"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    new_node = ListNode(value)
    if self.head == None:
      new_node = ListNode(value)
      self.tail = new_node
      self.head = new_node
    else:
      self.head.insert_before(value)
      self.head = self.head.prev
    self.length = self.length + 1

  def remove_from_head(self):
    if self.head:
      new_head = self.head.next
      temp = self.head.value
      self.head.delete()
      self.length = self.length -1
      self.head = new_head
      if not self.head:
        self.tail = None
      return temp
    else:
      return None

  def add_to_tail(self, value):
    if self.tail:
      self.tail.insert_after(value)
      self.tail = self.tail.next
      self.length += 1
    else:
      self.tail = ListNode(value)
      self.head = self.tail
      self.length += 1
    

  def remove_from_tail(self):
    if self.tail:
      new_tail = self.tail.prev
      temp = self.tail.value
      self.tail.delete()
      self.length = self.length - 1
      self.tail = new_tail
      if not self.tail:
        self.head = None
      return temp
    else:
      return None

  def move_to_front(self, node):
    if node.prev:
      node.prev.next = node.next
    if node.next:
      node.next.prev = node.prev
    node.prev = None
    if self.head:
      self.head.prev = node
      node.next = self.head
      self.head = node
    else:
      self.head = node
      self.tail = node


  def move_to_end(self, node):
    self.add_to_tail(node.value)
    if self.head == node:
        self.head = self.head.next
    node.delete()
    self.length = self.length - 1

  def delete(self, node):
    if not self.head and not self.tail:
      return False

    if self.head == node:
      self.head = node.next
    if self.tail == node:
      self.tail = node.prev

    node.delete()
    self.length = self.length - 1

  def get_max(self):
    if not self.head:
      return None
    current_node = self.head
    greatest = current_node.value
    while current_node.next:
      current_node = current_node.next
      if current_node.value > greatest:
        greatest = current_node.value
    return greatest