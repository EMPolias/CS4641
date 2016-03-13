from MatrixPrototypes import *

from matplotlib.pyplot import show, ion, axis
import random
import networkx as nx

def display(matrix, points):
    axis((-5, 10*len(points.keys()) + 5, -5, 10*len(points.keys()) + 5))
    nx.draw(matrix.graph(), points)
    show()

def getRandom(vertices):
    return {vertex : (random.randrange(10*len(vertices)),
            random.randrange(10*len(vertices))) for vertex in vertices}

matrixWeb = AdjacencyMatrix(24)
matrixWeb.addVertices(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X"])
matrixWeb.addEdge("A", "B")
matrixWeb.addEdge("B", "C")
matrixWeb.addEdge("C", "D")
matrixWeb.addEdge("D", "E")
matrixWeb.addEdge("E", "F")
matrixWeb.addEdge("F", "G")
matrixWeb.addEdge("G", "H")
matrixWeb.addEdge("H", "A")
matrixWeb.addEdge("I", "J")
matrixWeb.addEdge("J", "K")
matrixWeb.addEdge("K", "L")
matrixWeb.addEdge("L", "M")
matrixWeb.addEdge("M", "N")
matrixWeb.addEdge("N", "O")
matrixWeb.addEdge("O", "P")
matrixWeb.addEdge("P", "I")
matrixWeb.addEdge("Q", "R")
matrixWeb.addEdge("R", "S")
matrixWeb.addEdge("S", "T")
matrixWeb.addEdge("T", "U")
matrixWeb.addEdge("U", "V")
matrixWeb.addEdge("V", "W")
matrixWeb.addEdge("W", "X")
matrixWeb.addEdge("X", "Q")
matrixWeb.addEdge("A", "I")
matrixWeb.addEdge("B", "J")
matrixWeb.addEdge("C", "K")
matrixWeb.addEdge("D", "L")
matrixWeb.addEdge("E", "M")
matrixWeb.addEdge("F", "N")
matrixWeb.addEdge("G", "O")
matrixWeb.addEdge("H", "P")
matrixWeb.addEdge("I", "Q")
matrixWeb.addEdge("J", "R")
matrixWeb.addEdge("K", "S")
matrixWeb.addEdge("L", "T")
matrixWeb.addEdge("M", "U")
matrixWeb.addEdge("N", "V")
matrixWeb.addEdge("O", "W")
matrixWeb.addEdge("P", "X")


randSolution = getRandom(matrixWeb.vertices)

rhc_solution = {
"A": (457.000000, 314.000000),
"B": (446.000000, 430.000000),
"C": (395.000000, 382.000000),
"D": (307.000000, 262.000000),
"E": (250.000000, 150.000000),
"F": (258.000000, 0.000000),
"G": (323.000000, 39.000000),
"H": (394.000000, 163.000000),
"I": (334.000000, 347.000000),
"J": (329.000000, 499.000000),
"K": (284.000000, 424.000000),
"L": (227.000000, 296.000000),
"M": (175.000000, 187.000000),
"N": (166.000000, 32.000000),
"O": (238.000000, 81.000000),
"P": (306.000000, 192.000000),
"Q": (258.000000, 359.000000),
"R": (216.000000, 465.000000),
"S": (166.000000, 416.000000),
"T": (130.000000, 321.000000),
"U": (89.000000, 203.000000),
"V": (109.000000, 99.000000),
"W": (178.000000, 117.000000),
"X": (235.000000, 224.000000)
}

sima_solution = {
"A": (221.000000, 169.000000),
"B": (120.000000, 201.000000),
"C": (93.000000, 272.000000),
"D": (174.000000, 348.000000),
"E": (269.000000, 352.000000),
"F": (331.000000, 319.000000),
"G": (340.000000, 249.000000),
"H": (290.000000, 189.000000),
"I": (228.000000, 99.000000),
"J": (72.000000, 150.000000),
"K": (28.000000, 298.000000),
"L": (154.000000, 439.000000),
"M": (292.000000, 491.000000),
"N": (386.000000, 362.000000),
"O": (409.000000, 236.000000),
"P": (332.000000, 133.000000),
"Q": (242.000000, 27.000000),
"R": (136.000000, 93.000000),
"S": (163.000000, 271.000000),
"T": (231.000000, 411.000000),
"U": (358.000000, 467.000000),
"V": (454.000000, 379.000000),
"W": (485.000000, 221.000000),
"X": (378.000000, 80.000000)
}

genal_solution = {
"A": (406.000000, 190.000000),
"B": (492.000000, 495.000000),
"C": (203.000000, 330.000000),
"D": (34.000000, 256.000000),
"E": (48.000000, 394.000000),
"F": (201.000000, 476.000000),
"G": (80.000000, 298.000000),
"H": (136.000000, 380.000000),
"I": (352.000000, 177.000000),
"J": (240.000000, 60.000000),
"K": (11.000000, 22.000000),
"L": (102.000000, 486.000000),
"M": (167.000000, 194.000000),
"N": (352.000000, 276.000000),
"O": (220.000000, 272.000000),
"P": (355.000000, 394.000000),
"Q": (152.000000, 124.000000),
"R": (143.000000, 218.000000),
"S": (78.000000, 246.000000),
"T": (362.000000, 394.000000),
"U": (249.000000, 161.000000),
"V": (194.000000, 299.000000),
"W": (214.000000, 232.000000),
"X": (72.000000, 191.000000)
}

mimic_solution = {
"A": (32.000000, 480.000000),
"B": (372.000000, 484.000000),
"C": (478.000000, 253.000000),
"D": (418.000000, 121.000000),
"E": (421.000000, 366.000000),
"F": (319.000000, 380.000000),
"G": (288.000000, 433.000000),
"H": (60.000000, 406.000000),
"I": (48.000000, 311.000000),
"J": (200.000000, 96.000000),
"K": (442.000000, 81.000000),
"L": (449.000000, 207.000000),
"M": (423.000000, 318.000000),
"N": (88.000000, 257.000000),
"O": (161.000000, 477.000000),
"P": (245.000000, 467.000000),
"Q": (360.000000, 331.000000),
"R": (309.000000, 299.000000),
"S": (140.000000, 36.000000),
"T": (180.000000, 182.000000),
"U": (142.000000, 251.000000),
"V": (116.000000, 335.000000),
"W": (164.000000, 373.000000),
"X": (297.000000, 494.000000)
}


display(matrixWeb, randSolution)
display(matrixWeb, rhc_solution)
display(matrixWeb, sima_solution)
display(matrixWeb, genal_solution)
display(matrixWeb, mimic_solution)
