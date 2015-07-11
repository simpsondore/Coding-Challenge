"""
post_processing.py
Insight Data Coding Challenge
Sam Simpson Dore
07/05/15
Python 3.4.3
Mac OSX 10.10.4
Create an output file detailing to the top 10 tweets called out.
"""


# Import modules
import os.path
import pickle
from collections import OrderedDict
import itertools
import matplotlib.pyplot as plt


"""
Locate the parent directory and save as a string
Define the input and output file locations
"""
parent = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
inploc = os.path.join(parent, "tweet_output", "runpy_output.pkl")
outloc1 = os.path.join(parent, "tweet_output", "ft3.txt")
outloc2 = os.path.join(parent, "tweet_output", "plot.png")

"""
Use the pickle module to import data from run.py
"""
f = open(inploc, "rb")
odict = pickle.load(f)
word_tally = pickle.load(f)
interval = pickle.load(f)
word1 = pickle.load(f)
word2 = pickle.load(f)
f.close()


"""
Re-order the dictionary 'odict' by values (i.e. word count)
Use itertools.islice to extract the 10 most frequently used words
Find the length of the longest word for formatting
Open the output file and write a title
Write the word (key), followed by the number of occurrences (value) converted
from an integer to a string
"""
odict = OrderedDict(sorted(odict.items(), key=lambda x: x[1], reverse = True))
top_10 = OrderedDict(itertools.islice(odict.items(), 0, 9))
max_len = max(map(len, odict))
f = open(outloc1, "w")
f.write("Top 10 Most Frequently Used Words:\n\n" + "Word".ljust(max_len+4) +\
        "Number of Occurrences" + "\n\n")
for a, b in top_10.items():
    f.write(a.ljust(max_len+4) + str(b) + "\n")
f.close()


"""
Use 'word_tally' to create a plot to visalize the occurrences of the selected
words.
"""
plt.plot(word_tally)
plt.ylabel("Number of Occurrences")
plt.xlabel("Every 30 Tweets")
plt.title("Number of occurrences of the words\n" + word1 + " and " + word2 +\
        " in every 30 tweets")
plt.axis([0, len(word_tally)-1, 0, max(word_tally)+4])
plt.savefig(outloc2, bbox_inches='tight')
