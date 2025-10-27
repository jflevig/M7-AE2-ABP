from productos.models import Producto

# Crear un producto con save
producto = Producto(
    nombre = "Desodorante",
    descripcion = "Olor chocolate",
    precio = 1000,
    stock = 10
)
producto.save()

# Crear un producto con método create
Producto.objects.create(
    nombre = "Shampoo de Mascota",
    descripcion = "Shampoo para perritos y gatitos",
    precio = 500,
    stock = 5
)

# Obtener solo un objeto con get
producto1 = Producto.objects.get(id=1)
print(producto1, producto1.descripcion, producto.precio, producto1.stock)

# Modificar un registro
producto1.precio = 989
producto1.save()

# Eliminar un registro
producto1.delete()

'''
Cynthia Castillo — 20:10
Usando tu ejercicio individual AE2 haz los siguientes retos
1.- Agrega a tu modelo de Productos el atributo disponible como BooleanField y valor por defecto True -> No olvides makemigrations y migrate
2.- Agrega al menos 5 productos más para poder trabajar mejor y que las consultas sean más claras e interactivas
3.- Recupera todos los registros de la tabla Producto.
4.- Con filtros, obtén todos los productos con precio mayor a 50
5.- Con filtros, obtén todos los productos cuyo nombre empiecen con la letra A
6.- Utilizando raw, obtén todos los productos con precio menor a 100
7.- Utilizando raw, obtén todos los productos con bajo stock (menos de 10 productos en stock)
8.- Crea un índice en el campo nombre del modelo Producto.
9.- Utilizando time.time(), Verifica el impacto en la eficiencia de búsqueda.
10.- Obtén todos los productos y excluye el campo de disponible
11.- Usa annotate() para calcular un campo adicional llamado precio_con_impuesto, donde el impuesto sea del 16%.
12.- Usando connection.cursor() agrégale al precio de todos los productos 5 pesos.
'''