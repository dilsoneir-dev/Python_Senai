
import matplotlib.pyplot as plt

#criando os dados e plotando o gráfico
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Gráfico de Linha")
plt.show()

plt.bar(x, y, color='orange')
x = ["maçã", "banana", "laranja", "uva", "morango"]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Quantidade de Frutas - Gráfico de Linha")
plt.show()