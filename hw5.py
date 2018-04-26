# -*- coding: utf-8 -*-
import csv
import json
import pickle
from collections import Counter
import string


def main(filename):
    lines = open(filename).readlines()

    all_words = []

    for line in lines:
        words = line.split()

        # check the format of words and append it to "all_words" list
        for word in words:
            # then, remove (strip) unwanted punctuations from every word
            # "dream." => "dream"
            for a in string.punctuation:
                word = word.strip(a)
                 
            # check if word is not empty
            if word:
                # append the word to "all_words" list
                all_words.append(word)

    # compute word count from all_words
    counter = Counter(all_words)

    # dump to a csv file named "wordcount.csv":
    # word,count
    # a,12345
    # I,23456
    # ...
    with open("wordcount.csv", "w", newline='') as csv_file:
        # create a csv writer from a file object (or descriptor)
        writer = csv.writer(csv_file)
        # write table head
        writer.writerow(['word', 'count'])
        # write all (word, count) pair into the csv writer
        writer.writerows(counter.most_common())

    # dump to a json file named "wordcount.json"
    with open("wordcount.json", "w") as json_file:
        writer = json.dump(counter.most_common(), json_file)

    # BONUS: dump to a pickle file named "wordcount.pkl"
    # hint: dump the Counter object directly
    with open("wordcount.pkl", "wb") as pkl_file:
        writer = pickle.dump(counter.most_common(), pkl_file)


if __name__ == '__main__':
    main("i_have_a_dream.txt")
