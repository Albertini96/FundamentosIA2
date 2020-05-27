# -*- coding: utf-8 -*-

from numpy import zeros
import random as rd
rd.seed(30)


class QLearning:
    def __init__(self, reward = None, n_states = None, gama = 0.5, alpha = 1, episodes = 50, goal = None):
        
        if reward == None and n_states == None:
            n_states = 6
            
        if n_states != None:
            self.n_states = n_states
            self.reward = zeros((self.n_states, self.n_states))            

        if reward != None:
            self.reward = reward
            self.n_states = len(reward)
        
        self.start = 0
        self.episodes = episodes
        self.alpha = alpha
        self.gama = gama
        self.mq = zeros((self.n_states, self.n_states))
        self.mad = zeros((self.n_states, self.n_states))
        self.goal = goal
        
        if goal == None:
            self.goal = self.n_states - 1

    def select_rand_st(self, state):
        options = []
        for i in range(len(self.mad[state])):
            if self.mad[state][i] == 1:
                options.append(i)

        return rd.choice(options)

    def add_conn(self, frm, to, reward = 0, sided = False):
        self.reward[frm][to] = reward
        self.mad[frm][to] = 1

        if sided:
            self.reward[to][frm] = reward
            self.mad[to][frm] = 1

    def max_st(self, act):
        maxQ = 0
        for i in range(len(self.mq)):
            if self.mad[act][i] == 1:
                maxAux = self.mq[act][i]
                if maxAux > maxQ:
                    maxQ = maxAux

        return maxQ

    def q_updt(self, state, action):
        if self.goal == state:
            return

        self.mq[state][action] = ((1 - self.alpha) * self.reward[state][action]) + self.alpha * (self.reward[state][action] 
                                + (self.gama * self.max_st(action)))

    def learn(self):
        state = self.start
        while self.episodes > 0:
            randomAction = self.select_rand_st(state)
            self.q_updt(state, randomAction)
            state = randomAction
            self.episodes -= 1 

        print(self.mq)
        


q = QLearning(n_states=6, alpha=0.1, gama=0.9, goal=4)
q.add_conn(0, 1, 0, True)
q.add_conn(0, 2, 0, True)
q.add_conn(1, 3, 0, True)
q.add_conn(2, 4, 0, True)
q.add_conn(2, 3, 0, True)
q.add_conn(3, 4, 100)
q.add_conn(4, 3, 0)
q.add_conn(3, 5, 0, True)
q.add_conn(4, 5, 0)
q.add_conn(5, 4, 100)

q.learn()