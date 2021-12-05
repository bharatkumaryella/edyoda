#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Write a Python program to square the elements of a list using map() function.

def sqr(num):
  return num * num
Sample_List= [4, 5, 2, 9]
print("Sample List: ",Sample_List)
result = map(sqr, nums)
print("Square the elements of the list using map():")
print(list(result))


# In[ ]:




