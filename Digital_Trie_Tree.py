
class DTTree(object):

    def __init__(self):
        self.child = {}
        self.isWord = False

    def insert(self, string):
        node = self
        for i, char in enumerate(string):
            if char in node.child:
                node = node.child[char]
            else:
                break
        else:
            node.isWord = True
            i += 1
        for char in string[i:]:
            node.child[char] = node = DTTree()
        else:
            node.isWord = True

    def inspect(trie, deepness=0):      # this is just to help in debugging
        """
        Shows a nicely formatted and indented Trie.
        Cannot be tested as equivalent representations are randomly chosen from.
        """
        for i in trie.child:
            print("{}{} {}".format(
                " " * deepness, i, DTTree.inspect(trie.child[i], deepness + 1)))

    def search(self, key):
        node = self
        for char in key:
            if char in node.child:
                node = node.child[char]
            else:
                return None
        if node.isWord:
            return '~%s exists' % key

    def delete(self, key):
        node = self
        for char in key:
            if char in node.child:
                if len(node.child[char]) == 1:
                    del node.child[char]
                    break
                node = node.child[char]

    def __len__(self):
        n = 1 if self.isWord else 0
        for k in self.child.keys():
           n = n + len(self.child[k])
        return n

