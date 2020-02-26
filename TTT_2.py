import numpy as np

class game():
    """Takes two player objects and plays one round. Returns 'draw' or a pointer to the winner. Players required to have methods set_mark and next_move."""
    def __init__(self, player_one, player_two,m,n,k):
        self.k=k
        self.m=m
        self.n=n
        self.dio=0
        self.board = np.full((self.m,self.n), '_') # this is how the board will be represented
        # A somewhat long initialization of players and their marks 
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
    
    # actual game (wrote this first)
    def game(self):
        #print('board size:',self.board.size)
        for i in range(self.board.size): # maximum number of moves, but can finish earlier
            move = self.active_player.next_move(self.board.copy()) # cannot modify the common board
            if move in available_moves(self.board):
                self.board[move] = self.active_mark
                if self.win():
                    return self.active_player # end game
                else:
                    self.flip_players()
            else:
                self.flip_players()
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

    def win(self):
        #slice big board to small new board to set win
        s1=int(self.m+1-self.k)
        s2=int(self.n+1-self.k)
        self.dic_dio={}
        self.dic_negdio={}
        for i in range(s1):
            for j in range(s2):
                self.new=self.board[i:i+self.k,j:j+self.k]
                self.pos = (self.new == self.active_mark)
                self.dio=np.sum(np.diagonal(self.pos))
                self.negdio=np.sum(np.diagonal(self.pos[:,::-1]))
                #mij=str([i]+[j])
                #if self.active_player == self.player_one:
                 #   self.dic_dio[mij] = [dio]
                  #  self.dic_negdio[mij] = [negdio]
                    #return self.dic_dio, self.dic_negdio={}
                if self.dio == self.k: return True
                if self.negdio == self.k: return True
                for l in range(self.k):
                    if self.pos[l,:].sum() == self.k: return True
                    if self.pos[:,l].sum() == self.k: return True
       
        return False

# Note that this is not a class method, but a stand-alone function.
# I made this choice to allow players to use this function instead of writing their own methods.
def available_moves(board):
        a, b = board.shape
        am = [] # to accumulate available moves as tuples
        for i in range(a):
            for j in range(b):
                if board[i,j] == '_': am.append((i,j))
        return am

# again, this stand-alone function could be used outside interactive_player class
def print_board(board):
    a, b = board.shape   
    print(' ')
    for i in range(a):
        print (' ', end='')
        for j in range(b):
            print(board[i,j], end=' ')
        print(' ')
    print(' ')
    

class random_player():
    """Chooses a random move out of available ones."""
    def set_mark(self, mark):
        self.mark = mark
    
    def next_move(self, board):
        am = available_moves(board)
        return am[int(np.random.randint(0,len(am),1))]
    
class level_1():#win move-->move | no win move-->random
    def __init__(self,m,n,k):
        self.m=m
        self.n=n
        self.k=k
        
    def set_mark(self, mark):
        self.mark = mark
        
    def next_move(self, board):
        self.board=board
        am = available_moves(board)
        bm=am[int(np.random.randint(0,len(am),1))]
        self.levone_ls=[]
        if self.mark not in self.board:
            return bm
        else:
            for i in range(self.m-self.k+2):
                for j in range(self.n-self.k+2):
                    board_levone=self.board[i:i+self.k-1,j:j+self.k-1]
                    self.levone_pos = (board_levone == self.mark)
                    #print(levone_pos)
                    levone_dio=np.sum(np.diagonal(self.levone_pos))
                    levone_negdio=np.sum(np.diagonal(self.levone_pos[:,::-1]))
                
                    for l in range(self.k-1):
                        levone_x= self.levone_pos[l,:].sum().max()
                        levone_y= self.levone_pos[:,l].sum().max()
                    levone_max=max(levone_dio,levone_negdio,levone_x,levone_y)
                    #print(levone_max)
                    self.levone_ls += [levone_max] 
            max_m=max(self.levone_ls)
            
            for number in range(len(self.levone_ls)):
                if self.levone_ls[number] == max_m:
                    r_position=number//(self.m-self.k+2)
                    c_position=number%(self.m-self.k+2)
                    rm1=r_position-1
                    ra1=r_position+self.k-1
                    rax=r_position+1
                    cax=c_position+1
                    cm1=c_position-1
                    ca1=c_position+self.k-1
                    
            result_board=self.board[r_position:r_position+self.k-1,c_position:c_position+self.k-1]
            result_pos= (result_board == self.mark)
            if max_m == np.sum(np.diagonal(result_pos)):
                print('dio max')
                if (rm1,cm1) in am:
                    return (rm1,cm1)
                elif (ra1,ca1) in am:
                    return (ra1,ca1)
            if max_m == np.sum(np.diagonal(result_pos[:,::-1])):
                print('negdio max')
                if (rm1,cax) in am:
                    return (rm1,ca1)
                elif (rax,cm1) in am:
                    return (rax,cm1)
            
            return bm
                    
class level_2():#win move-->move | block user |no chioce-->random
    def __init__(self,m,n,k):
        self.m=m
        self.n=n
        self.k=k
        
    def set_mark(self, mark):
        self.mark = mark
        
    def next_move(self, board):
        self.board=board
        am = available_moves(board)
        bm=am[int(np.random.randint(0,len(am),1))]
        self.levone_ls=[]
        if self.mark not in self.board: #first step is random
            return bm
        else:
            #find win move
            for i in range(self.m-self.k+2):
                for j in range(self.n-self.k+2):
                    board_levone=self.board[i:i+self.k-1,j:j+self.k-1]
                    self.levone_pos = (board_levone == self.mark)
                    levone_dio=np.sum(np.diagonal(self.levone_pos))
                    levone_negdio=np.sum(np.diagonal(self.levone_pos[:,::-1]))
                
                    for l in range(self.k-1):
                        levone_x= self.levone_pos[l,:].sum().max()
                        levone_y= self.levone_pos[:,l].sum().max()
                    levone_max=max(levone_dio,levone_negdio,levone_x,levone_y)
                    self.levone_ls += [levone_max] 
                    
            max_m=max(self.levone_ls)
            for number in range(len(self.levone_ls)):
                if self.levone_ls[number] == max_m:
                    r_position=number//(self.m-self.k+2)
                    c_position=number%(self.m-self.k+2)
                    rm1=r_position-1
                    ra1=r_position+self.k-1
                    rax=r_position+1
                    cax=c_position+1
                    cm1=c_position-1
                    ca1=c_position+self.k-1
                    
            result_board=self.board[r_position:r_position+self.k-1,c_position:c_position+self.k-1]
            result_pos= (result_board == self.mark)
            if max_m == np.sum(np.diagonal(result_pos)):
                #print('dio max')
                if (rm1,cm1) in am:
                    return (rm1,cm1)
                elif (ra1,ca1) in am:
                    return (ra1,ca1)
                elif (r_position,c_position) in am:
                    return (r_position,c_position)
            if max_m == np.sum(np.diagonal(result_pos[:,::-1])):
                #print('negdio max')
                if (rm1,cax) in am:
                    return (rm1,ca1)
                elif (rax,cm1) in am:
                    return (rax,cm1)
                elif (r_position,c_position) in am:
                    return (r_position,c_position)
            
            # can't find win move. so, block user
            if self.mark=='x':
                self.opp_mark='o'
            elif self.mark=='o':
                self.opp_mark='x'
                
            self.opp_ls=[]
            for oppi in range(self.m-self.k+2):
                for oppj in range(self.n-self.k+2):
                    self.board_opp=self.board[i:i+self.k-1,j:j+self.k-1]
                    self.opp_pos = (self.board_opp == self.opp_mark)
                    self.opp_dio=np.sum(np.diagonal(self.opp_pos))
                    self.opp_negdio=np.sum(np.diagonal(self.opp_pos[:,::-1]))
                
                    for oppl in range(self.k-1):
                        self.opp_x= self.opp_pos[l,:].sum().max()
                        self.opp_y= self.opp_pos[:,l].sum().max()
                    opp_max=max(self.opp_dio,self.opp_negdio,self.opp_x,self.opp_y)
                    self.opp_ls += [opp_max] 
                    
            self.max_opp=max(self.opp_ls)
            for opp_number in range(len(self.opp_ls)):
                if self.opp_ls[opp_number] == self.max_opp:
                    self.opp_r_position=opp_number//(self.m-self.k+2)
                    self.opp_c_position=opp_number%(self.m-self.k+2)
                    self.opp_rm1=self.opp_r_position-1
                    self.opp_ra1=self.opp_r_position+self.k-1
                    self.opp_rax=self.opp_r_position+1
                    self.opp_cax=self.opp_c_position+1
                    self.opp_cm1=self.opp_c_position-1
                    self.opp_ca1=self.opp_c_position+self.k-1
                    
            self.opp_result_board=self.board[self.opp_r_position:self.opp_r_position+self.k-1,self.opp_c_position:self.opp_c_position+self.k-1]
            self.opp_result_pos= (self.opp_result_board == self.opp_mark)
            print('opp_result_board',self.opp_result_board)
            print('opp_rc:',self.opp_r_position,self.opp_c_position)
            if self.max_opp == np.sum(np.diagonal(self.opp_result_pos)):
                print('dio max opp')
                if (self.opp_rm1,self.opp_cm1) in am:
                    return (self.opp_rm1,self.opp_cm1)
                elif (self.opp_ra1,self.opp_ca1) in am:
                    return (self.opp_ra1,self.opp_ca1)
                elif (self.opp_r_position,self.opp_c_position) in am:
                    return (self.opp_r_position,self.opp_c_position)
            if self.max_opp == np.sum(np.diagonal(self.opp_result_pos[:,::-1])):
                print('negdio max opp')
                if (self.opp_rm1,self.opp_cax) in am:
                    return (self.opp_rm1,self.opp_ca1)
                elif (self.opp_rax,self.opp_cm1) in am:
                    return (self.opp_rax,self.opp_cm1)
                elif (self.opp_r_position,self.opp_c_position) in am:
                    return (self.opp_r_position,self.opp_c_position)
            
            
            
            print('its random')
            return bm #can't find win move or block user. so, random
    

    
    
class interactive_player():
    
    def set_mark(self, mark):
        self.mark = mark
   
    def next_move(self, board):
        am = available_moves(board)
        print("It's your turn. Your are playing: ", self.mark, '.', sep='')
        print_board(board)
        print('Enter your move as a i j')
        print('i and j are row and column numbers of your mark counting from 0.')
        while True:
            st = input()
            print(' ')
            r = int(st[0])
            c = int(st[2])
            if (type(r)==str) or (type(c)==str):
                print('Your input is not correct. Try, for example, ', am[0][0], ' ', am[0][1], '.', sep='')
                continue
            move = (r,c) 
            if move in am:
                return move
            else:
                print('This site is occupied. Available moves are: ')
                print(am)

def interactive_session(level):
    st = 'y'
    while st == 'y':

        player_two = interactive_player()
        if level==0:
            player_one= random_player()
        elif level==1:
            player_one = level_1(m,n,k)
        elif level ==2:
            player_one = level_2(m,n,k)
        else: print('wrong input')
            
        gm = game(player_one, player_two,m=m,n=n,k=k)
        outcome = gm.game()
        if outcome == 'draw':
         print('It is a draw')
        elif outcome == player_one:
         print('AI won.')
        else:
         print('Your won. Congratulation!')
        print_board(gm.board)
        print('AI played: ', player_one.mark, '.', sep='')
        print('You played: ', player_two.mark, '.', sep='')
        print(' ')
        st = input('Would you like to continue? Type y for yes or anything else to quit: ')

if __name__ == '__main__':
    m=int(input('please input row number as int: '))
    n=int(input('please input column number as int: '))
    k=int(input('please input the length of the sequence of marks arranged horizontally, vertically, or diagonally that constitutes a win: '))
    print('')
    print('There are three levels of AI:')
    print('AI Level 0. The program then places its own mark on a randomly chosen available position.')
    print('AI Level 1. The program checks if it can win by placing its mark in any of the available positions. If it makes the winning move.')
    print('AI Level 2. The program checks if it can win by placing its mark in any of the available positions. If so, it makes the winning move.')
    level=int(input('please input level of AI, 0, 1 or 2: '))
    interactive_session(level)
