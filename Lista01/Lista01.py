pip install wooldridge #instalando wooldridge no colab

import wooldridge # importando wooldridge

# Banco de dados
mic = wooldridge.data('meap01')
econ = wooldridge.data('econmath')

# q1
## a
micmax = mic['math4'].max()
micmin = mic['math4'].min()

micmax, micmin

## b
aprov_math = sum(mic['math4'] == 50)
aprov_math

## c
# Fazendo as medias
media_math = mic['math4'].mean()
media_read = mic['read4'].mean()

media_math, media_read

### O teste de leitura tem uma aprovacao mais dificil do que a de matematica. Visto que a media da taxa e aprovacao da leitura eh menor do que a de matematica.

## d
from scipy.stats import pearsonr # Funcao pra correlacao

mic_corr, _  = pearsonr(mic['math4'], mic['read4'])
mic_corr

## e
media_exppp = mic['exppp'].mean()
media_exppp

import statistics # conseguir o desvio padrao

sd_mic = statistics.stdev(mic['exppp'])
sd_mic

## f
import math

(6000/5500 - 1) * 100

#a diferença percentual aproximada baseada na diferença dos logaritmos.
100 * (math.log(6000) - math.log(5500))

# q2
## a
import pandas as pd

n = len(econ)
n

soma_econhs = sum(econ['econhs'] == 1)
soma_econhs

## b
# novos dataframes
econ_1 = econ.loc[econ['econhs'] == 1]
econ_0 = econ.loc[econ['econhs'] == 0]

econ_1['score'].mean(), econ_0['score'].mean()
