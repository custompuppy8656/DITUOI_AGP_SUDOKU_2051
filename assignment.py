# Πρότυπο εργασίας
from sudokugame import *

def main():
    inputdata=Input('sudokusamples.txt')
    #Όταν έχετε έτοιμο τον κώδικα για το Input function διαγράφεται την παρακάτω γραμμή
    inputdata.append('068420709001070450037085010002109080809300005010040096084006003000000800050034001')
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
