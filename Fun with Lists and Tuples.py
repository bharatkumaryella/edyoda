#!/usr/bin/env python
# coding: utf-8

# In[1]:


def last(n): return n[-1]
a=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
def sort_list_last(tuples):
  return sorted(tuples, key=last)

print(sort_list_last(a))


# In[ ]:




