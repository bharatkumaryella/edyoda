#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Write a Python program to reverse a string.



# Sample String : "1234abcd"

# Expected Output : "dcba4321"

def sample_string_reverse(str):

    rstr = ''
    index = len(str)
    while index > 0:
        rstr += str[ index - 1 ]
        index = index - 1
    return rstr
print(sample_string_reverse('1234abcd'))


# In[ ]:




