from sub import *
import threading as th
from scipy.spatial import KDTree
import Queue

class Tree(th.Thread):

    def __init__(self):
        self.Tree = KDTree()

