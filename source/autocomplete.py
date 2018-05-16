import random
import time

def get_words(filename):
    with open(filename, 'r') as file:
        words_list = file.read().lower().split()
    return words_list


def autocomplete(all_words, prefix=''):
    completed_words = []
    for item in all_words:
        if item.startswith(prefix):
            completed_words.append(item)
    print(completed_words)
    return completed_words


def benchmark(all_words, prefix): 
    time_start = time.time()
    autocomplete(all_words, prefix)
    time_end = time.time()
    return time_end - time_start



def main():
    all_words = get_words('/usr/share/dict/words')
    prefix_word = input('Please Enter In a Word: ')
    test_benchmark = benchmark(all_words,prefix_word)
    print(test_benchmark)
    

main()