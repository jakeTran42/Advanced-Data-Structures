#!python
import time

from typing import Tuple

class TrieNode(object):

    def __init__(self, char: str):
        self.char = char
        self.children = []

        #is it a word?
        self.word_finished = False
    

def insert(root, word: str):
    node = root
    for char in word:
        found = False
        for child in node.children:
            if child.char == char:
                node = child
                found =  True
                break
        
        if not found:
            new_node = TrieNode(char)
            node.children.append(new_node)
            print('appended: ', (new_node.char))
            node = new_node
        
    node.word_finished =  True



def find_prefix(root, prefix: str):

    node = root
    complete_word = ''
    completed_words = []

    if not root.children:
        return False, 0

    for char in prefix:
        char_not_found = True
        for child in node.children:
            if child.char == char:
                # print('found: ', char)
                char_not_found = False
                node = child
                break
        if char_not_found:
            return False, 0

    return completed_words

def get_words(filename):
    with open(filename, 'r') as file:
        words_list = file.read().lower().split()
    return words_list
    

def benchmark(root, prefixes): 
    time_start = time.time()

    for prefix in prefixes:
        print(prefix)
        print(find_prefix(root, prefix))

    time_end = time.time()
    return time_end - time_start


if __name__ == "__main__":
    root = TrieNode('*')

    # all_words = get_words('/usr/share/dict/words')
    all_words = get_words('dummy.txt')
    # all_prefixes = set([word[:len(word)//2] for word in all_words])
    all_prefixes = ['hello', 'i']
    # print(len(all_prefixes))
    for word in all_words:
        insert(root, word)
    
    print(benchmark(root, all_prefixes))
    
    