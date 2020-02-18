import sys
import os
import json
import math
from collections import Counter

class NBTrain:
    def train(self, data_directory_path):
        ham_list = []
        spam_list = []

        num_combined_emails = 0
        num_ham_emails = 0
        num_spam_emails = 0
        for directories, subdirs, files in os.walk(data_directory_path):
            if (os.path.split(directories)[1]  == 'ham'):
                for filename in files:      
                    with open(os.path.join(directories, filename), encoding="latin-1") as f:
                        num_combined_emails += 1
                        num_ham_emails += 1

                        print(num_combined_emails)
                        data = f.read().split()

                        for word in data:
                            ham_list.append(word)
            
            if (os.path.split(directories)[1]  == 'spam'):
                for filename in files:
                    with open(os.path.join(directories, filename), encoding="latin-1") as f:
                        num_combined_emails += 1
                        num_spam_emails += 1

                        print(num_combined_emails)
                        data = f.read().split()
                        for word in data:
                            spam_list.append(word)

        combined_words = ham_list + spam_list
        vocabulary_size = len(set(combined_words))

        num_ham_words = len(ham_list)
        num_spam_words = len(spam_list)

        ham_word_count = Counter(ham_list)
        spam_word_count = Counter(spam_list)
        combined_word_count = Counter(combined_words)

        probability_ham = math.log(num_ham_emails / num_combined_emails)
        probability_spam = math.log(num_spam_emails / num_combined_emails)

        ham_word_probabilities = {word: math.log((count + 1) / (num_ham_words + vocabulary_size)) \
                                    for word, count in ham_word_count.items()}
                                    
        spam_word_probabilities = {word: math.log((count + 1) / (num_spam_words + vocabulary_size)) \
                                    for word, count in spam_word_count.items()}

        probability_dict = {'probability_ham': probability_ham, 'probability_spam': probability_spam, \
                                'num_ham_words': num_ham_words, 'num_spam_words': num_spam_words, \
                                'vocab_size': vocabulary_size, 'ham_dict': ham_word_probabilities, \
                                    'spam_dict': spam_word_probabilities}

        with open('nbmodel.txt', 'w') as file:
            file.write(json.dumps(probability_dict))


if __name__ == '__main__':
    data_directory_path = sys.argv[1]
    nb_classifier = NBTrain()
    nb_classifier.train(data_directory_path)
