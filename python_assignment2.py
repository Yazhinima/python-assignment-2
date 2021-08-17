#!/usr/bin/env python
# coding: utf-8
Create the below pattern using nested for loop in Python.

*
**
***
****
*****
****
***
**
*


Write a Python program to reverse a word after accepting the input from the user.
Sample Output:
Input word: ineuron
Output: norueni
# In[51]:


b = ""
for i in range(1):
    for x in range(1,6):
        b = "*"*x
        print(b)
    for y in range(1,6,1):
        b=(len(b)-1)*"*"
        print(b)
       


# In[18]:


#method 1
word = input(str("enter the word : "))
i = -1
rev_word = ""
while i > -(len(word)+1):
    rev_word = rev_word+word[i]
    i = i-1
print(rev_word)


# In[3]:


#method 2
word_1 = input(str("enter the word : "))
print("reversed word is :", word_1[::-1])


# In[ ]:




