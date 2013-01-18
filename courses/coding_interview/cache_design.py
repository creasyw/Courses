# The cache infrustrature has two basic functions:
#       get(key), returning the value
#       set(key, value), set the value with certain key
# Besides, presuming that the cache only has limited length.
# So it should automatic throw away the "least frequent used" item.
#
# The most time efficient way is to maintain a hashmap which maps
# key to the node of a linkedlist containing the value of that key.
