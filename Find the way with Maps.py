#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Write a Python program to triple all numbers of a given list of integers. Use Python map.

list_of_integers = (1, 2, 3, 4, 5, 6, 7) 
result = map(lambda x: x*3, list_of_integers) 
print("Triple of all numbers in a given list of integers:")
print(list(result))


# In[ ]:




