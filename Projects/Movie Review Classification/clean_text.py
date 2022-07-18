#!/usr/bin/env python
# coding: utf-8

# ## Create NLP Pipeline to 'Clean' Reviews Data
# - Load Input File and Read Reviews
# - Tokenize
# - Remove Stopwords
# - Perform Stemming
# - While cleaned data to output file

# In[1]:


sample_text = """I loved this movie since I was 7 and I saw it on the opening day. It was so touching and beautiful. I strongly recommend seeing for all. It's a movie to watch with your family by far.<br /><br />My MPAA rating: PG-13 for thematic elements, prolonged scenes of disastor, nudity/sexuality and some language."""


# ### NLTK

# In[2]:


from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords


# In[3]:


# Init objects
tokenizer = RegexpTokenizer(r'\w+')
en_stopwords = set(stopwords.words('english'))
ps = PorterStemmer()


# In[6]:


def getCleanReview(review):
    
    review = review.lower()
    review = review.replace("<br /><br />"," ")
    
    #Tokenize
    tokens = tokenizer.tokenize(review)
    new_tokens = [token for token in tokens if token not in en_stopwords]
    stemmed_tokens = [ps.stem(token) for token in new_tokens]
    
    cleaned_review = ' '.join(stemmed_tokens)
    
    return cleaned_review


# In[7]:


# getStemmedReview(sample_text)


# In[ ]:




