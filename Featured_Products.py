
# coding: utf-8

# In[73]:


def featuredProduct(products):
    sorted_words=(sorted(products,reverse=True))
    print(sorted_words)
    max_count = max(sorted_words,key=sorted_words.count)    
    return max_count


# In[64]:


featuredProduct(['redShirt','greenPants','redShirt','orangeShoes','blackPants','blackPants'])


# In[65]:


featuredProduct(['yellowShirt','redHat','blackShirt','bluePants','redHat','pinkHat','blackShirt','yellowShirt','greenPants','greenPants'])


# In[66]:


featuredProduct(['greenShirt','bluePants','redShirt','blackShoes','redPants','redPants','whiteShirt','redShirt'])


# In[75]:


featuredProduct(['a'])

