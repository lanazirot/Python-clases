"""
    Una pizzeria ofrece pizzas vegetarianas y no vegetarianas a sus clientes
    Los ingredientes para cada tipo de pizza aparecen a continuacion
    Ingredientes vegetarianas: pimiento y tofu
    Ingredientes no vegetarianos: peperoni, jamon, salmon
    
    Escribir un programa que pregunte al usuario si quiere una vegetariana o no
    en base a su respuesta le muestre el menu con los ingredientes disponibles
    Solo se puede elegir 1 ingrediente, ademas del ingrediente seleccionado por defecto
    la mozarella y el tomate estan en todas las pizzas. Al final debe mostrar todos
    los ingredientes de la pizza
"""

ingredientesPizzaVegetariana = ['Pimiento','Tofu']
ingredientesPizzaNoVegetariana = ['Peperoni', 'Jamon', 'Salmon']
tipoPiza = int(input('Selecciona el tipo de pizza:\n1. Vegetariana\n2. Normal\n'))
ingredienteSeleccionado = -1
tipoPiza = ''
listaIngredientes = []

if tipoPiza == 1:
    listaIngredientes.extend(ingredientesPizzaVegetariana)
    tipoPiza = 'Vegetariana'
    print('Los ingredientes son: {ingredientesPizzaVegetariana}\nSelecciona un ingrediente: ')
    seleccionado = input('Selecciona un ingrediente: \n')
else:
    listaIngredientes.extend(ingredientesPizzaNoVegetariana)
    tipoPiza = 'Normal'
    print(f'Los ingredientes son: {ingredientesPizzaNoVegetariana}\nSelecciona un ingrediente: ')

listaIngredientes.append(seleccionado)

print(f'La pizza que escogiste es de {tipoPiza}. Estos son sus ingredientes: \n')
for ingrediente in listaIngredientes:
    print(ingrediente)
    


    

