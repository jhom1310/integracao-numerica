def func( x ):
    return 1/x

def simpsons13( ll, ul, n ):  
    h = ( ul - ll )/n

    x = list()
    fx = list()
     
    i = 0
    while i<= n:
        x.append(ll + i * h)
        fx.append(func(x[i]))
        i += 1
 
    # Calculating result
    res = 0
    i = 0
    while i<= n:
        if i == 0 or i == n:
            res+= fx[i]
        elif i % 2 != 0:
            res+= 4 * fx[i]
        else:
            res+= 2 * fx[i]
        i+= 1
    res = res * (h / 3)
    return res
    

lower_limit = float(input("Insira o limite inferior de integração: "))
upper_limit = float(input("Insira o limite superior de integração: "))
sub_interval = int(input("Insira o número de subintervalos: "))

if(sub_interval%2)==0:
    result = simpsons13(lower_limit, upper_limit, sub_interval)
    print("Resultado pelo metodo de 1/3 de Simpson: {}".format(result))
else:
    print("informe um subintervalo que seja multiplo de 2")