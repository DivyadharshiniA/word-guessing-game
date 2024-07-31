#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
words=['python','java','coding','designing','wireframing','prototyping']
word=random.choice(words)
guessed=False
attempt=0
while not guessed:
    guess=input("enter a word from words: ").lower()
    attempt+=1
    if not guess.isalpha():
        print("Please enter a valid word")
    elif guess not in(words):
        print("Enter a word only from words")
    elif guess==word:
        guessed=True
        print("Amazing! you are great")
    else:
        print("You are wrong")
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




