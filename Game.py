import tkinter as Tkinter
import random as Random
import Assets

class Game(Tkinter.Frame):
    
    def __init__(self):
        Tkinter.Frame.__init__(self)
        self.grid()
        self.master.title('2048 Game')
        self.mainGrid = Tkinter.Frame(self, background = Assets.GRID_COLOR, border = 3, width = 400, height = 400)
        self.mainGrid.grid(pady = (100, 0))
        
        self.GUI()
        self.StartGame()
        
        self.master.bind('<Left>', self.LeftArrow)
        self.master.bind('<Right>', self.RightArrow)
        self.master.bind('<Up>', self.UpArrow)
        self.master.bind('<Down>', self.DownArrow)
        
        self.mainloop()
    
    # GUI Method Of Our Game Program
    def GUI(self):

        ''' Initializing The Main Grid, Which Will Contain EveryThing '''
        self.Grid = [] 
        for X in range(4):
            Row = []
            for Y in range(4):
                gridFrame = Tkinter.Frame(self.mainGrid, background = Assets.EMPTY_CELL_COLOR, width = 100, height = 100)
                gridFrame.grid(row = X, column = Y, padx = 5, pady = 5 )
                gridNumber = Tkinter.Label(self.mainGrid, background = Assets.EMPTY_CELL_COLOR)
                gridNumber.grid(row = X, column = Y)
                gridData = {'frame' : gridFrame, 'number' : gridNumber}
                Row.append(gridData)
            self.Grid.append(Row)
        
        ''' Now, Displaying The Score On The Top '''
        scoreFrame = Tkinter.Frame(self)
        scoreFrame.place(relx = 0.5, y = 40, anchor = 'center')
        Tkinter.Label(scoreFrame, text = 'Score', font = Assets.SCORE_LABEL_FONT).grid(row = 0)
        self.scoreLabel = Tkinter.Label(scoreFrame, text = '0', font = Assets.SCORE_FONT)
        self.scoreLabel.grid(row = 1)
    
    # Function To Start The Game
    def StartGame(self):
        # Creating A Matrix Of 0's
        self.Matrix = [ [0] * 4 for _ in range(4) ]
        
        # ByDefault, User Will Get Two Random Cells With Value = 2
        row = Random.randint(0, 3)
        col = Random.randint(0, 3)
        self.Matrix[row][col] = 2
        self.Grid[row][col]['frame'].configure(background = Assets.CELL_COLORS[2])
        self.Grid[row][col]['number'].configure(background = Assets.CELL_COLORS[2], foreground = Assets.CELL_NUMBER_COLORS[2], font = Assets.CELL_NUMBER_FONTS[2], text = '2')
        
        while self.Matrix[row][col] != 0:
            row = Random.randint(0, 3)
            col = Random.randint(0, 3)
        self.Matrix[row][col] = 2
        self.Grid[row][col]['frame'].configure(background = Assets.CELL_COLORS[2])
        self.Grid[row][col]['number'].configure(background=Assets.CELL_COLORS[2], foreground=Assets.CELL_NUMBER_COLORS[2], font=Assets.CELL_NUMBER_FONTS[2], text='2')
        
        self.score = 0
        
    # Function To Manipulate The Matrix
    def ManipulateMatrix(self):
        newMatrix = [ [0] * 4 for _ in range(4) ]
        for row in range(4):
            positionFilled = 0
            for col in range(4):
                if self.Matrix[row][col] != 0:
                    newMatrix[row][positionFilled] = self.Matrix[row][col]
                    positionFilled += 1
        
        self.Matrix = newMatrix
    
    # Function To Combine Cells
    def Combine(self):
        for row in range(4):
            for col in range(3):
                if self.Matrix[row][col] != 0 and self.Matrix[row][col] == self.Matrix[row][col + 1]:
                    self.Matrix[row][col] *= 2
                    self.Matrix[row][col + 1] = 0
                    self.score += self.Matrix[row][col]
    # Function To Reverse The Matrix
    def Reverse(self):
        newMatrix = []
        for row in range(4):
            newMatrix.append([])
            for col in range(4):
                newMatrix[row].append(self.Matrix[row][3 - col])
        self.Matrix = newMatrix
    
    # Function To Transpose The Matrix
    def Transpose(self):
        newMatrix = [ [0] * 4 for _ in range(4) ]
        for row in range(4):
            for col in range(4):
                newMatrix[row][col] = self.Matrix[col][row]
        self.Matrix = newMatrix
        
    # Function To Add New Block
    def AddNewBlock(self):
        if any( 0 in row for row in self.Matrix ):
            row = Random.randint(0, 3)
            col = Random.randint(0, 3)
            while self.Matrix[row][col] != 0:
                row = Random.randint(0, 3)
                col = Random.randint(0, 3)
            self.Matrix[row][col] = Random.choice([2, 4])

    # Function To Update The GUI To Match The Updated Matrix
    def UpdateGUI(self):
        for row in range(4):
            for col in range(4):
                cellValue = self.Matrix[row][col]
                if cellValue == 0:
                    self.Grid[row][col]['frame'].configure(background = Assets.EMPTY_CELL_COLOR)
                    self.Grid[row][col]['number'].configure(background = Assets.EMPTY_CELL_COLOR, text = '')
                else:
                    self.Grid[row][col]['frame'].configure(background = Assets.CELL_COLORS[cellValue])
                    self.Grid[row][col]['number'].configure(
                        background=Assets.CELL_COLORS[cellValue], foreground=Assets.CELL_NUMBER_COLORS[cellValue], font = Assets.CELL_NUMBER_FONTS[cellValue], text = str(cellValue) )
        
        self.scoreLabel.configure(text = self.score)
        self.update_idletasks()
    
    # Function To Bind Arrow Keys On Pressing
    def LeftArrow(self, event):
        self.CallManipulateCombineManipulate()
        self.CallAddUpdateOver()
    
    def RightArrow(self, event):
        self.Reverse()
        self.CallManipulateCombineManipulate()
        self.Reverse()
        self.CallAddUpdateOver()
    
    def UpArrow(self, event):
        self.Transpose()
        self.CallManipulateCombineManipulate()
        self.Transpose()
        self.CallAddUpdateOver()
    
    def DownArrow(self, event):
        self.Transpose()
        self.Reverse()
        self.CallManipulateCombineManipulate()
        self.Reverse()
        self.Transpose()
        self.CallAddUpdateOver()


    # TODO Rename this here and in `LeftArrow`, `RightArrow`, `UpArrow` and `DownArrow`
    def CallAddUpdateOver(self):
        self.AddNewBlock()
        self.UpdateGUI()
        self.GameOver()
    
    def CallManipulateCombineManipulate(self):
        self.ManipulateMatrix()
        self.Combine()
        self.ManipulateMatrix()
        
    # Check If There Are Any Horizontal Move Possible
    def CheckHorizontalMove(self):
        for row in range(4):
            for col in range(3):
                if self.Matrix[row][col] == self.Matrix[row][col + 1]:
                    return True
        return False

    # Check If There Are Any Vertical Move Possible
    def CheckVerticalMove(self):
        for row in range(3):
            for col in range(4):
                if self.Matrix[row][col] == self.Matrix[row + 1][col]:
                    return True
        return False
    
    # Function To Check Game Is Over Or Not.
    def GameOver(self):
        if any(2048 in row for row in self.Matrix):
            gameOverFrame = Tkinter.Frame(self.mainGrid, borderwidth = 2)
            gameOverFrame.place(relx = 0.5, rely = 0.5, anchor = 'center')
            Tkinter.Label(gameOverFrame, text = 'Yoo! You Win :)', background = Assets.WINNER_BG, foreground = Assets.GAME_OVER_FONT_COLOR, font = Assets.GAME_OVER_FONT).pack()

        elif (
            all(0 not in row for row in self.Matrix)
            and not self.CheckHorizontalMove()
            and not self.CheckVerticalMove()
        ):
            gameOverFrame = Tkinter.Frame(self.mainGrid, borderwidth = 2)
            gameOverFrame.place(relx = 0.5, rely = 0.5, anchor = 'center')
            Tkinter.Label(gameOverFrame, text = 'Game Over', background = Assets.LOSER_BG, foreground = Assets.GAME_OVER_FONT_COLOR, font = Assets.GAME_OVER_FONT).pack()
        
            
def Play():
    Game()
    
if __name__ == '__main__':
    Play()
        
    
    
    
        
            
        