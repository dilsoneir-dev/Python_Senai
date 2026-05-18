def dividir (a,b):
    r = 0
    try:
        r  = a / b
        return print(r)
    except ZeroDivisionError:
        print("Não é possível dividir por zero.")
    except:
        print("Erro inesperado.")
    finally:
        print("A função dividir foi executada.")    
        
dividir(10,5)