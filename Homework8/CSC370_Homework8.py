#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random

 
def name_generator(ln):
    c = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijk"
    name = ""
    i = 0
    while (i < ln):
        name += c[random.randint(0,len(c)-1)]
        i +=1
    return name

def main():
    people = {}
    for i in range(100):
        people[name_generator(3)]= random.randint(0,99)
    for name in people:
        print(name, people[name])
     
main()


# In[ ]:




