#!/usr/bin/env python
# coding: utf-8

# In[113]:


import collections

def dirsort(dirs): #Dirsort functions
    sorted_dirs = [] #Declaring empty list
    dict = collections.defaultdict(list) 
    for i in range(len(dirs)):
        dict[dirs[i].count('/')].append(dirs[i])

    for key in sorted(dict.keys()):
        dict.get(key).sort()
        for j in dict.get(key): 
            sorted_dirs.append(j)
    return sorted_dirs #Returns sorted directory

def user_inputs(): #function to give inputs
    dir_names = [
        ["/", "/usr/", "/usr/local/", "/usr/local/bin/", "/games/", "/games/snake/", "/homework/ ", "/temp/downloads/"],
        ["/usr/", "/usr/local/", "/bin/", "/usr/local/bin/", "/usr/bin/", "/bin/local/", "/bin/local/"], 
        ["/", "/a/", "/b/", "/c/", "/d/", "/e/", "/f/", "/g/"],
        ["/", "/a/", "/b/", "/c/", "/d/", "/e/", "/f/", "/g/", "/a/a/", "/b/g/c/", "/g/f/"],
        ["/a/b/c/d/e/f/g/h/i/j/k/l/m/n/", "/o/p/q/r/s/t/u/v/w/x/y/z/"],
        ["/a/b/", "/ab/cd/", "/c/d/", "/a/b/c/", "/ab/c/d/", "/a/bc/d/", "/a/b/cd/"]]

    for i in range(len(dir_names)):
        print(dir_names[i])
        print(dirsort(dir_names[i])) #Calling the disort function and passing it through each of the inputs
        print()


user_inputs() #Calling user_input function 


# In[ ]:




