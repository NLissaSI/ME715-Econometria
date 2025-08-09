#pip install wooldridge

# Importando pacotes que serao usados
import wooldridge 
import statsmodels.api as sm

# Banco de dados
df = wooldridge.data('htv')

# Separando as variaveis pra fazer a regressao (nao linear)
## Variaveis dependentes
y = df['educ']

## Variaveis independentes
X = df[['motheduc', 'fatheduc', 'abil']]
X['abil^2'] = X['abil']**2 ## Criando a coluna onde `abil` esta ao quadrado

# Fazendo a regressao
#regressao = sm.OLS(y, X) ## Sem constante (intercepto)
regressao = sm.OLS(y, sm.add_constant(X)) ## Com constante (intercepto)

resultado = regressao.fit()
resultado.summary()

# educ -> Maior grau de escolaridade ate o ano de 1991 (da pessoa)
# abil -> (abil.measure nao padronizado) eh uma medidia para a habilidade
#         manual de uma pessoa adulta com deficiencias nos membros superiores
# motheduc -> Maior grau de escolaridade, mae
# fatheduc -> Maior grau de escolaridade, pai
