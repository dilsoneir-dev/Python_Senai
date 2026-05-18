import numpy as np

# Criando um array de 1 dimensão
arr1d = np.array([10, 20, 30, 40, 50])
# 0 - 10 - coluna A no Excel
# 1 - 20 - coluna B no Excel
# 2 - 30 - coluna C no Excel
# 3 - 40 - coluna D no Excel
# 4 - 50 - coluna E no Excel

print("Array 1D:")
print(arr1d) 
print(arr1d[2]) # Acessando o elemento na posição 2 (30)

# Criando um array de 2 dimensões
arr2d = np.array(
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]])

print("Array 2D:")
print(arr2d) 
print(arr2d[1, 2]) # Acessando o elemento na linha 1, coluna 2 (6)

print(f"Shape da matriz: {arr2d.shape}")
print(f"Número de dimensões: {arr2d.ndim}")
print(f"Tipo de dados: {arr2d.dtype}")
print(f"Tamanho total do array: {arr2d.size}")
print(f"Memória ocupada por elemento: {arr2d.itemsize} bytes")

# quando colca um array dentro de outro array, o primeiro é a linha e o segundo é a coluna
# quando coloca uma variável para imprimir, o f é para formatar a string, e o {} é para colocar a variável dentro da string

arr1 = np.array([10, 20, 30, 40, 50])

print("Array 1D:")
print(arr1)
print(arr1+10)
print(arr1*2)
print(arr1/2)

arr2 = np.array([10, 20, 30, 40, 50])
print(arr2)
print("Média:")
print(np.mean(arr2))
print("Mediana:")
print(np.median(arr2))
print("desvio padrão:")
print(np.std(arr2))
print("Variância:")
print(np.var(arr2))

print("Mínimo:")
print(np.min(arr2))
print("Máximo:")        
print(np.max(arr2))    
