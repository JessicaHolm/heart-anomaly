#! /usr/bin/python3

import sys
import os

class Heart(object):

    def __init__(self, filename):
        with open(filename, "r") as f:
            n = int(os.stat(filename).st_size / 23 / 2)
            T = [[0] * 23 for _ in range(n)]
            for i,row in zip(range(n), f):
                rows = row.strip().split(",")
                for j,col in zip(range(23), rows):
                    num = int(col)
                    T[i][j] = num
        self.T = T
        self.F = [[]]
        self.N = []

    def learn(self):
        self.F = [[0] * 22 for _ in range(2)]
        self.N = [0] * 2
        for t in self.T:
            tc = t[0]
            tf = t[1:len(t)]
            self.N[tc] = self.N[tc] + 1
            for j,f in zip(range(22), tf):
                if tf[j] == 1:
                    self.F[tc][j] = self.F[tc][j] + 1

def usage():
    print("usage: python3 heart.py filename")

if len(sys.argv) != 2: usage()
filename = sys.argv[1]
h = Heart(filename)
h.learn()
print(h.F)
print(h.N)
