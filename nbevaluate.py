import sys
import os
import json
from collections import Counter

class NBEvaluate:
    def evaluate(self, file_name):
        with open(file_name, encoding="latin-1") as f:
            data = f.read().split('\n')

            correctly_classified_ham = 0
            correctly_classified_spam = 0
            classified_ham = 0
            classified_spam = 0
            actual_ham = 0
            actual_spam = 0

            for line in data:
                guessed_label, file_path = line.split('\t')

                if guessed_label == 'ham':
                    classified_ham += 1
                    if 'ham' in file_path:
                        correctly_classified_ham += 1
                        actual_ham += 1
                    elif 'spam' in file_path:
                        actual_spam += 1
                elif guessed_label == 'spam':
                    classified_spam += 1
                    if 'spam' in file_path:
                        correctly_classified_spam += 1
                        actual_spam += 1
                    elif 'ham' in file_path:
                        actual_ham += 1

            precision_ham = correctly_classified_ham / classified_ham
            precision_spam = correctly_classified_spam / classified_spam
            recall_ham = correctly_classified_ham / actual_ham
            recall_spam = correctly_classified_spam / actual_spam
            f1_score_ham = (2 * precision_ham * recall_ham) / (precision_ham + recall_ham)
            f1_score_spam = (2 * precision_spam * recall_spam) / (precision_spam + recall_spam)

            print('************************')
            print('Precision_ham: ', precision_ham)
            print('Recall_ham: ', recall_ham)
            print('F1_ham: ', f1_score_ham)
            print('************************')
            print('Precision_spam: ', precision_spam)
            print('Recall_spam: ', recall_spam)
            print('F1_spam: ', f1_score_spam)

if __name__ == '__main__':
    file_name = sys.argv[1]
    nb_classifier = NBEvaluate()
    nb_classifier.evaluate(file_name)
