import numpy as np
class game():
    """Takes two player objects and plays one round. Returns 'draw' or a pointer to the winner. Players required to have methods set_mark and next_move."""
    def __init__(self,player_one, player_two, m=3,n=3,k=3):
        self.k=k
        self.board = np.full((m,n), '_')
        if np.random.randint(0,2,1): # chose random player to move first; that player plays 'x' 
            player_one.set_mark('x')
            self.mark_one = 'x'
            player_two.set_mark('o')
            self.mark_two = 'o'
            self.player_one = player_one # store the pointer to the players
            self.player_two = player_two
            self.active_player = self.player_one
        else:
            player_one.set_mark('o') # reverse order
            self.mark_one = 'o'
            player_two.set_mark('x')
            self.mark_two = 'x'
            self.player_one = player_one 
            self.player_two = player_two
            self.active_player = self.player_two
        self.active_mark = 'x' # by our convention that is the active mark
            
    def available_moves(self):
        a, b = self.board.shape
        am = [] # to accumulate available moves as tuples
        for i in range(a):
            for j in range(b):
                if self.board[i,j] == '_': am.append((i,j))
        return am
    def print_board(self):
        a, b = self.board.shape   
        print(' ')
        for i in range(a):
            print (' ', end='')
            for j in range(b):
                print(self.board[i,j], end=' ')
            print(' ')
        print(' ')
    def game(self):
        for i in range(self.board.size): # maximum number of moves, but can finish earlier
            move = self.active_player.next_move(self.board.copy()) # cannot modify the common board
            if move in available_moves(self.board):
                self.board[move] = self.active_mark
                if self.win():
                    return self.active_player # end game
                else:
                    self.flip_players()
            else:
                self.flip_player()
                return self.active_player # end game because of wrong move
        return 'draw'
    # after writing this function I know that I need three other functions available_moves, flip_players, and winn

    def flip_players(self):
        if self.active_player == self.player_one:
            self.active_player = self.player_two
            self.active_mark = self.mark_two
        else:
            self.active_player = self.player_one
            self.active_mark = self.mark_one

        
        
    def user_put(self):
        #print(self.mtx)
        j,i=input('please input a mark as yx: ')
        self.j=int(j)
        self.i=int(i)
        if self.inout[(self.j*3+self.i)] == False:
            self.mtx[self.j,self.i]=1
            self.inout[(self.j*3+self.i)]=True
            print(self.mtx)
        else:
            print('please place mark in somewhere else.')
            tic.user_put()
      
    def com_put(self):
        import random
        while True:
            num=random.randint(0,8)
            if self.inout[num] == False:
                self.mtx[(num//3),(num%3)]=-1
                self.inout[num]=5
                break
        print(self.mtx)
        
    def win(self):
        pos = (self.board == self.active_mark)
        #m, n = self.board.shape # assume square for now
        for i in range(m):
            if pos[i,:].sum() == self.k: return True
            if pos[:,i].sum() == self.k: return True
        if np.sum(np.diagonal(pos)) == self.k: return True
        if np.sum(np.diagonal(pos[:,::-1])) == self.k: return True # the opposite diagonal
        return False
        
    def tic_score(self):
        ##win
        win='you win!'
        if self.inout[4]==True:
            if self.inout[1] == True and self.inout[7] == True:
                print(win)
                self.tscore=True
            elif self.inout[3] == True and self.inout[5] == True:
                print(win)
                self.tscore=True
            elif self.inout[0] == True and self.inout[8] == True:
                print(win)
                self.tscore=True
            elif self.inout[2] == True and self.inout[6] == True:
                print(win)
                self.tscore=True
        if self.inout[6] == True:
            if self.inout[0] == True and self.inout[3] ==True:
                print(win)
                self.tscore=True
            elif self.inout[7] == True and self.inout[8] ==True:
                print(win)
                self.tscore=True
        if self.inout[2]==True:
            if self.inout[1] == True and self.inout[0] == True:
                print(win)
                self.tscore=True
            elif self.inout[5] == True and self.inout[8] == True:
                print(win)
                self.tscore=True
                
        ##lose
        lo='you lose!'
        if self.inout[4] == 5: 
            if self.inout[1] == 5 and self.inout[7] == 5:
                #print(lo)
                self.tscore=5
            elif self.inout[3] == 5 and self.inout[5] == 5:
                #print(lo)
                self.tscore=5
            elif self.inout[0] == 5 and self.inout[8] == 5:
                #print(lo)
                self.tscore=5
            elif self.inout[2] == 5 and self.inout[6] == 5:
                #print(lo)
                self.tscore=5
        if self.inout[6] == 5:
            if self.inout[0] == 5 and self.inout[3] == 5:
                #print(lo)
                self.tscore=5
            elif self.inout[7] == 5 and self.inout[8] == 5:
                #print(lo)
                self.tscore=5
        if self.inout[2] == 5:
            if self.inout[1] == 5 and self.inout[0] == 5:
                #print(lo)
                self.tscore=5
            elif self.inout[5] == 5 and self.inout[8] == 5:
                #print(lo)
                self.tscore=5
                
   
    def play(self):
        
        #print('inout:',self.inout)
        
        print(self.mtx)
        
        self.tscore=False
        
        tic.user_put()
        tic.com_put()
        while self.tscore != True:
            #print('inout:',self.inout)
            
            tic.user_put()
            tic.com_put()
            tic.tic_score()
            
            if False not in self.inout:
                print('game is over, no winner this time.')
                break
            if self.tscore == 5:
                print('try again!')
                break
                
