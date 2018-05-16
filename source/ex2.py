import time

class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}

    def all_words(self, prefix):
        if self.end:
            yield prefix

        for letter, child in self.children.items():
            yield from child.all_words(prefix + letter)

class Trie:
    # existing methods here
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for letter in word:
            node = curr.children.get(letter)
            if not node:
                node = TrieNode()
                curr.children[letter] = node
            curr = node
        curr.end = True

    def all_words_beginning_with_prefix(self, prefix):
        cur = self.root
        for c in prefix:
            cur = cur.children.get(c)
            if cur is None:
                return  # No words with given prefix

        yield from cur.all_words(prefix)

trie = Trie()
# trie.insert('foobar')
# trie.insert('foo')
# trie.insert('bar')
# trie.insert('foob')
# trie.insert('foof')

# print(list(trie.all_words_beginning_with_prefix('foo')))

def get_words(filename):
    with open(filename, 'r') as file:
        words_list = file.read().lower().split()
    return words_list


def benchmark(prefixes): 
    time_start = time.time()

    for prefix in prefixes:
        list(trie.all_words_beginning_with_prefix(prefix))

    time_end = time.time()
    return time_end - time_start

# all_words = get_words('dummy.txt')
all_words = get_words('words.txt')
all_prefixes = set([word[:len(word)//2] for word in all_words])
# all_prefixes = ['hello']

time1 = time.time()
for word in all_words:
    # print('inserting ' + word)
    trie.insert(word)

# time1 = time.time()
# print(list(trie.all_words_beginning_with_prefix('a')))
# print(time.time() - time1)


# print('Done Insertion. Time is:', time.time() - time1)
# print(benchmark(all_prefixes))