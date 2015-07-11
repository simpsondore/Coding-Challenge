"""
run.py
Insight Data Coding Challenge
Sam Simpson Dore
07/05/15
Python 3.4.3
Mac OSX 10.10.4
Calculate the total number of times that each word has been tweeted and return
the median number of unique words per tweet
"""


# Word(s) to search for and interval of tweets (for graph)
word1 = "thermodynamic"
word2 = "thermodynamics"
interval = 30


# Import modules
import os.path
import fileinput
from collections import Counter
from collections import OrderedDict
import pickle


"""
Locate the parent directory and save as a string
Define the input and output file locations
"""
parent = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
inploc = os.path.join(parent, "tweet_input", "tweets.txt")
outloc1 = os.path.join(parent, "tweet_output", "ft1.txt")
outloc2 = os.path.join(parent, "tweet_output", "ft2.txt")


# Create an empty list and counter for use later
c = Counter()
unique_words = []
k = 1
word_tally = []
ap = 0


"""
Open the output file
Read the tweets.txt file line-by-line
Split each single-string tweet into individual strings for each tweet
Remove unwanted entities
Count the number of occurrences of each word in 'line' and store
Write the median number of new tweets to a file
Append new word counts to the previously defined counter
"""
f = open(outloc2, "w")
for line in fileinput.input([inploc]):
    line = line.replace("#","").replace("?","").replace(",","").replace("@","")\
          .replace(":","").replace(".","").split()
    line = [ x for x in line if "http" not in x ]
    count_k = Counter(line)
    unique_words.append(len(count_k))  
    f.write(str(format(float(sum(unique_words)/len(unique_words)), '.2f')) + "\n")
    c = c + count_k
    """
    Additional feature: store the number of occurrences of the selected word(s) in
    the chosen number of tweets
    """
    ap = ap + line.count(word1) + line.count(word2)
    if k % interval == 0:
        word_tally.append(ap)
        # Reset the 'ap' counter
        ap = 0
    k+=1
f.close()


# Save the counter datatype as an ordered dictionary. Sort by alphabetical order
odict = OrderedDict(sorted(c.items(), key=lambda x: x[0]))


# Find the length of the longest word for formatting
max_len = max(map(len, odict))


"""
Open the output file
Cycle through items in the ordered dictionary
Write the word (key), followed by the number of occurences (value) converted from an
integer to a string
"""
f = open(outloc1, "w")
for a, b in odict.items():
    f.write(a.ljust(max_len+4) + str(b) + "\n")
f.close()


"""
Use pickle to export outputs for post-processing
"""
outloc3 = os.path.join(parent, "tweet_output", "runpy_output.pkl")
f = open(outloc3, "wb")
pickle.dump(odict, f)
pickle.dump(word_tally, f)
pickle.dump(interval, f)
pickle.dump(word1, f)
pickle.dump(word2, f)
f.close()
