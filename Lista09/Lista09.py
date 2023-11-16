import pandas as pd

# Instalando o pacote `pyreadstat`
!pip install pyreadstat #--quiet
# Pacote para ler .dta
import pyreadstat

# Instalando o pacote `linearmodels`
!pip install linearmodels #--quiet
# Funcao para o modelo SUR
from linearmodels.system import SUR

# Leitura dos dados
df, meta = pyreadstat.read_dta('/content/hsb2.dta')
df

# Formula
formula = {"eq01": "read ~ 1 + female + pd.to_numeric(ses) + socst", 
           "eq02": "math ~ 1 + female + pd.to_numeric(ses) + science"}

# Metodo SUR
mod = SUR.from_formula(formula, df)

## Generalizes Least Squares (GLS)
mod.fit()

## Ordinary Least Squares (OLS)
mod.fit(method="ols")
