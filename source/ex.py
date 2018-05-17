#!python
import time

from typing import Tuple

class Node(object):

    def __init__(self, char: str):
        self.char = char
        self.children = []

        #is it a word?
        self.word_finished = False
        self.data = ''

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
            new_node = Node(char)
            node.children.append(new_node)
            # print('appended: ', (new_node.char))
            node = new_node
        
    node.word_finished =  True
    node.data = word
    # print(node.word_finished, node.data)


# def find_prefix(root, prefix):
#     all_words = list()

#     if prefix == None or prefix == '':
#         raise ValueError('Require a Prefix')
#     if not root.children:
#         raise ValueError('No letters inside Trie')
    
#     current_node = root

#     for char in prefix:
#         for child in current_node.children:
#             if child.char == char:
#                 current_node = child
#                 if current_node.word_finished == True:
#                     all_words.append(current_node.data)
    
#     return all_words



                
def get_words(filename):
    with open(filename, 'r') as file:
        words_list = file.read().lower().split()
    return words_list
    

def benchmark(root, prefixes): 
    time_start = time.time()

    for prefix in prefixes:
        print(find_prefix(root, prefix))

    time_end = time.time()
    return time_end - time_start


if __name__ == "__main__":
    root = Node('*')

    # all_words = get_words('/usr/share/dict/words')
    all_words = get_words('dummy.txt')
    # all_prefixes =
    #  set([word[:len(word)//2] for word in all_words])
    all_prefixes = ['hello']
    
    for word in all_words:
        insert(root, word)

    # print(benchmark(root, all_prefixes))
    
    