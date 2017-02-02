class AVL_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class _AVL_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need.

    def __init__(self, value):
      self._value = value
      self._left = None
      self._right = None
      self._height = 0
      # TODO complete Node initialization

  def __init__(self):
    self._root = None
    # TODO complete initialization
    
  def _balance(self, node):
    if node._right is None and node._left is None:
      return node
    elif node._right is None and node._left._height == 1:
      return node
    elif node._left is None and node._right._height == 1:
      return node 
    elif node._right is None and node._left._height == 2:
      if node._left._right is None:
        node = self._rot_right(node)
        return node
      else:
        node = self._left_right(node)
        return node
    elif node._left is None and node._right._height == 2:
      if node._right._left is None:
        node = self._rot_left(node)
        return node
      else:
        node = self._right_left(node)
        return node
    else:
      return node
      
  def _rot_left(self, node):
    temp = self._AVL_Node(node._value)
    node = node._right
    if node._left is not None:
      temp._right = node._left 
    node._left = temp
    self._update_height(node._left)
    self._update_height(node)
    return node
  
  def _rot_right(self, node):
    temp = self._AVL_Node(node._value)
    node = node._left
    if node._right is not None:
      temp._left = node._right
    node._right = temp
    self._update_height(node._right)
    self._update_height(node)
    return node
  
  def _left_right(self, node):
    node._left = self._rot_left(node._left)
    return self._rot_right(node)
    
    
  def _right_left(self, node):
    node._right = self._rot_right(node._right)
    return self._rot_left(node)
    
    
  def _rinsert(self, new_value, next_node):
    if next_node is None:
      next_node = self._AVL_Node(new_value)
      self._update_height(next_node)
      return next_node
    if next_node._value == new_value:
      return next_node
    elif next_node._value > new_value:
      next_node._left = self._rinsert(new_value, next_node._left)
      self._update_height(next_node)
      next_node = self._balance(next_node)
      return next_node
    elif next_node._value < new_value:
      next_node._right = self._rinsert(new_value, next_node._right)
      self._update_height(next_node)
      next_node = self._balance(next_node)
      return next_node
      
    

  def insert_element(self, value):
    self._root = self._rinsert(value, self._root)
    
	
      
    # Insert the value specified into the tree, ensuring that
    # the tree remains balanced after the operation. Your solution
    # must be recursive. This will involve the introduction of
    # additional private methods.
    pass # TODO replace pass with your implementation

  def remove_element(self, value):
    # Remove the value specified from the tree, ensuring that
    # the tree remains balanced after the operation. Your solution
    # must be recursive. This will involve the introduction of
    # additional private methods.
    pass # TODO replace pass with your implementation


  def in_order_traversal(self, next_node):
    AVL_STR = ""
    if next_node is None:
      return AVL_STR
    
    if next_node._left is not None:
      AVL_STR += self.in_order_traversal(next_node._left)
       
    if len(AVL_STR) == 0:
      AVL_STR = AVL_STR + str(next_node._value)
      
    elif len(AVL_STR) != 0:
      AVL_STR = AVL_STR + ", " + str(next_node._value)
    
    if next_node._right is not None:
      AVL_STR += ", " + self.in_order_traversal(next_node._right)
      
    return AVL_STR
  
  def pre_order_traversal(self, next_node):
    AVL_STR = ""
    if next_node is None:
      return AVL_STR
    
    if len(AVL_STR) == 0:
      AVL_STR = AVL_STR + str(next_node._value)
      
    elif len(AVL_STR) != 0:
      AVL_STR = AVL_STR + ", " + str(next_node._value)    
    
    if next_node._left is not None:
      AVL_STR += ", " + self.pre_order_traversal(next_node._left)
    
    if next_node._right is not None:
      AVL_STR += ", " + self.pre_order_traversal(next_node._right)
      
    return AVL_STR
  
  def post_order_traversal(self, next_node):
    AVL_STR = ""
    if next_node is None:
      return AVL_STR   
    
    if next_node._left is not None:
      if len(AVL_STR) == 0:
        AVL_STR += self.post_order_traversal(next_node._left)
      else:
        AVL_STR += ", " + self.post_order_traversal(next_node._left)
    
    if next_node._right is not None:
      if len(AVL_STR) == 0:
        AVL_STR += self.post_order_traversal(next_node._right)
      else:
        AVL_STR += ", " + self.post_order_traversal(next_node._right)
            
    if len(AVL_STR) == 0:
      AVL_STR = AVL_STR + str(next_node._value)
      
    elif len(AVL_STR) != 0:
      AVL_STR = AVL_STR + ", " + str(next_node._value)
      
    return AVL_STR    
      
      
  def in_order(self):
    AVL_STR = self.in_order_traversal(self._root)
    AVL_STR = "[ " + str(AVL_STR) + " ]"
    return AVL_STR
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # TODO replace pass with your implementation

  def pre_order(self):
    AVL_STR = self.pre_order_traversal(self._root)
    AVL_STR = "[ " + str(AVL_STR) + " ]" 
    return AVL_STR
    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # TODO replace pass with your implementation

  def post_order(self):
    AVL_STR = self.post_order_traversal(self._root)
    AVL_STR = "[ " + str(AVL_STR) + " ]" 
    return AVL_STR    
    # Construct and return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # TODO replace pass with your implementation
  
  def _update_height(self, node):
    if node._left is None and node._right is None:
      node._height = 1
    elif node._left is None and node._right is not None:
      node._height = node._right._height + 1
    elif node._left is not None and node._right is None:
      node._height = node._left._height + 1
    else:
      node._height = max(node._left._height, node._right._height) + 1
      
    return node

  def get_height(self):
    if self._root is None:
      return 0
    else:
      return self._root._height

  def __str__(self):
    return self.in_order()


if __name__ == "__main__":
  
 
 #1. Inserting a root
  AVL = AVL_Tree()
  AVL.insert_element(1)
  print('1. Expected: [ 1 ]')
  print('   Actual  :', AVL, '\n')
 
 #2. Inserting to the left of the root
  AVL = AVL_Tree()
  AVL.insert_element(5)
  AVL.insert_element(1)
  print('2. Expected: [ 1, 5 ]')
  print('   Actual  :', AVL, '\n') 
 
 #3. Inserting to the right of the root
  AVL = AVL_Tree()
  AVL.insert_element(1)
  AVL.insert_element(2)
  print('3. Expected: [ 1, 2 ]')
  print('   Actual  :', AVL, '\n') 
 
 #4. Inserting to the right of the left child
  AVL = AVL_Tree()
  AVL.insert_element(5)
  AVL.insert_element(2)
  AVL.insert_element(3)
  print('4. Expected: [ 2, 3, 5 ]')
  print('   Actual  :', AVL, '\n')  
 
 #5. Inserting to the left of the left child
  AVL1 = AVL_Tree()
  AVL1.insert_element(7)
  AVL1.insert_element(5)
  AVL1.insert_element(2)
  print('5. Expected: [ 2, 5, 7 ]')
  print('   Actual  :', AVL1, '\n')   
 
 #6. Inserting to the left of the right child
  AVL1 = AVL_Tree()
  AVL1.insert_element(7)
  AVL1.insert_element(9)
  AVL1.insert_element(8)
  print('6. Expected: [ 7, 8, 9 ]')
  print('   Actual  :', AVL1, '\n') 

 #7. Inserting to the right of the right child
  AVL1 = AVL_Tree()
  AVL1.insert_element(7)
  AVL1.insert_element(9)
  AVL1.insert_element(10)
  print('7. Expected: [ 7, 9, 10 ]')
  print('   Actual  :', AVL1, '\n')

 #8. Check height of empty tree
  AVL = AVL_Tree()
  print('8. Expected: 0')
  print('   Actual  :', AVL.get_height(), '\n')   
 
 #9. Check height of 1 node tree
  AVL = AVL_Tree()
  AVL.insert_element(5)
  print('9. Expected: 1')
  print('   Actual  :', AVL.get_height(), '\n')    
 
 #10. Check height after insertion to the left of the root
  AVL = AVL_Tree()
  AVL.insert_element(5)
  AVL.insert_element(2)
  print('10. Expected: 2')
  print('    Actual  :', AVL.get_height(), '\n')   
 
 #11. Check height after insertion to the right of the root
  AVL = AVL_Tree()
  AVL.insert_element(5)
  AVL.insert_element(9)
  print('11. Expected: 2')
  print('    Actual  :', AVL.get_height(), '\n')   
  
 #12. Does inserting an equal value pass
  AVL = AVL_Tree()
  AVL.insert_element(5)
  AVL.insert_element(9)
  AVL.insert_element(5)
  print('12. Expected: [ 5, 9 ]')
  print('    Actual  :', AVL,  '\n')  
 
 #13. Does height stay the same when a node is inserted onto an existing level
  AVL = AVL_Tree()
  AVL.insert_element(5)
  AVL.insert_element(2)
  AVL.insert_element(7)
  print('13. Expected: 2')
  print('    Actual  :', AVL.get_height(), '\n')   
 
 #14. Remove from an empty tree
  AVL = AVL_Tree()
  print('14. Expected: None')
  print('    Actual  :', AVL.remove_element(5), '\n')

 #15. Remove from a 1 node tree
  AVL = AVL_Tree()
  AVL.insert_element(5)
  print('15. Original', AVL, '\n')
  AVL.remove_element(5)
  print('    Expected: None')
  print('    Actual  :', AVL, '\n')    

 #16. Remove a left child
  AVL = AVL_Tree()
  AVL.insert_element(5)
  AVL.insert_element(4)
  print('16. Original', AVL, '\n')
  AVL.remove_element(4)
  print('    Expected: None')
  print('    Actual  :', AVL, '\n') 
 
 #17. Remove a right child
  AVL = AVL_Tree()
  AVL.insert_element(5)
  AVL.insert_element(99)
  print('17. Original', AVL, '\n')
  AVL.remove_element(99)
  print('    Expected: None')
  print('    Actual  :', AVL, '\n') 
 
 #18. Remove the root of a right subtree
  AVL = AVL_Tree()
  AVL.insert_element(5)
  AVL.insert_element(4)
  AVL.insert_element(99)
  AVL.insert_element(98)
  AVL.insert_element(100)
  print('18. Original', AVL, '\n')
  AVL.remove_element(99)
  print('    Expected: None')
  print('    Actual  :', AVL, '\n') 
 
 #19. Remove the root of a left subtree
  AVL = AVL_Tree()
  AVL.insert_element(6)
  AVL.insert_element(4)
  AVL.insert_element(99)
  AVL.insert_element(3)
  AVL.insert_element(5)
  print('19. Original', AVL, '\n')
  AVL.remove_element(4)
  print('    Expected: None')
  print('    Actual  :', AVL, '\n')  
 
 #20. Remove the root of the tree
  AVL = AVL_Tree()
  AVL.insert_element(6)
  AVL.insert_element(4)
  AVL.insert_element(99)
  AVL.insert_element(3)
  AVL.insert_element(5)
  print('20. Original', AVL, '\n')
  AVL.remove_element(6)
  print('    Expected: None')
  print('    Actual  :', AVL, '\n')  
 
 #21. Does removing decrement height correctly
  AVL = AVL_Tree()
  AVL.insert_element(6)
  AVL.insert_element(4)
  print('21. Original', AVL.get_height(), '\n')
  AVL.remove_element(4)
  print('    Expected: None')
  print('    Actual  :', AVL.get_height(), '\n')  
 
 #22. Does height stay the same if a leaf of a full tree is removed
  AVL = AVL_Tree()
  AVL.insert_element(99)
  AVL.insert_element(150)
  AVL.insert_element(80)
  AVL.insert_element(75)
  AVL.insert_element(90)
  AVL.insert_element(120)
  AVL.insert_element(170)
  print('22. Original', AVL.get_height(), '\n')
  AVL.remove_element(170)
  print('    Expected: None')
  print('    Actual  :', AVL.get_height(), '\n')    
  
 #23. Does pre-order work
  AVL = AVL_Tree()
  AVL.insert_element(5)
  AVL.insert_element(2)
  AVL.insert_element(7)
  print('23. Expected: [ 5, 2, 7]')
  print('    Actual  :', AVL.pre_order(), '\n')
 
 #24. Does pre-order work on a larger tree
  AVL = AVL_Tree()
  AVL.insert_element(30)
  AVL.insert_element(40)
  AVL.insert_element(15)
  AVL.insert_element(25)
  AVL.insert_element(90)
  AVL.insert_element(80)
  AVL.insert_element(70)
  AVL.insert_element(85)
  AVL.insert_element(15)
  AVL.insert_element(72)
  print('24. Expected: [ 30, 15, 25, 80, 70, 40, 72, 90, 85 ] ')
  print('    Actual  :', AVL.pre_order(), '\n') 

 #25. Does post-order work
  AVL = AVL_Tree()
  AVL.insert_element(5)
  AVL.insert_element(2)
  AVL.insert_element(7)
  print('25. Expected: [ 2, 7, 5 ]')
  print('    Actual  :', AVL.post_order(), '\n')
 
 #26. Does post-order work on a larger tree
  AVL = AVL_Tree()
  AVL.insert_element(30)
  AVL.insert_element(40)
  AVL.insert_element(15)
  AVL.insert_element(25)
  AVL.insert_element(90)
  AVL.insert_element(80)
  AVL.insert_element(70)
  AVL.insert_element(85)
  AVL.insert_element(15)
  AVL.insert_element(72)
  print('26. Expected: [ 25, 15, 40, 72, 70, 85, 90, 80, 30 ]  ')
  print('    Actual  :', AVL.post_order(), '\n')  
 
 #27. Does in-order work on a larger tree
  AVL = AVL_Tree()
  AVL.insert_element(30)
  AVL.insert_element(40)
  AVL.insert_element(15)
  AVL.insert_element(25)
  AVL.insert_element(90)
  AVL.insert_element(80)
  AVL.insert_element(70)
  AVL.insert_element(85)
  AVL.insert_element(15)
  AVL.insert_element(72)
  print('27. Expected: [ 15, 25, 30, 40, 70, 72, 80, 85, 90 ] ')
  print('    Actual  :', AVL, '\n')  