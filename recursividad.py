
#imprime el valor que se encuentra en la posición n en la serie de fibonacci
def fibonacci(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#imprime la serie en forma de lista
def serieFibonacci(n):
    lista = [0,1];
    if n >= 2:   
        while(len(lista) < n):
            lista.append(lista[-1] + lista[-2])
    else:
        return [0]
    return lista
num = input("Ingresa el número de la posición hasta la cual quieres ver la serie de fibonacci: ")
print(f"El número que está en la posición {num} de la serie de fibonacci es: \n{fibonacci(int(num))}\nLa serie de fibonacci hasta la posición {num} es: \n{serieFibonacci(int(num))}") 
    
