import Pkg
Pkg.add("WooldridgeDatasets") 
Pkg.add("GLM")

using DataFrames
using WooldridgeDatasets
using GLM

df = DataFrame(wooldridge("bwght"))

regressao = lm(@formula(bwght ~ cigs), df)

# a)
resultados = coef(regressao) # [Intercepto, beta1]

## Para cigs == 0
resultados[1] + resultados[2] * 0 # 119.77
## Para cigs == 20
resultados[1] + resultados[2] * 20 # 109.50

# b)
## O Modelo de Regressão Linear Simples (MRLS) não necessariamente captura uma relação causal entre o peso no nascimento da criança e os 
## hábitos de fumar da mãe, pois pode haver outros fatores, além de fumar, que podem afetar o peso da criança.


# c)
(125 - resultados[1]) / resultados[2] # -10.175911994206903
# A magnitude de `cigs` deveria ser -10.18 para que o peso de nascimento fosse de 125 onças. Mas isso não é possível.


# d)
nrow(subset(df, :cigs => ByRow(==(1)))) / nrow(df) # `subset` eh mais novo do que `filter`

nrow(filter(:cigs => c -> c == 0, df)) / nrow(df)