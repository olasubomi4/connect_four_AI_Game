from collections import deque
import numpy as np
from distributed.protocol import torch
import torch
from helper import plot
from Game import Game
from Grid import Grid
from Model import Linear_QNet, QTrainer
from Player import Player
import random

LR = 0.001
MAX_MEMORY = 100_000
BATCH_SIZE = 1000
class Agent:

    def __init__(self,grid_rows,grid_cols):
        self.numberOfGameRounds = 0
        self.grid_rows = grid_rows
        self.grid_cols = grid_cols
        self.__epsilon=0
        self.__gamma=0.90
        self.__memory= deque(maxlen=MAX_MEMORY)
        self.__model= Linear_QNet((grid_rows*grid_cols)+ grid_rows+1,256,grid_cols);
        self.trainer = QTrainer(self.__model, lr=LR, gamma=self.__gamma)

    @property
    def epsilon(self):
        return self.__epsilon

    @epsilon.setter
    def epsilon(self,epsilon):
        self.__epsilon=epsilon

    @property
    def memory(self):
        return self.__memory

    @property
    def model(self):
        return self.__model

    def get_state(self,game:Game,agentPlayer:Player):
        a=self.get_flattend_game_grid(game,agentPlayer)
        b=self.get_danger_point(game,agentPlayer)
        state = np.concatenate((a,
                               b))
        return state



    def get_danger_point(self,game:Game,agentPlayer:Player):
        columns= game.grid.columns
        danger_points = np.zeros(columns)  # Example of danger points for each column
        for col in range(columns):
            if game.is_disc_placed_at_invalid_column(col) or game.is_disc_placed_at_invalid_row(col):  # Assuming `is_danger` is a function that checks danger for a column
                danger_points[col] = 1
        return np.array(danger_points,dtype=int)



    def get_flattend_game_grid(self,game:Game,agentPlayer:Player):
        rows=game.grid.rows
        columns=game.grid.columns
        game_grid= np.zeros((rows,columns),dtype=int)

        for row in range(rows):
            for col in range(columns):
                if game.grid.board[row][col] == agentPlayer.playerSignature:
                    game_grid[row][col] = -1
                elif game.grid.board[row][col] == 0:
                    game_grid[row][col] = 0
                else:
                    game_grid[row][col] = -1
        flattened_game_board= game_grid.flatten()
        return np.array(flattened_game_board).flatten()

    def remember(self,state,action,reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def train_long_memory(self):
        if len(self.memory) > BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE)
        else:
            mini_sample = self.memory

        states, actions, rewards, next_states, dones = zip(*mini_sample)
        self.trainer.train_step(states,actions,rewards,next_states,dones)


    def train_short_memory(self, state, action, reward, next_state, done):
        self.trainer.train_step(state, action, reward, next_state, done)

    def get_action(self, state,game):

        self.epsilon = 80 - self.numberOfGameRounds
        rows=game.grid.rows
        # final_move= [0 for i in range(rows)];

        if random.randint(0,200) < self.epsilon:
            move= random.randrange(0,rows)
            final_move = move

        else:
            state0 = torch.tensor(state, dtype=torch.float)
            prediction = self.model(state0)
            move = torch.argmax(prediction).item()
            final_move = move

        return final_move





def train():
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    human_score = 0
    record = 0
    agent = Agent(grid_rows=6, grid_cols=7)
    grid = Grid(7, 6)
    player_human = Player.RED
    player_ai_agent = Player.YELLOW
    game = Game(player_human, player_ai_agent, grid)
    human_done=False
    state_old=None
    ai_reward=None
    ai_move=None
    ai_done=False
    while True:
        if human_done:
            state_new = agent.get_state(game, player_ai_agent)
            ai_reward -=20;
            agent.train_short_memory(state_old, ai_move, ai_reward, state_new, ai_done)
            agent.remember(state_old, ai_move, ai_reward, state_new, ai_done)
            human_done = False
            state_old = None
            ai_reward = None
            ai_move = None
            ai_done = False
            game.resetGame()
            agent.numberOfGameRounds += 1
            agent.train_long_memory()
            ##penalise agent
        else :
            state_old = agent.get_state(game, player_ai_agent)
            ai_move = agent.get_action(state_old, game)
            ai_reward, ai_done = game.playAI(ai_move, player_ai_agent)
            state_new = agent.get_state(game, player_ai_agent)
            agent.train_short_memory(state_old, ai_move, ai_reward, state_new, ai_done)
            agent.remember(state_old, ai_move, ai_reward, state_new, ai_done)
            if ai_done:
                game.resetGame()
                agent.numberOfGameRounds += 1
                agent.train_long_memory()

                if ai_reward > record:
                    record = ai_reward
                    agent.model.save()

                print(f'Game {agent.numberOfGameRounds}, Score {ai_reward}, Record: {record}')

                plot_scores.append(ai_reward)
                total_score += ai_reward
                mean_score = total_score / agent.numberOfGameRounds
                plot_mean_scores.append(mean_score)
                plot(plot_scores, plot_mean_scores)

                human_done = False
                state_old = None
                ai_reward = None
                ai_move = None
                ai_done = False

            else:

                human_move = int(input("Human Enter a move: "))
                reward, human_done = game.playAI(human_move, player_human)

if __name__ == '__main__':
    train()