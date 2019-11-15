#! /usr/bin/python3

import sys
import os
import math

class Heart(object):

    def __init__(self, train_file, test_file):
        self.create_training(train_file)
        self.create_test(test_file)
        self.F = [[]]
        self.N = []
        self.L = []

    def create_training(self, train_file):
        with open(train_file, "r") as f:
            n = int(os.stat(train_file).st_size / 23 / 2)
            T = [[0] * 23 for _ in range(n)]
            for i,row in zip(range(n), f):
                rows = row.strip().split(",")
                for j,col in zip(range(23), rows):
                    num = int(col)
                    T[i][j] = num
        self.T = T
        self.n = n

    def create_test(self, test_file):
        with open(test_file, "r") as f:
            n = int(os.stat(test_file).st_size / 23 / 2)
            C = [[0] * 23 for _ in range(n)]
            for i,row in zip(range(n), f):
                rows = row.strip().split(",")
                for j,col in zip(range(23), rows):
                    num = int(col)
                    C[i][j] = num
        self.C = C
        self.n = n

    def train(self):
        self.F = [[0] * 22 for _ in range(2)]
        self.N = [0] * 2
        for t in self.T:
            tc = t[0]
            tf = t[1:len(t)]
            self.N[tc] += + 1
            for j,f in zip(range(22), tf):
                if tf[j] == 1:
                    self.F[tc][j] += 1
    
    def determine_likelihood(self):
        N = self.N
        F = self.F
        n = self.n
        self.L = [[math.log10(N[i] + 0.5) - math.log10(N[0] + N[1] + 0.5)] * n for i in range(2)]
        for i in range(2):
            for j,c in zip(range(n), self.C):
                cf = c[1:len(c)]
                for k in range(22):
                    s = F[i][k]
                    if cf[k] == 0:
                        s = N[i] - s
                    self.L[i][j] += math.log10(s + 0.5) - math.log10(N[i] + 0.5)

   def classify(self):
        list1 = self.L[0]
        list2 = self.L[1]
        R = []
        for c0,c1 in zip(list1, list2):
            if c1 > c0:
                R.append(1)
            else:
                R.append(0)
        self.R = R

    def verify(self):
        correct = 0
        for c,r in zip(self.C, self.R):
            if c[0] == r:
                correct += 1

        print("orig {}/{} ({})".format(correct, self.n, correct/self.n))


def usage():
    print("usage: python3 heart.py training_file test_file")
    exit(0)

if len(sys.argv) != 3: usage()
train_file = sys.argv[1]
test_file = sys.argv[2]
h = Heart(train_file, test_file)
h.train()
h.determine_likelihood()
h.classify()
h.verify()
# print(h.F)
# print(h.N)
# print(h.L)
