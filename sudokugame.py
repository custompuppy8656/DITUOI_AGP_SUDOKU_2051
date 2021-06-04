from pencilmark import CmdMarking
import math
from ortools.sat.python import cp_model

def Input(filename):
    # Here you will insert the sequences you want to use
    # File you can use https://raw.githubusercontent.com/vasnastos/DITUOI_AGP_SUDOKU/main/RESOURCES/sudokusequence.input?token=APD2HAL7LD3PY3ZC7HHFPV3AXBTJM
    return list()

#Converts a sudoku sequence into a list
def ToBoard(rawdata:str)->list:
    if rawdata=='':
        return list()
    gridsize=int(math.sqrt(len(rawdata)))
    substrs=list()
    start=0
    next=gridsize
    while next<=len(rawdata):
      substrs.append(rawdata[start:next])
      start=next
      next+=gridsize
    return substrs

# Formats and display a preview into the cmd
def Formatter(sudokustr):
    if sudokustr=='':
        return
    data=ToBoard(sudokustr)
    totallinelength = len(data[0]) + 4
    print(str("." + "-" * 6 + "") * 3, end="")
    print(".")
    counter = 0
    for x in data:
        if counter % 3 == 0 and counter != 0:
            print(":", end="")
            print("------ " * 2, end="")
            print("------:")
        print("|", end="")
        for j in range(0, len(x), 3):
            print(
                str(x[j]) if x[j] != "0" else ".",
                str(x[j + 1]) if x[j + 1] != "0" else ".",
                str(x[j + 2]) if x[j + 2] != "0" else ".",
                "|",
                end="",
            )
        print()
        counter += 1
    print(str("." + "-" * 6 + "") * 3 + ".")

#Displays the Pencil Mark
def pencilMark(data):
    CmdMarking(data)


#Solve the sudoku Puzzle and return a string
def SolveSudoku(sudokustr):
    # Μοντέλο
    model = cp_model.CpModel()

    # Μεταβλητές απόφασης
    cells = dict()

    range9 = range(0, 9)

    for row in range9:
        for column in range9:
            cells[row, column] = model.NewIntVar(1, 9, f"cell{row}{column}")

    # Περιορισμοί
    # Ήδη συμπληρωμένα κελιά
    for row in range9:
        for column in range9:
            cellString = sudokustr[row * 9 + column]
            if cellString != "0":
                model.Add(cells[row, column] == int(cellString))

    ## Όλα τα κελιά σε κάθε γραμμή έχουν διαφορετική τιμή
    for row in range9:
        model.AddAllDifferent(cells[row, column] for column in range9)

    ## Όλα τα κελιά σε κάθε στήλη έχουν διαφορετική τιμή
    for column in range9:
        model.AddAllDifferent(cells[row, column] for row in range9)

    ## Όλα τα κελιά σε κάθε εσωτερικό τετράγωνο έχουν διαφορετική τιμή
    for rowid in range(0, 9, 3):
        for colid in range(0, 9, 3):
            model.AddAllDifferent(
                [
                    cells[i, j]
                    for j in range(colid, (colid + 3))
                    for i in range(rowid, (rowid + 3))
                ]
            )

    # Κλήση του επιλυτή
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    # Εκτύπωση του αποτελέσματος
    solution = ""
    if status == cp_model.OPTIMAL:
        for row in range9:
            for column in range9:
                solution = solution + str(solver.Value(cells[row, column]))
    return solution








