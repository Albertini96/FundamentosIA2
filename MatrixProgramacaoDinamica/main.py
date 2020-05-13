# -*- coding: utf-8 -*-

import numpy as np
import string
import random
import time

class MatrixHandler:
    def __init__(self):
        self.n_matrix = 0
        self.matrixes = list()
        self.vP = list()
        self.result_matrix = None
        self.mS = None
        self.add_random_matrix(2,2)
        self.char_pointer = 0
        self.chars = string.ascii_lowercase[:14] 
        
    def add_random_matrix(self, rows, cols):
        new_matrix = np.random.randint(100, size=(rows, cols))
        self.matrixes.append(new_matrix)
        self.n_matrix += 1      
        
        
    def minimize(self, i, j):
        min_val = self.big_int()
        
        min_index_k = i
        
        if (i == j):
            return 0
        
        if (self.result_matrix[i][j] != None):
            self.result_matrix[i][j]
        
        for k in range(i, j):
            minvalk = self.minimize(i, k) + self.minimize(k + 1, j) + (self.vP[i - 1] * self.vP[k] * self.vP[j])
            
            if (minvalk < min_val):
                min_val = minvalk
                min_index_k = k
        
        self.result_matrix[i][j] = min_val
        self.mS[i][j] = min_index_k
    
        return min_val
        
        
    def find_sequence(self):
        
        self.result_matrix = np.array([[None] * self.n_matrix] * self.n_matrix)
        self.mS = np.array([[None] * self.n_matrix] * self.n_matrix)
        
        for i in range(1, self.n_matrix):
            self.vP.append(self.matrixes[i].shape[0])
            
        self.vP.append(self.matrixes[self.n_matrix-1].shape[1]) 
        
        sequence = self.minimize(1, self.n_matrix-1)         
#        print('Quantidade de Multiplicações: ',sequence)
#        print()
        return sequence
        
    def print_sequece(self, i, j):
        
        result = ''
        
        bracket = self.mS[i][j]
    
        if (i == j):
            result += self.chars[self.char_pointer]
            self.char_pointer += 1
            return result

    
        result += '(';
    
        result += self.print_sequece(i, bracket)
        result += self.print_sequece(bracket + 1, j);
    
        result += ')'
    
        return result

    def big_int(self):
        return 999999999999
    


mh = MatrixHandler()
mh.add_random_matrix(826,250)
mh.add_random_matrix(250,851)
mh.add_random_matrix(851,615)
mh.add_random_matrix(615,876)
mh.add_random_matrix(876,709)
mh.add_random_matrix(709,278)
mh.add_random_matrix(278,997)
mh.add_random_matrix(997,153)
mh.add_random_matrix(153,141)
mh.add_random_matrix(141,902)

mh.find_sequence()



n_tst = 10
n_mat = 1
low = 2
high = 20

outLoop = 15
innerLoop = 1


lst_hdl = list()
for i in range(outLoop):
    
    var = 2 * i
    n_mat += 1
    
    mh = MatrixHandler()
    s_row = random.randint(low + var, high + var)
    s_col = random.randint(low + var, high + var)
    mh.add_random_matrix(s_row, s_col)
    
    for j in range(n_mat):
        
        s_row = s_col
        s_col = random.randint(low + var, high + var)
        
        print(s_row, 'x', s_col)

        mh.add_random_matrix(s_row, s_col)
    
    print()
    
    lst_hdl.append(mh)



print('Test;Number Matrixes;Time')

for i in range(outLoop):

    accTime = 0
    start = time.time()
    lst_hdl[i].find_sequence()
    end = time.time()
    accTime = (end - start)
    
    print(i, ';' , lst_hdl[i].n_matrix ,';' , str(accTime))











