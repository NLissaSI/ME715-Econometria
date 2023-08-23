library(wooldridge)

htv = wooldridge::htv
head(htv)

# Modelo errado abil nao esta fixo
fit = lm(educ ~ motheduc + fatheduc + abil + I(abil^2), htv)
fit$coefficients #coef(lm(educ ~ motheduc + fatheduc + abil + I(abil^2), htv))
# se abil aumenta 1, educ aumenta 0.4015, mantendo os outros fatores fixos

# Para uma analise correta, devemos derivar o modelo com relacao ao abil assim temos que
fit$coefficients[4] + 2 * fit$coefficients[5]

# Ponto de inflexao
- fit$coefficients[5] / (2 * fit$coefficients[4])
