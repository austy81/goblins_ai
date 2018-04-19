from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
from random import randint


# https://github.com/Vict0rSch/deep_learning/tree/master/keras/recurrent
# https://github.com/jjrob13/deep_ultimate_tic_tac_toe/blob/master/utils.py
# https://keras.io/layers/recurrent/
# https://gist.github.com/EderSantana/c7222daa328f0e885093#file-qlearn-py-L147-L148
class AgentKeras:

    def __init__(self):
        self.history = []
        self.model = Sequential()
        self.model.add(Dense(64, input_dim=18))
        self.model.add(Activation('relu'))
        self.model.add(Dense(9))
        self.model.add(Activation('softmax'))
        self.model.compile(optimizer='rmsprop',
                           loss='categorical_crossentropy',
                           metrics=['accuracy'])

    def act(self, board):
        state = self._board_to_state(board)
        prediction = self.model.predict(state)[0]
        max = np.max(prediction)
        min = np.min(prediction)
        if max == min:
            return randint(0, 8)
        return np.argmax(prediction)

    def new_game(self):
        self.history = []

    def learn(self, board, action, reward):
        self.history.append(
            {'state': self._board_to_state(board), 'action': action})

        if reward < -1:  # unallowed move
            state = self._board_to_state(board)
            predict = self.model.predict(state)[0]
            predict[action] += reward
            self.model.train_on_batch(np.array([state]), np.array([predict]))
            return

        if reward != 0:  # end of game
            x = []
            y = []
            for history_entry in self.history:
                state = history_entry['state']
                action = history_entry['action']

                predict = self.model.predict(state)[0]  # get current prediction
                predict[action] += reward  # add reward
                
                x.append(state)
                y.append(predict)

            self.model.train_on_batch(np.array(x), y)

    def _board_to_state(self, board):
        state = []
        for cell in board:
            filled = 1 if cell == 1 else 0
            state.append(filled)
        for cell in board:
            filled = 1 if cell == 2 else 0
            state.append(filled)
        return np.array(state)
