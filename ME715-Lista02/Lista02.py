pip install wooldridge

# Importando pacotes que serao usados
import wooldridge 
import statsmodels.formula.api as smf

# Banco de dados
df = wooldridge.data('bwght')

# Fazendo a regressao (regredindo `bwght` sobre `cigs`)
regressao = smf.ols(formula = 'bwght ~ cigs', data = df)
resultado = regressao.fit()

## a)
resultado.params
#Intercept    119.771900
#cigs          -0.513772
#dtype: float64

intercepto, cigarros = resultado.params

# Para `cigs` == 0
intercepto + cigarros * 20 # 119.77190039834969

# Para `cigs` == 20
intercepto + cigarros * 20 # 109.49645854188189
# Quando `cigs` for zero, o valor previsto pelo modelo foi 119.77 ounces. Quando `cigs` for 20, o valor previsto foi de 109.50 ounces.


## b)
# O Modelo de Regressão Linear Simples (MRLS) não necessariamente captura uma relação causal entre o peso no nascimento da criança e os 
# hábitos de fumar da mãe, pois pode haver outros fatores, além de fumar, que podem afetar o peso da criança.


## c)
(125 - intercepto) / cigarros # -10.175911994206903
# A magnitude de `cigs` deveria ser -10.18 para que o peso de nascimento fosse de 125 onças. Mas isso não é possível.


## d)
sum(df['cigs'] == 0) / df.shape[0] # Quantidade de mulheres que tem `cigs` == 0 / Numero total de mulheres no banco de dados
# 0.8472622478386167
