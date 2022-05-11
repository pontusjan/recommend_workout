#BST to store movement names and to efficiently search the movements with a depth first search
class BinarySearchTree:
  def __init__(self, value, depth=1):
    self.value = value
    self.depth = depth
    self.left = None
    self.right = None

  def insert(self, value):
    if (value < self.value):
      if (self.left is None):
        self.left = BinarySearchTree(value, self.depth + 1)
      else:
        self.left.insert(value)
    else:
      if (self.right is None):
        self.right = BinarySearchTree(value, self.depth + 1)
      else:
        self.right.insert(value)

  #Depth first search, returning a list of all options beginning with the entered value
  def autocomplete_depth_first(self, value):
    lst = []
    if (self.left is not None) and (self.value[:len(value)] >= value):
      lst += self.left.autocomplete_depth_first(value)
    if self.value[:len(value)] == value:
      lst.append(self.value)
    if (self.right is not None) and (self.value[:len(value)] <= value):
      lst += self.right.autocomplete_depth_first(value)
    return lst


