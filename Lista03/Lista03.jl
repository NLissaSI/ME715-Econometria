using WooldridgeDatasets, DataFrames, GLM

df = DataFrame(wooldridge("HTV"));

modelo = lm(@formula(educ~motheduc + fatheduc + abil + abil^2), df)

parametros = coef(modelo)

B3 = parametros[4]
B4 = parametros[5]

Delta_y = B3 + 2*B4

ponto_inf = -B4 / (2*B3)

#mantendo as outras variaveis constantes, de abil = 0 para abil = 1, educ aumenta B3
#mantendo as outras variaveis constantes, de abil = 1 para abil = x, educ aumenta (Delta_y)*(x-1)
#mantendo as outras variaveis constantes, motheduc aumentando uma unidade, educ aumenta B1
#mantendo as outras variaveis constantes, fatheduc aumentando uma unidade, educ aumenta B2
