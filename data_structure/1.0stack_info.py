# Define

# A stack  is a linear data structure that follows the LIFO (Last In, First Out)
# principle, meaning the last element added is the first one to be removed.
# Imagine a stack of plates: you can only add or remove plates from the top.

# /-------

# .Key Operations:
#   Push : Adds an element to the top of the stack.
#   Pop : Removes the top element from the stack.
#   Peek/Top : Returns the top element without removing it.
#   IsEmpty : Checks if the stack is empty.

# /------------------

# .Applications:
# Managing function calls/recursion in programming.
# Undo/redo features in software (e.g., editing text).
# Parsing expressions (e.g., balancing parentheses).
# Memory management in operating systems.


# /---------

# > Implementation:
# Arrays : Fixed size, efficient for small stacks.
# Linked Lists : Dynamic size, efficient for large stacks.


# > Time Complexity:
# Push, Pop, Peek : O(1) (constant time).


# Common Issues:
# Stack Overflow : Occurs if too many elements are pushed (e.g., infinite recursion).
# Stack Underflow : Happens when trying to pop an empty stack.
