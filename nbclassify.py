import sys
import os
import json
import math
from collections import Counter

class NBClassify:
    def classify(self, data_directory_path):
        i = 0
        with open('nbmodel.txt') as file:
            model = json.loads(file.read())
            #print(model)
                        
            ham_dict = model['ham_dict']
            spam_dict = model['spam_dict']

        output_file = open('nboutput.txt', 'w')
        newline = ''
        for directories, subdirs, files in os.walk(data_directory_path):
            for filename in files:      
                with open(os.path.join(directories, filename), encoding="latin-1") as f:
                    probability_ham = model['probability_ham']
                    probability_spam = model['probability_spam']

                    i += 1
                    print(i)

                    data = f.read().split()
                    email_class = None
                    
                    for word in data:
                        if word not in ham_dict and word not in spam_dict:
                            continue
                        probability_ham += ham_dict.get(word, math.log(1 / (model['num_ham_words'] + model['vocab_size'])))
                        probability_spam += spam_dict.get(word, math.log(1 / (model['num_spam_words'] + model['vocab_size'])))
                    
                    if probability_ham > probability_spam:
                        email_class = 'ham'
                    else:
                        email_class = 'spam'

                    output_file.write(newline + email_class+'\t'+str(os.path.join(directories, filename)))
                    newline = '\n'

if __name__ == '__main__':
    data_directory_path = sys.argv[1]
    nb_classifier = NBClassify()
    nb_classifier.classify(data_directory_path)