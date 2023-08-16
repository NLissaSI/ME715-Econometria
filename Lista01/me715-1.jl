import Pkg
Pkg.add("DelimitedFiles")
Pkg.add("DataFrames")
using Statistics
using DelimitedFiles
using DataFrames
homedir()
data = readdlm("econmath.csv", ',')
econmath = DataFrame(data[2:end, :], string.(data[1, :]))

data1 = readdlm("meap01.csv",',')
meap01 = DataFrame(data1[2:end, :], string.(data1[1, :]))

maximum(meap01[:, :math4])
minimum(meap01[:, :math4])

subset(meap01, :math4 => ByRow(==(50)))

mean(meap01[:, :math4])
mean(meap01[:, :read4])

cor(meap01[:, :math4]::AbstractVector, meap01[:, :read4]::AbstractVector)

mean(meap01[:, :exppp])
std(meap01[:, :exppp])

(6000/5500)*100
100*(log(6000)-log(5500))

econmath
econ1 = subset(econmath, :econhs => ByRow(==(1)))
mean(econ1[:, :score])
econ0 = subset(econmath, :econhs => ByRow(==(0)))
mean(econ0[:, :score])
