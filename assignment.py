# Πρότυπο εργασίας
from sudokugame import *

def main():
    inputdata=Input('sudokusamples.txt')
    #Όταν έχετε έτοιμο τον κώδικα για το Input function διαγράφεται την παρακάτω γραμμή

    for sudoku in inputdata:
       print(f'Sequence used:{sudoku}\n')
       Formatter(sudoku)
       print()
       pencilMark(sudoku)
       print()
       solutiontoproblem=SolveSudoku(sudoku)
       Formatter(solutiontoproblem)
       print('-------------------------------------------------------------------\n')

if __name__=="__main__":
    main()
