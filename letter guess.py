#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
words=['python','java','coding','designing','wireframing','prototyping']
word=random.choice(words)
guesses=[]
guessed=False
attempt=0
while not guessed:
    guess=input("enter a letter from words: ").lower()
    attempt+=1
    
    if len(guess)!=1 and not guess.isalpha():
        print("Enter a letter with length 1")
    elif guess in guesses:
        print("You have already guessed that letter")
    else:
        guesses.append(guess)
        
        if guess in word:
            print("Good guess")
        else:
            print("Wrong guesses")
        cp=''
        for letter in word:
            if letter in guesses:
                cp+=letter
            else:
                cp+='_'
        print("current progress: "+cp)
        if '_' not in cp:
            guessed=True
            print("successful! you guessed it")


# In[ ]:





# In[ ]:


g

