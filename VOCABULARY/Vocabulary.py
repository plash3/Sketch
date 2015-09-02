"""
class Vocabulary

Vocabulary is a collection of words. They can be strings
of random characters and not necessarily English words.

Let each word in the vocabulary represent a vertex in an
undirected graph. In this graph, two vertices (words) are
connected (i.e. there is an edge between these two vertices)
if the edit distance between the two words is 1 (again, edit
distance of 1 between word w1 and word w2 means that you can
obtain w1 from w2 by a single character
deletion/insertion/substitution).

Write a function, that accepts the vocabulary (in the form
of a set) and a word (a word by definition must be contained
in the vocabulary):
def word_clique(vocab, w):
    ...

This function should return the set of all words reachable
from w (i.e. all words x such that there is a path in the
graph from x to w).
"""

import Graph
import Vertex

class Vocabulary(Graph.Graph):

    def __init__(self):
        # Vertices is a dictionary; a key being words' length
        # and values being a list of words of that length.
        # Words in the vocabulary are dispersed in various
        # bundles arranged by their legths.
        self.vertices = {}

    # Checks if edit distance between two words is 1. Edit distance of 1
    # between word w1 and word w2 means that w1 can be obtained from w2
    # by a single character deletion / insertion / substitution.
    @staticmethod
    def _is_edit_distance_one(s, t):
        ans = True
        ls = len(s)
        lt = len(t)
        diff = abs(ls - lt)
        if diff > 1:
            ans = False
        elif diff == 0:
            cnt = 0
            for i in xrange(ls):
                if s[i] != t[i]:
                    cnt += 1
                if cnt > 1:
                    ans = False
                    break
        else:
        # diff == 1
            cnt = 0
            if ls > lt:
                ln = lt
                longer = s
                shorter = t
            else:
                ln = ls
                longer = t
                shorter = s
            for i in xrange(ln):
                # consider a sample - 'ABCEF' and 'ABCDEF'
                # when it comes to 'D' it has to skip a letter
                # and proceed to the next one
                if shorter[i] != longer[i+cnt]:
                    cnt += 1
                    if shorter[i] != longer[i+cnt]:
                        cnt += 1
                if cnt > 1:
                    ans = False
                    break
        return ans

    # Adds a word to the vocabulary. Checks that there is no
    # duplicate values. Disperses words in various bundles
    # arranging them by their legths.
    def add_vertex(self, val):
        l = len(val)
        # if there is a word in the vocabulary of the same lenght
        # then append the word to that bundle
        if l in self.vertices:
            s = self.vertices[l]
            if val not in s:
                s.append(val)
        else:
            self.vertices[l] = [val]

    # Gets an adjacency list for a given node - word - its neighbours.
    def adj(self, vertex):
        adjl = []
        val = vertex.value
        # one word must not be 1 letter longer than the other word
        # so that the edit distance of 1 be met
        for l in xrange(len(val) - 1, len(val) + 2):
            if l in self.vertices:
                # scan a bundle of words of legth l
                for w in self.vertices[l]:
                    # check that edit distance between 2 words is 1
                    # avoiding duplicates - itself
                    if w == val:
                        continue
                    if Vocabulary._is_edit_distance_one(w, val):
                        v = Vertex.Vertex(w)
                        adjl.append(v)
        return adjl
