from Grid import Grid
from Player  import Player
from helper import plot


class Game:
    def __init__(self, player1, player2,grid,attemptGracePeriod=3,targetMatchingDisc=4):
        self.__player1 = player1
        self.__player2 = player2
        self.__grid = grid
        self.__attemptGracePeriod = attemptGracePeriod
        self.__targetMatchingDisc = targetMatchingDisc


    @property
    def player1(self):
        return self.__player1

    @property
    def player2(self):
        return self.__player2
    @property
    def grid(self):
        return self.__grid

    @property
    def attemptGracePeriod(self):
        return self.__attemptGracePeriod
    @property
    def targetMatchingDisc(self):
        return self.__targetMatchingDisc

    def resetGame(self):
        self.grid.reset();

    def is_disc_placed_at_invalid_column(self,column):
        return self.__grid.is_disc_placed_at_invalid_column(column)

    def is_disc_placed_at_invalid_row(self,column):
        return self.__grid.is_disc_placed_at_invalid_row(column)




    def play(self):
        self.grid.show_board()
        while True:
            player1Move= int(input("Player 1 move: "))
            counter=0;
            player1LastMoveLocation=[-1,-1];

            try:
                player1LastMoveLocation=self.grid.add_disc(player1Move, self.player1)
            except:
                while counter < self.attemptGracePeriod:
                    print("invalid move");
                    player1Move = int(input("Player 1 move: "))
                    try:
                        player1LastMoveLocation=self.grid.add_disc(player1Move, self.player1)
                        break
                    except:
                        counter += 1

            if self.grid.has_player_won(self.player1,player1LastMoveLocation,self.targetMatchingDisc):
                return "Player 1 won"

            player2Move = int(input("Player 2 move: "))
            counter = 0
            player2LastMoveLocation=[-1,-1]

            try:
                player2LastMoveLocation=self.grid.add_disc(player2Move, self.player2)
            except:
                while counter < self.attemptGracePeriod:
                    print("invalid move");
                    player2Move = int(input("Player 2 move: "))
                    try:
                        player2LastMoveLocation=self.grid.add_disc(player2Move,self.player2)
                        break
                    except:
                        counter += 1
            if self.grid.has_player_won(self.player2,player2LastMoveLocation,self.targetMatchingDisc):
                return "Player 2 won"



    def playAI(self,playerMove,player:Player):
        self.grid.show_board()
        reward=0
        game_over=False
        self.score=0;
        playerLastMoveLocation=[-1,-1]
        try:
            playerLastMoveLocation=self.grid.add_disc(playerMove, player)
            reward=reward+5;
        except:
            reward=reward-10;

        if(self.grid.has_player_won(player,playerLastMoveLocation,self.targetMatchingDisc)):
            reward=reward+15;
            game_over=True
            # playerScore +=1

        return reward,game_over

        # return reward,game_over,playerScore

# plot_scores=[]
# plot_mean_scores=[]
# total_score = 0
# record = 0
# aiMove, state_old, aiReward, aiDone, aiScore=None;
#
#
# def getMoves(agent,game):
#     global state_old, aiScore, aiDone, aiReward, aiMove
#     humanMove= int(input("Player 1 move: "))
#     humanReward,humanDone,humanScore=game.playAI(humanMove,game.__player1)
#     # aiMove, state_old,aiReward, aiDone, aiScore
#     if(humanDone==False):
#         aiMove,state_old= get_agentMove(agent,game,game.player2)
#         aiReward, aiDone, aiScore =game.playAI(aiMove,game.player2)
#
#     update_agent(agent,game,game.player2, aiMove,aiReward,aiDone,aiScore,state_old)
#
# def get_agentMove(agent, game, playerAIAgent):
#     state_old = agent.get_state(game, playerAIAgent)
#     finalMove = agent.get_action(state_old, game)
#     return finalMove,state_old
#
# def update_agent(agent, game, playerAIAgent, finalMove, reward, done, score, state_old):
#         state_new = agent.get_state(game, playerAIAgent);
#
#         agent.train_short_memory(state_old, finalMove, reward, state_new, done)
#
#         agent.remember(state_old, finalMove, reward, state_new, done)
#
#         if done:
#             game.resetGame()
#             agent.numberOfGameRounds += 1
#             agent.train_long_memory()
#
#             if score > record:
#                 record = score
#                 agent.model.save()
#
#             print('Game', agent.n_games, 'Score', score, 'Record:', record)
#
#             plot_scores.append(score)
#             total_score += score
#             mean_score = total_score / agent.n_games
#             plot_mean_scores.append(mean_score)
#             plot(plot_scores, plot_mean_scores)

#
# if __name__=="__main__":
#     grid= Grid(4,4)
#     game=Game(Player.RED,Player.YELLOW,grid)
#     print(game.play())