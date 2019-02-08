BLACK = 0
RED = 1

class RBNode(object):

    def __init__(self, key=None, color=RED):
        self.key = key
        self.right = None
        self.left = None
        self.p = None
        self.color = color

    def __str__(self):
        return "~Node %s exists!" % self.key


class RBTree(object):

    def __init__(self):
        self.sentinel = RBNode()
        self.sentinel.right = self.sentinel.left = self.sentinel
        self.sentinel.color = BLACK
        self.root = self.sentinel
    def insert(T, z):

        z = RBNode(z)

        y = None
        x = T.root
        while x != T.sentinel and x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y is None:
            T.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = T.sentinel
        z.right = T.sentinel
        T.insertFix(z)



    def insertFix(T, z):

        while z != T.root and z.p.color == RED:
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.color == RED:
                    z.p.color = BLACK
                    y.color = BLACK
                    z.p.p.color = RED
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        T.leftRotate(z)
                    z.p.color = BLACK
                    z.p.p.color = RED
                    T.rightRotate(z.p.p)
            elif z.p == z.p.p.right:
                y = z.p.p.left
                if y.color == RED:
                    z.p.color = BLACK
                    y.color = BLACK
                    z.p.p.color = RED
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        T.rightRotate(z)
                    z.p.color = BLACK
                    z.p.p.color = RED
                    T.leftRotate(z.p.p)
        T.root.color = BLACK

    def findNode(self, key):
        current = self.root
        key = int(key)
        while current != self.sentinel:
            if key - current.key == 0:
                return current
            elif key - current.key > 0:
                current = current.right
            else:
                current = current.left

    def leftRotate(T, x):
        y = x.right
        x.right = y.left
        if y.left != T.sentinel:
            y.left.p = x
        if y != T.sentinel:
            y.p = x.p
        if x.p is None:
            T.root = y
        else:
            if x== x.p.left:
                x.p.left = y
            else:
                x.p.right = y
        y.left = x
        if x!= T.sentinel:
            x.p = y

    def rightRotate(T, x):
        y = x.left
        x.left = y.right
        if y.right != T.sentinel:
            y.right.p = x
        if y != T.sentinel:
            y.p = x.p
        if x.p is None:
            T.root = y
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x
        if x != T.sentinel:
            x.p = y
