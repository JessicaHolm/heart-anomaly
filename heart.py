#! /usr/bin/python3

import sys
import os
import math

class Heart(object):

    def __init__(self, train_file, test_file):
        T = self.create_data(train_file)
        C = self.create_data(test_file)
        self.F = [[]]
        self.N = []
        self.L = []
        self.T = T
        self.C = C

    def create_data(self, data_file):
        with open(data_file, "r") as f:
            D = []
            i = 0
            for rows in f:
                row = rows.strip().split(",")
                num_cols = len(row)
                for j in range(num_cols):
                    row[j] = int(row[j])
                D.append(row)
                i += 1
        self.n = i
        self.features = num_cols - 1
        return D

    def train(self):
        self.F = [[0] * self.features for _ in range(2)]
        self.N = [0] * 2
        for t in self.T:
            tc = t[0]
            tf = t[1:len(t)]
            self.N[tc] += + 1
            for j,f in zip(range(self.features), tf):
                if tf[j] == 1:
                    self.F[tc][j] += 1
    
    def determine_likelihood(self):
        N = self.N
        self.L = [[math.log10(N[i] + 0.5) - math.log10(N[0] + N[1] + 0.5)] * self.n for i in range(2)]
        for i in range(2):
            for j,c in zip(range(self.n), self.C):
                cf = c[1:len(c)]
                for k in range(self.features):
                    s = self.F[i][k]
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

    def verify(self, kind):
        correct = 0
        true_negative = 0
        true_positive = 0
        total_negative = 0
        total_positive = 0
        for c,r in zip(self.C, self.R):
            if c[0] == 0:
                total_negative += 1
                if c[0] == r:
                    true_negative += 1
                    correct += 1
            if c[0] == 1:
                total_positive += 1
                if c[0] == r:
                    true_positive += 1
                    correct += 1

        print("{} {}/{} ({}) {}/{} ({}) {}/{} ({})"
        .format(kind, correct, self.n, round(correct/self.n, 2),
        true_negative, total_negative, round(true_negative/total_negative, 2),
        true_positive, total_positive, round(true_positive/total_positive, 2)))

def usage():
    print("usage: python3 heart.py training_file test_file")
    exit(0)

if len(sys.argv) != 3: usage()
train_file = sys.argv[1]
test_file = sys.argv[2]
kind = test_file[test_file.find('-')+1:test_file.find('.')]
h = Heart(train_file, test_file)
h.train()
h.determine_likelihood()
h.classify()
h.verify(kind)
