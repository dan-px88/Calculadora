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
            # Use the eval function to evaluate the expression
            # The eval function parses the expression passed to this method and executes Python expression(s) passed as a string
            result = eval(expression)
            
            # Print the result of the expression to the user
            print(f"Result: {result}")
        
        # Catch any ZeroDivisionError exceptions that occur during evaluation
        except ZeroDivisionError:
            # If a ZeroDivisionError occurs, print an error message to the user
            print("Error: Division by zero is not allowed")
        
        # Catch any SyntaxError exceptions that occur during evaluation
        except SyntaxError:
            # If a SyntaxError occurs, print an error message to the user
            print("Error: Invalid syntax. Please enter a valid mathematical expression")
        
        # Catch any other exceptions that occur during evaluation
        except Exception as e:
            # If any other exception occurs, print an error message to the user
            print(f"Error: {e}")

# Call the calculator function to start the program
calculator()