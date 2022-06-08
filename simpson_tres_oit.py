def func( x ):
    return 1/x

def simpsons38( ll, ul, n ):  
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
        elif i % 3 == 0:
            res+= 2 * fx[i]
        else:
            res+= 3 * fx[i]
        i+= 1
    res = res * (3 * h / 8)
    return res
        
lower_limit = float(input("Insira o limite inferior de integração: "))
upper_limit = float(input("Insira o limite superior de integração: "))
sub_interval = int(input("Insira o número de subintervalos: "))

if not (sub_interval%3) :
    result = simpsons38(lower_limit, upper_limit, sub_interval) 
    print("Resultado pelo metodo de 3/8 de Simpson: {}".format(result))
else:
    print("informe um subintervalo que seja multiplo de 3")