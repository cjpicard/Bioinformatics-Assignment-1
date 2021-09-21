#!/usr/bin/env python
# coding: utf-8

# In[28]:


import numpy as np
from random import random

def waiting_time(probability,pattern) :
    assert abs(sum(probability.values ())-1) < 0.01 , 'Probabilities do not add up to 1.'

    pattern_size = len(pattern)
    sequence =''

    #main loop
    '''
    First condition:
    used to generate sequence of at least 'pattern size'
    example: RYY
    pattern size = 3

    Second condition:
    checks if the last 'pattern size' (in our case 3) matches with our input pattern

'''
    while len(sequence) < pattern_size or sequence[-pattern_size:] != pattern :
        ran = random() #sampling a random number between 0 and 1
        p = 0
        for letter in probability:
            p += probability[letter]
            if ran<p:
                sequence += letter
                break
    #return length of generated sequence
    #print(sequence)
    return len(sequence)

'''
example:
sequences of purine (R) and pyrimidine (Y)
probability of drawing R - p
probability of drawing Y - q
or nucleotide bases
'''

probability = dict()
probability ['R']=0.5
probability ['Y']=0.5


pattern = "RR"

n = 10000

print("Generating sequences")
print("Number of sequences to generate: %d" % n)
waiting_times = [waiting_time(probability, pattern) for i in range(n)]
print("Average waiting time for %d sequences: %.f Pattern: %s" % (n, np.mean(waiting_times),pattern))


# In[29]:


import numpy as np
from random import random

def waiting_time(probability,pattern) :
    assert abs(sum(probability.values ())-1) < 0.01 , 'Probabilities do not add up to 1.'

    pattern_size = len(pattern)
    sequence =''

    #main loop
    '''
    First condition:
    used to generate sequence of at least 'pattern size'
    example: RYY
    pattern size = 3

    Second condition:
    checks if the last 'pattern size' (in our case 3) matches with our input pattern

'''
    while len(sequence) < pattern_size or sequence[-pattern_size:] != pattern :
        ran = random() #sampling a random number between 0 and 1
        p = 0
        for letter in probability:
            p += probability[letter]
            if ran<p:
                sequence += letter
                break
    #return length of generated sequence
    #print(sequence)
    return len(sequence)

'''
example:
sequences of purine (R) and pyrimidine (Y)
probability of drawing R - p
probability of drawing Y - q
or nucleotide bases
'''

probability = dict()
probability ['R']=0.5
probability ['Y']=0.5


pattern = "RY"

n = 10000

print("Generating sequences")
print("Number of sequences to generate: %d" % n)
waiting_times = [waiting_time(probability, pattern) for i in range(n)]
print("Average waiting time for %d sequences: %.f Pattern: %s" % (n, np.mean(waiting_times),pattern))


# In[31]:


import numpy as np
from random import random

def waiting_time(probability,pattern) :
    assert abs(sum(probability.values ())-1) < 0.01 , 'Probabilities do not add up to 1.'

    pattern_size = len(pattern)
    sequence =''

    #main loop
    '''
    First condition:
    used to generate sequence of at least 'pattern size'
    example: RYY
    pattern size = 3

    Second condition:
    checks if the last 'pattern size' (in our case 3) matches with our input pattern

'''
    while len(sequence) < pattern_size or sequence[-pattern_size:] != pattern :
        ran = random() #sampling a random number between 0 and 1
        p = 0
        for letter in probability:
            p += probability[letter]
            if ran<p:
                sequence += letter
                break
    #return length of generated sequence
    #print(sequence)
    return len(sequence)

'''
example:
sequences of purine (R) and pyrimidine (Y)
probability of drawing R - p
probability of drawing Y - q
or nucleotide bases
'''

probability = dict()
probability ['R']=0.75
probability ['Y']=0.25


pattern = "RY"

n = 10000

print("Generating sequences")
print("Number of sequences to generate: %d" % n)
waiting_times = [waiting_time(probability, pattern) for i in range(n)]
print("Average waiting time for %d sequences: %.f Pattern: %s" % (n, np.mean(waiting_times),pattern))


# In[30]:


import numpy as np
from random import random

def waiting_time(probability,pattern) :
    assert abs(sum(probability.values ())-1) < 0.01 , 'Probabilities do not add up to 1.'

    pattern_size = len(pattern)
    sequence =''

    #main loop
    '''
    First condition:
    used to generate sequence of at least 'pattern size'
    example: RYY
    pattern size = 3

    Second condition:
    checks if the last 'pattern size' (in our case 3) matches with our input pattern

'''
    while len(sequence) < pattern_size or sequence[-pattern_size:] != pattern :
        ran = random() #sampling a random number between 0 and 1
        p = 0
        for letter in probability:
            p += probability[letter]
            if ran<p:
                sequence += letter
                break
    #return length of generated sequence
    #print(sequence)
    return len(sequence)

'''
example:
sequences of purine (R) and pyrimidine (Y)
probability of drawing R - p
probability of drawing Y - q
or nucleotide bases
'''

probability = dict()
probability ['R']=0.75
probability ['Y']=0.25


pattern = "RR"

n = 10000

print("Generating sequences")
print("Number of sequences to generate: %d" % n)
waiting_times = [waiting_time(probability, pattern) for i in range(n)]
print("Average waiting time for %d sequences: %.f Pattern: %s" % (n, np.mean(waiting_times),pattern))


# In[ ]:
