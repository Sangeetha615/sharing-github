# -*- coding: utf-8 -*-
"""
Created on Mon May 18 11:52:10 2020

@author: ELCOT
"""


toy_text = """ Elephants are large mammals of the family Elephantidae and 
the order Proboscidea. Two species are traditionally recognised, 
the African elephant and the Asian elephant. Elephants are scattered 
throughout sub-Saharan Africa, South Asia, and Southeast Asia. 
Male African elephants are the largest extant terrestrial animals.
 All elephants have a long trunk used for many purposes, particularly breathing, 
 lifting water and grasping objects. Their incisors grow into tusks, 
 which can serve as weapons and as tools for moving objects and digging. 
 Elephants' large ear flaps help to control their body temperature. 
 Their pillar-like legs can carry their great weight. 
 African elephants have larger ears and concave backs while Asian elephants 
 have smaller ears and convex or level backs.  """



from gensim.summarization import summarize, keywords

def text_summarization_gensim(text, summary_ratio=0.5):
    summary = summarize(text, split=True, ratio=summary_ratio)
    
    for sentence in summary:
        print (sentence)
   

text_summarization_gensim(toy_text)