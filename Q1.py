# imports
import pulp
import numpy as np

def isnotzero(x):
    if x > 0:
        return 1
    else:
        return 2

#
prob = pulp.LpProblem('Q2', pulp.LpMinimize)

# Variáveis de decisão
x0y0 = pulp.LpVariable('x0y0', lowBound=0, cat='Integer')
x0y0_bin = pulp.LpVariable('x0y0_bin', lowBound=0, upBound = 1, cat='Integer')
x1y0 = pulp.LpVariable('x1y0', lowBound=0, cat='Integer')
x1y0_bin = pulp.LpVariable('x1y0_bin', lowBound=0, upBound = 1, cat='Integer')
x2y0 = pulp.LpVariable('x2y0', lowBound=0, cat='Integer')
x2y0_bin = pulp.LpVariable('x2y0_bin', lowBound=0, upBound = 1, cat='Integer')
x3y0 = pulp.LpVariable('x3y0', lowBound=0, cat='Integer')
x3y0_bin = pulp.LpVariable('x3y0_bin', lowBound=0, upBound = 1, cat='Integer')
x4y0 = pulp.LpVariable('x4y0', lowBound=0, cat='Integer')
x4y0_bin = pulp.LpVariable('x4y0_bin', lowBound=0, upBound = 1, cat='Integer')

x0y1 = pulp.LpVariable('x0y1', lowBound=0, cat='Integer')
x0y1_bin = pulp.LpVariable('x0y1_bin', lowBound=0, upBound = 1, cat='Integer')
x1y1 = pulp.LpVariable('x1y1', lowBound=0, cat='Integer')
x1y1_bin = pulp.LpVariable('x1y1_bin', lowBound=0, upBound = 1, cat='Integer')
x2y1 = pulp.LpVariable('x2y1', lowBound=0, cat='Integer')
x2y1_bin = pulp.LpVariable('x2y1_bin', lowBound=0, upBound = 1, cat='Integer')
x3y1 = pulp.LpVariable('x3y1', lowBound=0, cat='Integer')
x3y1_bin = pulp.LpVariable('x3y1_bin', lowBound=0, upBound = 1, cat='Integer')
x4y1 = pulp.LpVariable('x4y1', lowBound=0, cat='Integer')
x4y1_bin = pulp.LpVariable('x4y1_bin', lowBound=0, upBound = 1, cat='Integer')

x0y2 = pulp.LpVariable('x0y2', lowBound=0, cat='Integer')
x0y2_bin = pulp.LpVariable('x0y2_bin', lowBound=0, upBound = 1, cat='Integer')
x1y2 = pulp.LpVariable('x1y2', lowBound=0, cat='Integer')
x1y2_bin = pulp.LpVariable('x1y2_bin', lowBound=0, upBound = 1, cat='Integer')
x2y2 = pulp.LpVariable('x2y2', lowBound=0, cat='Integer')
x2y2_bin = pulp.LpVariable('x2y2_bin', lowBound=0, upBound = 1, cat='Integer')
x3y2 = pulp.LpVariable('x3y2', lowBound=0, cat='Integer')
x3y2_bin = pulp.LpVariable('x3y2_bin', lowBound=0, upBound = 1, cat='Integer')
x4y2 = pulp.LpVariable('x4y2', lowBound=0, cat='Integer')
x4y2_bin = pulp.LpVariable('x4y2_bin', lowBound=0, upBound = 1, cat='Integer')

x0y3 = pulp.LpVariable('x0y3', lowBound=0, cat='Integer')
x0y3_bin = pulp.LpVariable('x0y3_bin', lowBound=0, upBound = 1, cat='Integer')
x1y3 = pulp.LpVariable('x1y3', lowBound=0, cat='Integer')
x1y3_bin = pulp.LpVariable('x1y3_bin', lowBound=0, upBound = 1, cat='Integer')
x2y3 = pulp.LpVariable('x2y3', lowBound=0, cat='Integer')
x2y3_bin = pulp.LpVariable('x2y3_bin', lowBound=0, upBound = 1, cat='Integer')
x3y3 = pulp.LpVariable('x3y3', lowBound=0, cat='Integer')
x3y3_bin = pulp.LpVariable('x3y3_bin', lowBound=0, upBound = 1, cat='Integer')
x4y3 = pulp.LpVariable('x4y3', lowBound=0, cat='Integer')
x4y3_bin = pulp.LpVariable('x4y3_bin', lowBound=0, upBound = 1, cat='Integer')

x0y4 = pulp.LpVariable('x0y4', lowBound=0, cat='Integer')
x0y4_bin = pulp.LpVariable('x0y4_bin', lowBound=0, upBound = 1, cat='Integer')
x1y4 = pulp.LpVariable('x1y4', lowBound=0, cat='Integer')
x1y4_bin = pulp.LpVariable('x1y4_bin', lowBound=0, upBound = 1, cat='Integer')
x2y4 = pulp.LpVariable('x2y4', lowBound=0, cat='Integer')
x2y4_bin = pulp.LpVariable('x2y4_bin', lowBound=0, upBound = 1, cat='Integer')
x3y4 = pulp.LpVariable('x3y4', lowBound=0, cat='Integer')
x3y4_bin = pulp.LpVariable('x3y4_bin', lowBound=0, upBound = 1, cat='Integer')
x4y4 = pulp.LpVariable('x4y4', lowBound=0, cat='Integer')
x4y4_bin = pulp.LpVariable('x4y4_bin', lowBound=0, upBound = 1, cat='Integer')

x0y5 = pulp.LpVariable('x0y5', lowBound=0, cat='Integer')
x0y5_bin = pulp.LpVariable('x0y5_bin', lowBound=0, upBound = 1, cat='Integer')
x1y5 = pulp.LpVariable('x1y5', lowBound=0, cat='Integer')
x1y5_bin = pulp.LpVariable('x1y5_bin', lowBound=0, upBound = 1, cat='Integer')
x2y5 = pulp.LpVariable('x2y5', lowBound=0, cat='Integer')
x2y5_bin = pulp.LpVariable('x2y5_bin', lowBound=0, upBound = 1, cat='Integer')
x3y5 = pulp.LpVariable('x3y5', lowBound=0, cat='Integer')
x3y5_bin = pulp.LpVariable('x3y5_bin', lowBound=0, upBound = 1, cat='Integer')
x4y5 = pulp.LpVariable('x4y5', lowBound=0, cat='Integer')
x4y5_bin = pulp.LpVariable('x4y5_bin', lowBound=0, upBound = 1, cat='Integer')

x0y6 = pulp.LpVariable('x0y6', lowBound=0, cat='Integer')
x0y6_bin = pulp.LpVariable('x0y6_bin', lowBound=0, upBound = 1, cat='Integer')
x1y6 = pulp.LpVariable('x1y6', lowBound=0, cat='Integer')
x1y6_bin = pulp.LpVariable('x1y6_bin', lowBound=0, upBound = 1, cat='Integer')
x2y6 = pulp.LpVariable('x2y6', lowBound=0, cat='Integer')
x2y6_bin = pulp.LpVariable('x2y6_bin', lowBound=0, upBound = 1, cat='Integer')
x3y6 = pulp.LpVariable('x3y6', lowBound=0, cat='Integer')
x3y6_bin = pulp.LpVariable('x3y6_bin', lowBound=0, upBound = 1, cat='Integer')
x4y6 = pulp.LpVariable('x4y6', lowBound=0, cat='Integer')
x4y6_bin = pulp.LpVariable('x4y6_bin', lowBound=0, upBound = 1, cat='Integer')

x0y7 = pulp.LpVariable('x0y7', lowBound=0, cat='Integer')
x0y7_bin = pulp.LpVariable('x0y7_bin', lowBound=0, upBound = 1, cat='Integer')
x1y7 = pulp.LpVariable('x1y7', lowBound=0, cat='Integer')
x1y7_bin = pulp.LpVariable('x1y7_bin', lowBound=0, upBound = 1, cat='Integer')
x2y7 = pulp.LpVariable('x2y7', lowBound=0, cat='Integer')
x2y7_bin = pulp.LpVariable('x2y7_bin', lowBound=0, upBound = 1, cat='Integer')
x3y7 = pulp.LpVariable('x3y7', lowBound=0, cat='Integer')
x3y7_bin = pulp.LpVariable('x3y7_bin', lowBound=0, upBound = 1, cat='Integer')
x4y7 = pulp.LpVariable('x4y7', lowBound=0, cat='Integer')
x4y7_bin = pulp.LpVariable('x4y7_bin', lowBound=0, upBound = 1, cat='Integer')

x0y8 = pulp.LpVariable('x0y8', lowBound=0, cat='Integer')
x0y8_bin = pulp.LpVariable('x0y8_bin', lowBound=0, upBound = 1, cat='Integer')
x1y8 = pulp.LpVariable('x1y8', lowBound=0, cat='Integer')
x1y8_bin = pulp.LpVariable('x1y8_bin', lowBound=0, upBound = 1, cat='Integer')
x2y8 = pulp.LpVariable('x2y8', lowBound=0, cat='Integer')
x2y8_bin = pulp.LpVariable('x2y8_bin', lowBound=0, upBound = 1, cat='Integer')
x3y8 = pulp.LpVariable('x3y8', lowBound=0, cat='Integer')
x3y8_bin = pulp.LpVariable('x3y8_bin', lowBound=0, upBound = 1, cat='Integer')
x4y8 = pulp.LpVariable('x4y8', lowBound=0, cat='Integer')
x4y8_bin = pulp.LpVariable('x4y8_bin', lowBound=0, upBound = 1, cat='Integer')

x0y9 = pulp.LpVariable('x0y9', lowBound=0, cat='Integer')
x0y9_bin = pulp.LpVariable('x0y9_bin', lowBound=0, upBound = 1, cat='Integer')
x1y9 = pulp.LpVariable('x1y9', lowBound=0, cat='Integer')
x1y9_bin = pulp.LpVariable('x1y9_bin', lowBound=0, upBound = 1, cat='Integer')
x2y9 = pulp.LpVariable('x2y9', lowBound=0, cat='Integer')
x2y9_bin = pulp.LpVariable('x2y9_bin', lowBound=0, upBound = 1, cat='Integer')
x3y9 = pulp.LpVariable('x3y9', lowBound=0, cat='Integer')
x3y9_bin = pulp.LpVariable('x3y9_bin', lowBound=0, upBound = 1, cat='Integer')
x4y9 = pulp.LpVariable('x4y9', lowBound=0, cat='Integer')
x4y9_bin = pulp.LpVariable('x4y9_bin', lowBound=0, upBound = 1, cat='Integer')



precos = [[10, 15, 10, 15, 20, 20, 20, 40, 10, 30],
                [30, 15, 10, 20, 10, 20, 20, 30, 20, 30],
                [20, 10, 5, 15, 10, 15, 15, 10, 5, 5],
                [40, 25, 15, 20, 10, 30, 30, 10, 15, 10],
                [30, 30, 25, 10, 5, 35, 35, 15, 5, 10]]


# Definindo função objetivo
custo = precos[0][0]*x0y0 + precos[1][0]*x1y0 + precos[2][0]*x2y0 + precos[3][0]*x3y0 + precos[4][0]*x4y0 + \
        precos[0][1]*x0y1 + precos[1][1]*x1y1 + precos[2][1]*x2y1 + precos[3][1]*x3y1 + precos[4][1]*x4y1 + \
        precos[0][2]*x0y2 + precos[1][2]*x1y2 + precos[2][2]*x2y2 + precos[3][2]*x3y2 + precos[4][2]*x4y2 + \
        precos[0][3]*x0y3 + precos[1][3]*x1y3 + precos[2][3]*x2y3 + precos[3][3]*x3y3 + precos[4][3]*x4y3 + \
        precos[0][4]*x0y4 + precos[1][4]*x1y4 + precos[2][4]*x2y4 + precos[3][4]*x3y4 + precos[4][4]*x4y4 + \
        precos[0][5]*x0y5 + precos[1][5]*x1y5 + precos[2][5]*x2y5 + precos[3][5]*x3y5 + precos[4][5]*x4y5 + \
        precos[0][6]*x0y6 + precos[1][6]*x1y6 + precos[2][6]*x2y6 + precos[3][6]*x3y6 + precos[4][6]*x4y6 + \
        precos[0][7]*x0y7 + precos[1][7]*x1y7 + precos[2][7]*x2y7 + precos[3][7]*x3y7 + precos[4][7]*x4y7 + \
        precos[0][8]*x0y8 + precos[1][8]*x1y8 + precos[2][8]*x2y8 + precos[3][8]*x3y8 + precos[4][8]*x4y8 + \
        precos[0][9]*x0y9 + precos[1][9]*x1y9 + precos[2][9]*x2y9 + precos[3][9]*x3y9 + precos[4][9]*x4y9


# Add a função-objetivo
prob += custo

# Restrições
washington = x0y0 + x1y0 + x2y0 + x3y0 + x4y0
oregon = x0y1 + x1y1 + x2y1 + x3y1 + x4y1
california = x0y2 + x1y2 + x2y2 + x3y2 + x4y2
idaho = x0y3 + x1y3 + x2y3 + x3y3 + x4y3
nevada = x0y4 + x1y4 + x2y4 + x3y4 + x4y4
montana = x0y5 + x1y5 + x2y5 + x3y5 + x4y5
wyoming = x0y6 + x1y6 + x2y6 + x3y6 + x4y6
arizona = x0y7 + x1y7 + x2y7 + x3y7 + x4y7
utah = x0y8 + x1y8 + x2y8 + x3y8 + x4y8
colorado = x0y9 + x1y9 + x2y9 + x3y9 + x4y9

seattle = x0y0 + x0y1 + x0y2 + x0y3 + x0y4 + x0y5 + x0y6 + x0y7 + x0y8 + x0y9
francisco = x1y0 + x1y1 + x1y2 + x1y3 + x1y4 + x1y5 + x1y6 + x1y7 + x1y8 + x1y9
vegas = x2y0 + x2y1 + x2y2 + x2y3 + x2y4 + x2y5 + x2y6 + x2y7 + x2y8 + x2y9
phoenix = x3y0 + x3y1 + x3y2 + x3y3 + x3y4 + x3y5 + x3y6 + x3y7 + x3y8 + x3y9
denver = x4y0 + x4y1 + x4y2 + x4y3 + x4y4 + x4y5 + x4y6 + x4y7 + x4y8 + x4y9

washington_min = x0y0_bin + x1y0_bin + x2y0_bin + x3y0_bin + x4y0_bin
oregon_min = x0y1_bin + x1y1_bin + x2y1_bin + x3y1_bin + x4y1_bin
california_min = x0y2_bin + x1y2_bin + x2y2_bin + x3y2_bin + x4y2_bin
idaho_min = x0y3_bin + x1y3_bin + x2y3_bin + x3y3_bin + x4y3_bin
nevada_min = x0y4_bin + x1y4_bin + x2y4_bin + x3y4_bin + x4y4_bin
montana_min = x0y5_bin + x1y5_bin + x2y5_bin + x3y5_bin + x4y5_bin
wyoming_min = x0y6_bin + x1y6_bin + x2y6_bin + x3y6_bin + x4y6_bin
arizona_min = x0y7_bin + x1y7_bin + x2y7_bin + x3y7_bin + x4y7_bin
utah_min = x0y8_bin + x1y8_bin + x2y8_bin + x3y8_bin + x4y8_bin
colorado_min = x0y9_bin + x1y9_bin + x2y9_bin + x3y9_bin + x4y9_bin

x0y0_rec = x0y0 - x0y0_bin*25
x1y0_rec = x1y0 - x1y0_bin*30
x2y0_rec = x2y0 - x2y0_bin*30
x3y0_rec = x3y0 - x3y0_bin*35
x4y0_rec = x4y0 - x4y0_bin*25 #
x0y1_rec = x0y1 - x0y1_bin*25
x1y1_rec = x1y1 - x1y1_bin*30
x2y1_rec = x2y1 - x2y1_bin*30
x3y1_rec = x3y1 - x3y1_bin*35
x4y1_rec = x4y1 - x4y1_bin*25 #
x0y2_rec = x0y2 - x0y2_bin*25
x1y2_rec = x1y2 - x1y2_bin*30
x2y2_rec = x2y2 - x2y2_bin*30
x3y2_rec = x3y2 - x3y2_bin*35
x4y2_rec = x4y2 - x4y2_bin*25 #
x0y3_rec = x0y3 - x0y3_bin*25
x1y3_rec = x1y3 - x1y3_bin*30
x2y3_rec = x2y3 - x2y3_bin*30
x3y3_rec = x3y3 - x3y3_bin*35
x4y3_rec = x4y3 - x4y3_bin*25 #
x0y4_rec = x0y4 - x0y4_bin*25
x1y4_rec = x1y4 - x1y4_bin*30
x2y4_rec = x2y4 - x2y4_bin*30
x3y4_rec = x3y4 - x3y4_bin*35
x4y4_rec = x4y4 - x4y4_bin*25 #
x0y5_rec = x0y5 - x0y5_bin*25
x1y5_rec = x1y5 - x1y5_bin*30
x2y5_rec = x2y5 - x2y5_bin*30
x3y5_rec = x3y5 - x3y5_bin*35
x4y5_rec = x4y5 - x4y5_bin*25 #
x0y6_rec = x0y6 - x0y6_bin*25
x1y6_rec = x1y6 - x1y6_bin*30
x2y6_rec = x2y6 - x2y6_bin*30
x3y6_rec = x3y6 - x3y6_bin*35
x4y6_rec = x4y6 - x4y6_bin*25 #
x0y7_rec = x0y7 - x0y7_bin*25
x1y7_rec = x1y7 - x1y7_bin*30
x2y7_rec = x2y7 - x2y7_bin*30
x3y7_rec = x3y7 - x3y7_bin*35
x4y7_rec = x4y7 - x4y7_bin*25 #
x0y8_rec = x0y8 - x0y8_bin*25
x1y8_rec = x1y8 - x1y8_bin*30
x2y8_rec = x2y8 - x2y8_bin*30
x3y8_rec = x3y8 - x3y8_bin*35
x4y8_rec = x4y8 - x4y8_bin*25 #
x0y9_rec = x0y9 - x0y9_bin*25
x1y9_rec = x1y9 - x1y9_bin*30
x2y9_rec = x2y9 - x2y9_bin*30
x3y9_rec = x3y9 - x3y9_bin*35
x4y9_rec = x4y9 - x4y9_bin*25 #

x0y0_rec_2 = x0y0 - x0y0_bin*175
x1y0_rec_2 = x1y0 - x1y0_bin*175
x2y0_rec_2 = x2y0 - x2y0_bin*175
x3y0_rec_2 = x3y0 - x3y0_bin*175
x4y0_rec_2 = x4y0 - x4y0_bin*175 #
x0y1_rec_2 = x0y1 - x0y1_bin*175
x1y1_rec_2 = x1y1 - x1y1_bin*175
x2y1_rec_2 = x2y1 - x2y1_bin*175
x3y1_rec_2 = x3y1 - x3y1_bin*175
x4y1_rec_2 = x4y1 - x4y1_bin*175 #
x0y2_rec_2 = x0y2 - x0y2_bin*175
x1y2_rec_2 = x1y2 - x1y2_bin*175
x2y2_rec_2 = x2y2 - x2y2_bin*175
x3y2_rec_2 = x3y2 - x3y2_bin*175
x4y2_rec_2 = x4y2 - x4y2_bin*175 #
x0y3_rec_2 = x0y3 - x0y3_bin*175
x1y3_rec_2 = x1y3 - x1y3_bin*175
x2y3_rec_2 = x2y3 - x2y3_bin*175
x3y3_rec_2 = x3y3 - x3y3_bin*175
x4y3_rec_2 = x4y3 - x4y3_bin*175 #
x0y4_rec_2 = x0y4 - x0y4_bin*175
x1y4_rec_2 = x1y4 - x1y4_bin*175
x2y4_rec_2 = x2y4 - x2y4_bin*175
x3y4_rec_2 = x3y4 - x3y4_bin*175
x4y4_rec_2 = x4y4 - x4y4_bin*175 #
x0y5_rec_2 = x0y5 - x0y5_bin*175
x1y5_rec_2 = x1y5 - x1y5_bin*175
x2y5_rec_2 = x2y5 - x2y5_bin*175
x3y5_rec_2 = x3y5 - x3y5_bin*175
x4y5_rec_2 = x4y5 - x4y5_bin*175 #
x0y6_rec_2 = x0y6 - x0y6_bin*175
x1y6_rec_2 = x1y6 - x1y6_bin*175
x2y6_rec_2 = x2y6 - x2y6_bin*175
x3y6_rec_2 = x3y6 - x3y6_bin*175
x4y6_rec_2 = x4y6 - x4y6_bin*175 #
x0y7_rec_2 = x0y7 - x0y7_bin*175
x1y7_rec_2 = x1y7 - x1y7_bin*175
x2y7_rec_2 = x2y7 - x2y7_bin*175
x3y7_rec_2 = x3y7 - x3y7_bin*175
x4y7_rec_2 = x4y7 - x4y7_bin*175 #
x0y8_rec_2 = x0y8 - x0y8_bin*175
x1y8_rec_2 = x1y8 - x1y8_bin*175
x2y8_rec_2 = x2y8 - x2y8_bin*175
x3y8_rec_2 = x3y8 - x3y8_bin*175
x4y8_rec_2 = x4y8 - x4y8_bin*175 #
x0y9_rec_2 = x0y9 - x0y9_bin*175
x1y9_rec_2 = x1y9 - x1y9_bin*175
x2y9_rec_2 = x2y9 - x2y9_bin*175
x3y9_rec_2 = x3y9 - x3y9_bin*175
x4y9_rec_2 = x4y9 - x4y9_bin*175 #


# Add restrições
prob += (x0y0_rec >= 0)
prob += (x1y0_rec >= 0)
prob += (x2y0_rec >= 0)
prob += (x3y0_rec >= 0)
prob += (x4y0_rec >= 0)
prob += (x0y1_rec >= 0)
prob += (x1y1_rec >= 0)
prob += (x2y1_rec >= 0)
prob += (x3y1_rec >= 0)
prob += (x4y1_rec >= 0)
prob += (x0y2_rec >= 0)
prob += (x1y2_rec >= 0)
prob += (x2y2_rec >= 0)
prob += (x3y2_rec >= 0)
prob += (x4y2_rec >= 0)
prob += (x0y3_rec >= 0)
prob += (x1y3_rec >= 0)
prob += (x2y3_rec >= 0)
prob += (x3y3_rec >= 0)
prob += (x4y3_rec >= 0)
prob += (x0y4_rec >= 0)
prob += (x1y4_rec >= 0)
prob += (x2y4_rec >= 0)
prob += (x3y4_rec >= 0)
prob += (x4y4_rec >= 0)
prob += (x0y5_rec >= 0)
prob += (x1y5_rec >= 0)
prob += (x2y5_rec >= 0)
prob += (x3y5_rec >= 0)
prob += (x4y5_rec >= 0)
prob += (x0y6_rec >= 0)
prob += (x1y6_rec >= 0)
prob += (x2y6_rec >= 0)
prob += (x3y6_rec >= 0)
prob += (x4y6_rec >= 0)
prob += (x0y7_rec >= 0)
prob += (x1y7_rec >= 0)
prob += (x2y7_rec >= 0)
prob += (x3y7_rec >= 0)
prob += (x4y7_rec >= 0)
prob += (x0y8_rec >= 0)
prob += (x1y8_rec >= 0)
prob += (x2y8_rec >= 0)
prob += (x3y8_rec >= 0)
prob += (x4y8_rec >= 0)
prob += (x0y9_rec >= 0)
prob += (x1y9_rec >= 0)
prob += (x2y9_rec >= 0)
prob += (x3y9_rec >= 0)
prob += (x4y9_rec >= 0)

prob += (x0y0_rec_2 <= 0)
prob += (x1y0_rec_2 <= 0)
prob += (x2y0_rec_2 <= 0)
prob += (x3y0_rec_2 <= 0)
prob += (x4y0_rec_2 <= 0)
prob += (x0y1_rec_2 <= 0)
prob += (x1y1_rec_2 <= 0)
prob += (x2y1_rec_2 <= 0)
prob += (x3y1_rec_2 <= 0)
prob += (x4y1_rec_2 <= 0)
prob += (x0y2_rec_2 <= 0)
prob += (x1y2_rec_2 <= 0)
prob += (x2y2_rec_2 <= 0)
prob += (x3y2_rec_2 <= 0)
prob += (x4y2_rec_2 <= 0)
prob += (x0y3_rec_2 <= 0)
prob += (x1y3_rec_2 <= 0)
prob += (x2y3_rec_2 <= 0)
prob += (x3y3_rec_2 <= 0)
prob += (x4y3_rec_2 <= 0)
prob += (x0y4_rec_2 <= 0)
prob += (x1y4_rec_2 <= 0)
prob += (x2y4_rec_2 <= 0)
prob += (x3y4_rec_2 <= 0)
prob += (x4y4_rec_2 <= 0)
prob += (x0y5_rec_2 <= 0)
prob += (x1y5_rec_2 <= 0)
prob += (x2y5_rec_2 <= 0)
prob += (x3y5_rec_2 <= 0)
prob += (x4y5_rec_2 <= 0)
prob += (x0y6_rec_2 <= 0)
prob += (x1y6_rec_2 <= 0)
prob += (x2y6_rec_2 <= 0)
prob += (x3y6_rec_2 <= 0)
prob += (x4y6_rec_2 <= 0)
prob += (x0y7_rec_2 <= 0)
prob += (x1y7_rec_2 <= 0)
prob += (x2y7_rec_2 <= 0)
prob += (x3y7_rec_2 <= 0)
prob += (x4y7_rec_2 <= 0)
prob += (x0y8_rec_2 <= 0)
prob += (x1y8_rec_2 <= 0)
prob += (x2y8_rec_2 <= 0)
prob += (x3y8_rec_2 <= 0)
prob += (x4y8_rec_2 <= 0)
prob += (x0y9_rec_2 <= 0)
prob += (x1y9_rec_2 <= 0)
prob += (x2y9_rec_2 <= 0)
prob += (x3y9_rec_2 <= 0)
prob += (x4y9_rec_2 <= 0)

prob += (washington >= 100)
prob += (oregon >= 65)
prob += (california >= 100)
prob += (idaho >= 70)
prob += (nevada >= 120)
prob += (montana >= 60)
prob += (wyoming >= 75)
prob += (arizona >= 100)
prob += (utah >= 95)
prob += (colorado >= 85)

prob += (washington_min >= 3)
prob += (oregon_min >= 2)
prob += (california_min >= 3)
prob += (idaho_min >= 2)
prob += (nevada_min >= 3)
prob += (montana_min >= 2)
prob += (wyoming_min >= 2)
prob += (arizona_min >= 3)
prob += (utah_min >= 3)
prob += (colorado_min >= 3)

prob += (seattle <= 175)
prob += (francisco <= 175)
prob += (vegas <= 175)
prob += (phoenix <= 175)
prob += (denver <= 175)




# escrevendo o problema de otimização linear
print(prob)

# Resolvendo o problema
optimization_result = prob.solve()

# Verificando se a solução ótima foi encontrada
assert optimization_result == pulp.LpStatusOptimal

sumy0 = x0y0.value()*precos[0][0] + x1y0.value()*precos[1][0] + x2y0.value()*precos[2][0] + x3y0.value()*precos[3][0] + x4y0.value()*precos[4][0]
sumy1 = x0y1.value()*precos[0][1] + x1y1.value()*precos[1][1] + x2y1.value()*precos[2][1] + x3y1.value()*precos[3][1] + x4y1.value()*precos[4][1]
sumy2 = x0y2.value()*precos[0][2] + x1y2.value()*precos[1][2] + x2y2.value()*precos[2][2] + x3y2.value()*precos[3][2] + x4y2.value()*precos[4][2]
sumy3 = x0y3.value()*precos[0][3] + x1y3.value()*precos[1][3] + x2y3.value()*precos[2][3] + x3y3.value()*precos[3][3] + x4y3.value()*precos[4][3]
sumy4 = x0y4.value()*precos[0][4] + x1y4.value()*precos[1][4] + x2y4.value()*precos[2][4] + x3y4.value()*precos[3][4] + x4y4.value()*precos[4][4]
sumy5 = x0y5.value()*precos[0][5] + x1y5.value()*precos[1][5] + x2y5.value()*precos[2][5] + x3y5.value()*precos[3][5] + x4y5.value()*precos[4][5]
sumy6 = x0y6.value()*precos[0][6] + x1y6.value()*precos[1][6] + x2y6.value()*precos[2][6] + x3y6.value()*precos[3][6] + x4y6.value()*precos[4][6]
sumy7 = x0y7.value()*precos[0][7] + x1y7.value()*precos[1][7] + x2y7.value()*precos[2][7] + x3y7.value()*precos[3][7] + x4y7.value()*precos[4][7]
sumy8 = x0y8.value()*precos[0][8] + x1y8.value()*precos[1][8] + x2y8.value()*precos[2][8] + x3y8.value()*precos[3][8] + x4y8.value()*precos[4][8]
sumy9 = x0y9.value()*precos[0][9] + x1y9.value()*precos[1][9] + x2y9.value()*precos[2][9] + x3y9.value()*precos[3][9] + x4y9.value()*precos[4][9]



table = """
Distribuição        Washington   Oregon     California     Idaho      Nevada     Montana     Wyoming     Arizona       Utah     Colorado 
Seattle         {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f} 
San Francisco   {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f} 
Las Vegas       {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f} 
Phoenix         {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f} 
Denver          {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f} 
      Custos:   {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f}  {:10.0f} 
      Total: {:10.0f}

""".format(x0y0.value(), x0y1.value(), x0y2.value(), x0y3.value(), x0y4.value(), x0y5.value(), x0y6.value(), x0y7.value(), x0y8.value(), x0y9.value(), 
           x1y0.value(), x1y1.value(), x1y2.value(), x1y3.value(), x1y4.value(), x1y5.value(), x1y6.value(), x1y7.value(), x1y8.value(), x1y9.value(), 
           x2y0.value(), x2y1.value(), x2y2.value(), x2y3.value(), x2y4.value(), x2y5.value(), x2y6.value(), x2y7.value(), x2y8.value(), x2y9.value(), 
           x3y0.value(), x3y1.value(), x3y2.value(), x3y3.value(), x3y4.value(), x3y5.value(), x3y6.value(), x3y7.value(), x3y8.value(), x3y9.value(), 
           x4y0.value(), x4y1.value(), x4y2.value(), x4y3.value(), x4y4.value(), x4y5.value(), x4y6.value(), x4y7.value(), x4y8.value(), x4y9.value(),
           sumy0, sumy1, sumy2, sumy3, sumy4, sumy5, sumy6, sumy7, sumy8, sumy9, custo.value())

print(table)
