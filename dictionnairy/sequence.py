#Import library
import json
# This is a python library for 'Text Processing Serveices', as the offcial site suggests.
import difflib
from difflib import SequenceMatcher, get_close_matches

#Let's load the same data again
data = json.load(open("data.json"))

#Run a Sequence Matcher
#First parameter is 'Junk' which includes white spaces, blank lines and so onself.
#Second and third parameters are the words you want to find similarities in-between.
#Ratio is used to find how close those two words are in numerical terms
value = SequenceMatcher(None, "rainn", "rain").ratio()

#Print out the value
print(value)


output = get_close_matches("rain", data.keys(), n=1, cutoff=0.75)

# Print out output, any guesses?
print(output)