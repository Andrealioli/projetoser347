

def sazonalidade(file_location):
#Função que calcula o valor do angulo theta de cada ano de uma estação
    def theta(file_location):
        import pandas as pd
        import numpy as np
        #file_location = "C:\Ser347\Projeto\EXEMPLO_INDICE_SAZONALIDADE.xlsx"
        #Carregando a planilha excel
        xl = pd.ExcelFile(file_location)
        #trnasformando a planilha em um dataframe
        df1 = xl.parse('Plan1')
        df1.rename(columns={" Year": "year"}, inplace=True)
        #selecionando a coluna anos
        anos = [df1.loc[:]["year"]]

        #Transformando uma data em dia Juliano
        import datetime as dt
        data_flood = [df1.loc[:]['DATE_ACESS']]
        jd = [ts.dt.dayofyear for ts in data_flood]
        anos_bis = [ts.dt.is_leap_year for ts in data_flood]
    #Calculando o angulo theta
        angulo_theta = np.empty(shape=np.shape(jd))
        for j in range(0,len(angulo_theta[0][:]-1)):
            if anos_bis[0][j]==True:
                angulo_theta[0][j] = jd[0][j]*2*np.pi/366
            elif anos_bis[0][j] == False:
                angulo_theta[0][j] = jd[0][j] * 2 * np.pi / 365
        angulo_theta = angulo_theta[0][:]
        return(angulo_theta)

    # Função que calcula o valor de x
    def x (angulo_theta):
        import numpy as np
        import math
        costheta = [math.cos(i) for i in angulo_theta]
        xvalue= sum(costheta)/len(costheta)
        return(xvalue)

    # Função que calcula o valor de y
    def y (angulo_theta):
        import numpy as np
        import math
        sintheta = [math.sin(i) for i in angulo_theta]
        yvalue = sum(sintheta) / len(sintheta)
        return (yvalue)

    #Função que calcula o valor de r com base nos valores de x e y
    def r (x, y):
        import numpy as np
        import math
        rvalue = math.sqrt(x**2+y**2)
        return(rvalue)

    def angtheta(x, y):
        import math
        import numpy as np
        if x > 0 and y > 0:
            t = math.atan(y/x)
        elif x < 0:
            t = math.atan(y/x)+ math.pi
        elif x > 0 and y < 0:
            t = math.atan(y/x) + 2*math.pi
        elif x == 0 and y > 0:
            t = math.pi/2
        elif x == 0 and y < 0:
            t = (3*math.pi)/2
        elif x==0 and y==0:
            t = None
        return(t)
    def mdf(t):
        import math
        import numpy as np
        m = (t*365)/(2*math.pi)
        return(m)
    import numpy as np
    index = np.empty(5)
    index[0] = x(theta(file_location))
    index[1] = y(theta(filename))
    index[2] = r(index[0], index[1])
    index[3] = angtheta(index[0], index[1])
    index[4] = mdf(index[3])


    print("Valores [x, y, r, theta, mdf] ", index )
    return(index)

#Localização do arquivo de uma série temporal de uma determinada estação
filename = r"C:\Ser347\Projeto\EXEMPLO_INDICE_SAZONALIDADE.xlsx"
sazonalidade(filename)
#coisas que fizemos na reunião
import numpy as np
matriz = np.zeros((69,5), float)
for i in range(0, len(lista)-1):
    matriz[i]= sazonalidade(i)



#Função para plotar os dados
# # def plotagem ()
# # import numpy as np
# # import matplotlib.pyplot as plt
# #
# #
# # r = np.arange(0, 2, 0.01)
# # theta = 2 * np.pi * r
# #
# # ax = plt.subplot(111, projection='polar')
# # ax.plot(theta, r)
# # ax.set_rmax(2)
# # ax.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
# # ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
# # ax.grid(True)
# #
# # ax.set_title("A line plot on a polar axis", va='bottom')
# # plt.show()