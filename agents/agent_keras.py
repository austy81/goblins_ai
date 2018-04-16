from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
from random import randint


# https://github.com/Vict0rSch/deep_learning/tree/master/keras/recurrent
# https://github.com/jjrob13/deep_ultimate_tic_tac_toe/blob/master/utils.py
# https://keras.io/layers/recurrent/ 
class AgentKeras:

    def __init__(self):
        self.model = Sequential()
        self.model.add(Dense(32, input_dim=784))
        self.model.add(Activation('relu'))

    def act(self, board):
        return randint(0, 8)
        
    def new_game(self):
        pass

    def learn(self, board, action, reward):
        pass
   