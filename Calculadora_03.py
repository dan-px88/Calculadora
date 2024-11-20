# Definimos una función llamada calculadora, que es la que contiene el programa
def calculator():
    # Ps por si el usuario no se ha dado cuenta, es una calculadora (En inglés, pq Bilingue)
    print("Simple Calculator")
    
    # Tutorial de como usar una calculadora 
    print("Enter a mathematical expression (e.g., 2+3*4, 10/2-3, etc.)")

    # Se hace un loop para que el usuario siga metiendole numeros, hasta que el usuario quiera parar
    while True:
        # Aquí se le mete la expresion
        expression = input("Enter your expression (or 'q' to quit): ")

        # Checa que el usuario ya quiere parar (Se utiliza lower para convertir la letra en miuscula)
        if expression.lower() == 'q':
            # Si el usuario quiere parar se rompe el ciclo, y se termina el programa
            break 

        # Aquí se evalua el input del usuario como expresion matematica
        try:
            # Se utiliza la función eval para evaluar la expresion
            result = eval(expression)
            
            # Se muestra el resultado de la expresión al usuario
            print(f"Result: {result}")
        
        # Detecta cualquier ZeroDivisionError exceptions que pueda llegar a ocurrir
        except ZeroDivisionError:
            # si un ZeroDivisionError ocurre, se le manda un aviso al usuario
            print("Error: Division by zero is not allowed")
        
        # Detecta cualquier SyntaxError exceptions que pueda llegar a ocurrir 
        except SyntaxError:
            # si un SyntaxError ocurre, ps igual se le avisa al usuario
            print("Error: Invalid syntax. Please enter a valid mathematical expression")
        
        # Detecta cualquier error que pueda llegar a ocurrir
        except Exception as e:
            # Cualquier otro error que pueda llegar a presentarse se le manda un mensaje 
            print(f"Error: {e}")

# Aquí se llama la funcion de la calculadora para que ya se pueda ejecutar el programa
calculator()
