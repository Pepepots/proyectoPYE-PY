import pandas as pd

Tabla = pd.read_csv('bebidas.csv', index_col = 0)
numClientes = len(Tabla.index)

# Categorizacion edad:
# 0 es menor de edad
# 1 Adulto 
# 2 Mayor de edad 

for i in range(numClientes):
    if (Tabla.Edad[i] < 18):
        Tabla.Edad[i] = 0
    elif (Tabla.Edad[i] >= 18) & (Tabla.Edad[i] < 60):
        Tabla.Edad[i] = 1
    else:
        Tabla.Edad[i] = 2
        
# Categorizacion temperatura:
# 0 Frio
# 1 Templado
# 2 Calido

for i in range(numClientes):
    if (Tabla.Temperatura[i] <= 10):
        Tabla.Temperatura[i] = 0
    elif (Tabla.Temperatura[i] > 10) & (Tabla.Temperatura[i] < 20):
        Tabla.Temperatura[i] = 1
    else:
        Tabla.Temperatura[i] = 2

Tabla

prioriZ = [0,0]

for i in range(numClientes):
    prioriZ[Tabla.Bebida[i]] += 1
    
# print('Bebidas Frias: #',prioriZ[0])
# print('Bebidas Calientes: #',prioriZ[1])

for i in range(len(prioriZ)):
    prioriZ[i] /= numClientes
    
# print('')
# print('Distribucion de probabilidad de bebidas Frias: ', prioriZ[0])
# print('Distribucion de probabilidad de bebidas Calientes: ', prioriZ[1])

evidenciaXY = [[0,0,0],
               [0,0,0],
               [0,0,0]]

for i in range(numClientes):
    evidenciaXY[Tabla.Edad[i]][Tabla.Temperatura[i]] += 1
    
for i in range(3):
    for j in range(3):
        evidenciaXY[i][j] /= numClientes
        
distriXYZ = [[
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ],[
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]]

for i in range(numClientes):
    distriXYZ[Tabla.Bebida[i]][Tabla.Edad[i]][Tabla.Temperatura[i]] += 1


suma = 0
for i in range(2):
    for j in range(3):
        for k in range(3):
            distriXYZ[i][j][k] /= numClientes
            suma += distriXYZ[i][j][k]


tablaLikelihood = [[
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ],[
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]]

suma2 = 0
suma3 = 0
for i in range(2):
    for j in range(3):
        for k in range(3):
            tablaLikelihood[i][j][k] = distriXYZ[i][j][k]/prioriZ[i]


def bebida(edad, temperaturaDDia):
    if edad < 18:
        edad = 0
    elif edad >= 18 & edad < 60:
        edad = 1
    else:
        edad = 2
        

    if temperaturaDDia <= 10:
        temperaturaDDia = 0
    elif temperaturaDDia > 10 & temperaturaDDia < 20:
        temperaturaDDia = 1
    else:
        temperaturaDDia = 2

    probBebFria = (prioriZ[0]*tablaLikelihood[0][edad][temperaturaDDia])/evidenciaXY[edad][temperaturaDDia]
    probBebCaliente = (prioriZ[1]*tablaLikelihood[1][edad][temperaturaDDia])/evidenciaXY[edad][temperaturaDDia]

    if probBebFria > probBebCaliente:
        return 'fria'
    else:
        return 'caliente'