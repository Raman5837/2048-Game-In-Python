import random as Random
from typing import List

class MyGame:
    
    Width, Height, WinningValue = 4, 4, 2048
    
    def __init__(self) -> None:
        
        self.Board = [ [ 0 for _ in range(self.Width) ] for _ in range(self.Height) ]
    
    def ShowBoard(self) -> None:
        for Row in self.Board: print(Row)
    
    def ReadInput(self) -> str:
        userInput = input("Choose Any One [ 1 : LEFT, 2 : RIGHT, 3 : UP, 4 : DOWN ] : ")
        inputMapping = {'3': 'UP', '1': 'LEFT', '4': 'DOWN', '2': 'RIGHT'}
        return inputMapping[userInput]
        
    def GetEmptyPositions(self) -> List:
        CELL = []
        for Row in range(len(self.Board)):
            for Col in range(len(self.Board[0])):
                if self.Board[Row][Col] == 0:
                    CELL.append([Row, Col])
        return CELL
    
    def HasUserWon(self) -> bool:
        for Row in range(len(self.Board)):
            for Col in range(len(self.Board[0])):
                if self.Board[Row][Col] == self.WinningValue:
                    return True
        return False
    
    def SetValue(self, Position, Value) -> None:
        self.Board[Position[0]][Position[1]] = Value
    
    def GetRandomValueForBoard(self) -> int:
        return Random.choice([2,4])
    
    def GameOver(self) -> str:
        return 'OOPS! Game Over'
    
    def Start(self) -> None:
        # Should Game Be Continue After A Win ?
        shouldGameBeContinue = False
        while True:
            emptyPositions = self.GetEmptyPositions()
            if len(emptyPositions) == 0:
                self.GameOver()
                break
            if not shouldGameBeContinue and self.HasUserWon():
                print("\n Congratulations You Won!! \n")
                if(input("Continue Playing ? YES / NO : ") == "YES" or 'yes'):
                    shouldGameBeContinue = True
                else:
                    break
            emptyRandomChoice = Random.choice(emptyPositions)
            self.SetValue(emptyRandomChoice,self.GetRandomValueForBoard())
            self.ShowBoard()
            while True:
                if self.Move(self.ReadInput()) == True:
                    break
                else:
                    print("Operation Cannot Be Performed")
    
    def Move(self, Direction) -> bool:
        if Direction in ["UP", "DOWN"]:
            return self.MoveVertical(Direction)
        elif Direction in ["LEFT", "RIGHT"]:
            return self.MoveHorizontal(Direction)
        print("Invalid Move")
        return False
    
    def MoveHorizontal(self, Direction) -> bool:
        moved = False
        if Direction == "LEFT":
            increment, start = 1, 0
            end = len(self.Board[0]) - 1
            
        elif Direction == "RIGHT":
            start = len(self.Board[0]) - 1
            increment =- 1
            end = 0
        for row in range(len(self.Board)):
            if Direction == "LEFT":
                start = 0
            elif Direction == "RIGHT":
                start = len(self.Board[0]) - 1
            while start != end:
                k = start + increment
                while k >= 0 and k < len(self.Board[row]) and self.Board[row][k] == 0:
                    k += increment
                if k >= 0 and k < len(self.Board[row]):
                    
                    if self.Board[row][start] != 0:
                        if self.Board[row][k] == self.Board[row][start]:
                            self.Board[row][start] += self.Board[row][k]
                            self.Board[row][k] = 0
                            moved = True
                    else:
                        self.Board[row][start] = self.Board[row][k]
                        self.Board[row][k] = 0
                        moved = True
                        continue
                start +=increment
        return moved
    
    def MoveVertical(self, Direction) -> bool:
        moved = False
        if len(self.Board) > 0:
            if Direction == "DOWN":
                start = len(self.Board) - 1
                increment =- 1
                end = 0
            elif Direction == "UP":
                start, increment = 0, 1
                end = len(self.Board) - 1
            for col in range(len(self.Board[0])):
                if Direction == "UP":
                    start = 0
                elif Direction == "DOWN":
                    start = len(self.Board[0]) - 1
                while start != end:
                    k = start + increment
                    while k >= 0 and k < len(self.Board) and self.Board[k][col] == 0:
                        k += increment
                    if k >= 0 and k < len(self.Board):

                        if self.Board[start][col] != 0:
                            if self.Board[k][col] == self.Board[start][col]:
                                self.Board[start][col] += self.Board[k][col]
                                self.Board[k][col] = 0
                                moved = True
                        else:
                            self.Board[start][col] = self.Board[k][col]
                            self.Board[k][col] = 0
                            moved = True
                            continue
                    start += increment
        return moved


if __name__ == "__main__":
    Game = MyGame()
    Game.Start()