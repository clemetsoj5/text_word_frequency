
from tkinter.filedialog import *
import re
from itertools import islice

def open_and_read_file():
    # Have user select file to open
    path = askopenfilename()
    # Open the file and remove all the line endings as well as any non alpha numeric characters
    # besides space characters
    with open(path, 'r') as file:
        data = file.read().replace('\n', '')
        data = re.sub(r'[^a-zA-Z0-9\s]', '', data)
    # return the full text as a complete string
    return(data)

def split_text_into_words(data):
    # Converting complete string into list of words
    word_list = data.split(' ')
    word_counts = {}
    # Looping through each word and keeping track of frequency
    for word in word_list:
        if(word in word_counts):
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return(word_counts)

def find_top_ten(word_counts):
    # Sorting word list in descending order
    sorted_dict = {k: v for k, v in sorted(word_counts.items(), key=lambda item: item[1], reverse=True)}

    # Grabbing and retuning the top 10 most frequently used words. If less than 10 words, then return the entire dict
    if(len(sorted_dict) > 10):
        top_ten = dict(islice(sorted_dict.items(), 10))
    else:
        top_ten = sorted_dict
    return(top_ten)

# Open file from user input and read text file
data = open_and_read_file()
# Grab all the word counts
word_counts = split_text_into_words(data)
# Find the top 10 items
top_word_counts = find_top_ten(word_counts)
print(top_word_counts)
