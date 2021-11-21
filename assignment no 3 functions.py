#!/usr/bin/env python
# coding: utf-8

# In[31]:


#sum
numbers =(8,2,0,3,7)
Sum=sum(numbers)
print(Sum)


# In[ ]:


# "1234ABCD"


# In[30]:


txt="1234abcd"[::-1]
print (txt)


# In[49]:


# sample string :'The quick Brow Fox'

def string():
    my_string='The quick Brow Fox'
    count=0
    count1=0
    for i in my_string:
        if i.isupper():
            count+=1
        if i.islower():
            count1+=1
    print(count)
    print(count1)
string()


# In[ ]:




