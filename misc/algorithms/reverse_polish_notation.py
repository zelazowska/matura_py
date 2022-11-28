"""program to calculate expressions using polish notation"""
import heapq

def rpn(expression):
    symbol = expression.split()
    OPERATORS = ["*", "+", "-", "/"] #possible operators in rpn
    heap = [] #initialize heap to add symbols to
    
    for individual_symbol in symbol:
        if individual_symbol in OPERATORS:
            a = int(heap.pop())
            b = int(heap.pop())
            if individual_symbol == "*":
                result = a*b
            elif individual_symbol == "/":
                result = a/b
            elif individual_symbol == "+":
                result = a+b
            elif individual_symbol == "-":
                result = a-b
            heap.append(result)
        else:
            heap.append(individual_symbol)
    return(heap.pop())
    
rpn_notation_expression = input("Enter a reverse polish notation expression you wish to calculate:")
print(rpn(rpn_notation_expression)) 

"""debug input
--------------
for input = 23 4 5 2 * 3 6 / + * +
result should be 71"""