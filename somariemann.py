import numpy as np

#f = lambda x: np.exp(-x)*np.sin(x)  
f = lambda x: x*x 
a = 1  
b = 2 
n = 4  
h = (b-a)/n  
x = np.linspace(a,b,n+1)  

print(x)
 
S_esq = 0  
S_dir = 0  
S_med = 0  
 
print("Soma de Riemman de {} a {} com {} intervalos:\n".format(a, b, n))  
 
for i in range(n):  
    S_esq += f(x[i])*h  
print("A esquerda: {:.5e}".format(S_esq))  
 
for i in range(n):  
    S_dir += f(x[i+1])*h  
print("A direita: {:.5e}".format(S_dir))  
 
for i in range(n):  
    S_med += f(((x[i]) + (x[i+1]))/2)*h  
print("Ponto medio: {:.5e}".format(S_med))