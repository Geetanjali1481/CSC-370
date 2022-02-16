#!/usr/bin/env python
# coding: utf-8

# In[22]:


def DrawTree(nodes, names):
    for i in nodes:
        if i == -1:
            a = nodes.index(i)
            print("+-",names[a])
            
    for j in range(len(nodes)-1):
        if nodes[j] == a:
            print("\t+-",names[j])
            for r in range(len(nodes)):
                if nodes[r] == j:
                    print("\t\t+-",names[r])
                    
                    for q in range(len(nodes)):
                        if nodes[q] == r:
                            print("\t\t\t+-",names[q])
                            
                            for p in range(len(nodes)):
                                if nodes[p] == q:
                                    print("\t\t\t\t+-",names[p])
                                    
                                    for s in range(len(nodes)):
                                        if nodes[s] == p:
                                            print("\t\t\t\t\t+-",names[s])
                                            
                                            for t in range(len(nodes)):
                                                if nodes[t] == s:
                                                    print("\t\t\t\t\t\t+-",names[t])
                                                    
DrawTree([-1,0,1,1,0,0,5,5], ["Root","SubB","LEAF1","LEAF2","LEAF3","SubA","LEAF4","LEAF5"])
print("\n")
DrawTree([1,2,3,4,5,6,-1], ["A","B","C","D","E","F","G"])
print("\n")
DrawTree([1,2,3,4,6,6,-1], ["A","B","C","D","E","F","G"])
print("\n")
DrawTree([6,2,3,4,5,6,-1], ["A","B","C","D","E","F","G"])
print("\n")
DrawTree([-1,0,1,1,2,2,3,3,0,8,8,9,9,10,10], ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"])
    
    

