### Lambdas ###

"""
Las lambdas son funciones anonimas, que significan que no necesitan un nombre
Tiene parametros de entradas.
- lambda params_one, params_two ... : params_one + params_two
- La podemos almacenar en una variable
"""

sum_two_values = lambda params_one, params_two: params_one + params_two
print(sum_two_values(2, 2))

multiply_values = lambda params_one, params_two: params_one * params_two - 3 
print(multiply_values(2, 4))

"""
Una función con lambda, le pasamos el parametro de la funcion y los parametros de lambda 
sum_values(2)(2,5)
"""
def sum_values(values):
    return lambda params_one, params_two: params_one + params_two + values

print(sum_values(2)(2,5))