#Indicamos el directorio en el que vamos a trabajar
import os
os.chdir('C:/Users/lvallarta/Desktop/Deloitte/Personal/Maestria/1er Semestre/Programacion')

#Importamos los paquetes que vamos a necesitar 
import pandas as pd #Contiene funciones que nos ayudan en el análisis de datos
import matplotlib.pyplot as plt #Nota: Fue necesario instalar matplotlib 2 con conda install matplotlib=2
                                #y comentar la linea 4 del archivo _classic_test_patch.mplstyle

#Leemos el archivo a analizar
atletas = pd.read_csv('categorias de corredores.csv', index_col=0) #Con index_col=0 le indicamos que las filas tienen un nombre
atletas.info()

#Creamos una función que cree el histograma
import seaborn as sns
def crear_histograma(variable,j,z):
       plt.figure(j)
       sns.countplot(x=atletas[variable],color = z)
       plt.title(f"Gráfico de barras de  {variable}")
       plt.savefig(f"{variable}.jpg")
       plt.show()


variable=["Genero","Pais","Velocidad"]
color=["blue","yellow","green"]
j=1
z=0

for i in variable:
       crear_histograma(i,j,color[z])
       j +=1
       z +=1

#Para conocer la frecuencia de una variable que es categórica
import seaborn as sns
plt.figure(2)
sns.countplot(x=atletas['Velocidad'], palette = 'ocean')
plt.savefig("Velocidades.jpg")
#Si queremos saber las velocidades en hombres y en mujeres
plt.figure(3)
grafico3 = sns.countplot(x = 'Genero', hue = 'Velocidad', palette = 'hot_r', data = atletas)
grafico3.set(title = 'Velocidades por Género',
       xlabel = 'Género', ylabel = 'Total')
plt.title("Gráfico de Barras Genero")
plt.savefig("Genero.jpg")
plt.show()



