import time

class Node:

    '''
        is_word == if the node is a word
        children == dict of {character: <node_object>}
        counter == count up how many times the letter is inserted so we can get all possible word from that
                    node's char

        all_sub_node recursively call its sub-nodes to get all words until there is no more node
        and yield from will stop.
    '''

    def __init__(self):
        self.is_word = False
        self.children = {}
        self.counter = 1

    def all_sub_node(self, prefix):

        # if it is a word then return that value as object
        if self.is_word:
            yield prefix

        # recursive call through all children and its sub children of the current node
        for char, child in self.children.items():
            next_prefix = prefix + char
            yield from child.all_sub_node(next_prefix)


class Trie:
    # existing methods here
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        current_node = self.root

        # loop through all character and it's nodes until we reach the last character and set that node to True
        for char in word:
            # everytime a node is loop through, possible word for that letter become +1
            current_node.counter += 1
            node = current_node.children.get(char)

            # if the node does not exist then we create new node and set current node's children to new Node
            if not node:
                node = Node()
                current_node.children[char] = node

            #if node does exist
            current_node = node
        # set the last node to True because the word is finished inserting
        current_node.is_word = True

    def get_prefix(self, prefix):
        current_node = self.root

        # find if all the character in the prefix exist in our trie first.
        for char in prefix:
            current_node = current_node.children.get(char)

            # if the node does not exist, prefix is invalid or incomplete
            if current_node is None:
                return None
        
        # you can return current_node counter to see how many words are possible with given prefix
        # return current_node.counter

        # if all the prefix character exist then we can call on the all_sub_node method in that last node
        yield from current_node.all_sub_node(prefix)

        # yield from can be written like this. ('yield from' is syntactical sugar):
        # for objects in current_node.all_sub_node(prefix):
        #     yield objects


def get_words(filename):
    '''Opening file and getting/cleaning all words from that file'''
    with open(filename, 'r') as file:
        words_list = file.read().split()
    return words_list


def benchmark(trie, prefixes): 
    '''Getting Time Stamp by searching for prefix'''
    benchmark_time_start = time.time()

    for prefix in prefixes:
        # return a generator object <node_object>, wrap it with list() method to get raw data
        trie.get_prefix(prefix)

    benchmark_time_end = time.time()
    return benchmark_time_end - benchmark_time_start


def main():

    # initializing root node
    trie = Trie()

    '''Getting dictionary words and prefixes'''

    all_words = get_words('/usr/share/dict/words')
    all_prefixes = set([word[:len(word)//2] for word in all_words])

    '''Starting Insertion'''

    print('Inserting', len(all_words), 'Words')
    inserting_time_start = time.time()
    for word in all_words:
        trie.insert(word)
    inserting_time_finish = time.time()
    print('Done Insertion Time:', inserting_time_finish - inserting_time_start, 'seconds')

    '''Finding time for one prefix'''

    # time1 = time.time()
    # print(list(trie.get_prefix('a')))
    # print(time.time() - time1)

    '''Finding time for all prefixes (default 71000 prefixes iterated) below'''

    total_time = 0
    count = 0
    for i in range(5):
        total_time += benchmark(trie, all_prefixes)
        count += 1
    average_time = total_time / count

    print('Finish Benchmarking', len(all_prefixes), 'Words', 'x', count, 'times')
    print('Average Time:', average_time, 'seconds')

main()