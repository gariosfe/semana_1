class Stack:
    def __init__(self):
        """Inicializa una pila vacía."""
        self.items = []

    def is_empty(self):
        """Verifica si la pila está vacía."""
        return len(self.items) == 0

    def push(self, item):
        """Inserta un elemento en la pila."""
        self.items.append(item)

    def pop(self):
        """Elimina y devuelve el elemento en la cima de la pila."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Devuelve el elemento en la cima de la pila sin eliminarlo."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        """Devuelve el número de elementos en la pila."""
        return len(self.items)

    def __str__(self):
        """Devuelve una representación en cadena de la pila."""
        return str(self.items)
def evaluate_postfix(expression):
    """Evalúa una expresión en notación postfija (RPN) usando una pila.
    
    Args:
        expression (str): La expresión en notación postfija.
        
    Returns:
        float: El resultado de la evaluación.
    """
    stack = Stack()
    operators = set(['+', '-', '*', '/'])

    for token in expression.split():
        if token.isdigit():
            # Si el token es un operando (número), lo empujamos en la pila
            stack.push(int(token))
        elif token in operators:
            # Si el token es un operador, sacamos los operandos necesarios de la pila
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            # Empujamos el resultado de la operación en la pila
            stack.push(result)
        else:
            raise ValueError(f"Unknown token: {token}")

    # El resultado final debe estar en la cima de la pila
    return stack.pop()

# Ejemplo de uso de la calculadora postfija
if __name__ == "__main__":
    expression = "3 4 + 2 * 7 /"
    result = evaluate_postfix(expression)
    print(f"El resultado de la expresión '{expression}' es: {result}")
