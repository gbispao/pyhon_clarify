import matplotlib.pyplot as plt
import numpy as np

###############################
# Exemplo 1: Grafico de Linhas
###############################

# Dados para o grafico de linha
x = np.linspace(0, 10, 100) # 100 pontos entre 0 e 10
y = np.sin(x) # Função seno

# Criando o grafico de linha
plt.plot(x, y, label = "Seno(x)", color = 'b')

# Adicionando titulo e colunas
plt.title('Grafico de Linha: Seno(x)')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.legend()
plt.show()

###############################
# Exemplo 2: Grafico de Barras
###############################

categorias = ['A', 'B', 'C', 'D']
valores = [10,20,15,25]

plt.bar(categorias, valores, color = 'green')

plt.title('Grafico de Barras')
plt.xlabel('Categorias')
plt.ylabel('Valores')
plt.show()