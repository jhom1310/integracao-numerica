def f(x):
    return 1/x


def trapezio(x0,xn,n):

    h = (xn - x0) / n
    
    integration = f(x0) + f(xn)
    
    for i in range(1,n):
        k = x0 + i*h
        integration = integration + 2 * f(k)
    
    integration = integration * h/2
    
    return integration
    

lower_limit = float(input("Insira o limite inferior de integração: "))
upper_limit = float(input("Insira o limite superior de integração: "))
sub_interval = int(input("Insira o número de subintervalos: "))


result = trapezio(lower_limit, upper_limit, sub_interval)
print("Resultado pelo metodo dos trapezios: {:.5e}".format(result) )