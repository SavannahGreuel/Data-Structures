class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # adds the input value to the binary search tree, adhering to the rules of the ordering of elements in a binary search tree.
    root = self
    given = value
    complete = False
    while not complete:
      if given < root.value:
        if root.left:
          root = root.left
        else:
          root.left = BinarySearchTree(given)
          complete = True

      if given > root.value:
        if root.right:
          root = root.right
        else:
          root.right = BinarySearchTree(given)
          complete = True

  def contains(self, target):
    #searches the binary search tree for the input value, returning a boolean indicating whether the value exists in the tree or not.
    root = self
    complete= False
    while not complete:
      if not root:
        return False
      if root.value == target:
        return True
      elif root.value < target:
        root = root.right
      else:
        root = root.left

  def get_max(self):
    #  returns max val in bst
    current = self
    max = 0
    
    while current:
      if current.value > max:
        max = current.value
        current = current.right
    return max
    

  def for_each(self, cb):
    cb(self.value)
    if self.left != None:
      self.left.for_each(cb)
    if self.right != None:
      self.right.for_each(cb)