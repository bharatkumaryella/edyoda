#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Write a Python program to count the number of even and odd numbers from a series of numbers.
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
count_odd = 0
count_even = 0
for i in numbers:
        if not i % 2:
            count_odd= count_odd+1
        else:
            count_even=count_even+1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)


# In[ ]:




