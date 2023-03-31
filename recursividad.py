def fibonacci(n):
    lista = [];
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def serieFibonnacci(n):
    lista = [0,1];
    if n >= 2:   
        while(len(lista) < n):
            lista.append(lista[len(lista)-1] + lista[len(lista) - 2])
    else:
        return [0]
    return lista

        
    
