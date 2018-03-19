# Word counts in the Brown corpus
# Demo for conditional probability
#
import nltk
from nltk.corpus import brown

# number of words in the Brown corpus
brown_numwords = len(brown.words())

# number of word pairs in the Brown corpus
# word pairs = "bigrams"
brown_num_bigrams = len(list(nltk.bigrams(brown.words())))

# quick look at typical word pairs: via pre-given collocations function
brown_nltk = nltk.Text(brown.words())
brown_nltk.collocations()

# Now we look at one of those collocations in more detail:
# How likely is it that the next word will be "ago", 
# GIVEN THAT the word we just read was "years"?

# First we determine the 
# frequencies for "years" and "ago"
count_years = brown.words().count("years")
count_ago = brown.words().count("ago")

# Probability for "years": relative frequency
prob_years = count_years / brown_numwords

# Now we determine the frequency of "years ago"
count_years_ago = 0
for word1, word2 in nltk.bigrams(brown.words()):
    if word1 == "years" and word2 == "ago":
        count_years_ago += 1

# Again, we estimate the probability as relative frequency
prob_years_ago = count_years_ago / brown_num_bigrams

# now check the probability of "ago" given "years"
prob_years_ago / prob_years

# This will come out the same as when we compute: 
# out of all occurrences of "years _", what percentage is "years ago"?
count_years_something = 0
for word1, word2, in nltk.bigrams(brown.words()):
    if word1 == "years":
        count_years_something += 1

print(count_years_ago / count_years_something)