###########################################
###  M7_AE5_ABP - Ejercicio Individual  ###
###########################################

from productos.models import Producto

Producto.objects.create(
    nombre = "Galletas McKay",
    descripcion = "Más ricas no hay",
    precio = 800,
    stock = 15,
    disponible = True,
)
Producto.objects.create(
    nombre = "Bilz y Pap",
    descripcion = "Yo quiero otro mundo",
    precio = "1200",
    stock = "10",
    disponible = True,
)
Producto.objects.create(
    nombre = "Red Bull",
    descripcion = "Te da Alas",
    precio = 1650,
    stock = 8,
    disponible = True,
)
Producto.objects.create(
    nombre = "De Todito",
    descripcion = "Mezcla de Papas Fritas, Cheetos y Ramitas",
    precio = 2500,
    stock = 13,
    disponible = True,
)
Producto.objects.create(
    nombre = "Platanos",
    descripcion = "Amarillo, amarillo los platanos",
    precio = 1000,
    stock = 9,
    disponible = True,
)

# 1.Recuperando Registros con Django ORM
# 1.2- Usa el ORM de Django para recuperar todos los registros de la tabla Producto.
productos = Producto.objects.all()

# 2. Aplicando Filtros en Recuperación de Resgistros
# 2.1- Con filtros, obtén todos los productos con precio mayor a 50 (lo haré mayor 1000)
productos.filter(precio__gt=1000)


# 2.2- Con filtros, obtén todos los productos cuyo nombre empiecen con la letra A (lo haré con las D)
productos.filter(nombre__istartswith="d")

# 2.3- Productos disponibles.
productos.filter(disponible=True)


# 3. Ejecutando Queries SQL desde Django
# 3.1- Utilizando raw, obtén todos los productos con precio menor a 100 (lo haré menos a 1000)
productos_raw = Producto.objects.raw("SELECT * FROM productos_producto WHERE precio < 1000")
for producto in productos_raw:
    print(producto.nombre)


# 4.- Utilizando raw, obtén todos los productos con bajo stock (menos de 10 productos en stock)
productos_bajo_stock = Producto.objects.raw("SELECT * FROM productos_producto WHERE stock < 10")
for producto in productos_bajo_stock:
    print(producto)


# 5.- Realizando Búsquedas de Índice
# 5.1- Los indices permiten optimizar consultas haciendo la aplicación más rápida
# 5.2- Se utiliza "db_index=True" en el campo "nombre" del modelo "Producto"
# 5.3- Consulta
productos_index = Producto.objects.filter(nombre__istartswith = 'de')
print(productos_index)


# 6. Exclusión de Campos del Modelo
# 6.1- Recupera todos los productos pero excluyendo el campo disponible
productos_sin_dispo = Producto.objects.defer('disponible').all()

# 6.2- Excluir campos hace las consultas más rápida al no cargar esa información. Sin embargo, si se quiere acceder a la información Django vuelve a realizar la consulta con el campo requerido.


# 7.- Añadiendo Anotaciones en Consultas
# 7.1- Usa annotate() para calcular un campo adicional llamado precio_con_impuesto, donde el impuesto sea del 16%.
from django.db.models import F, ExpressionWrapper, DecimalField
productos_con_impuesto = Producto.objects.annotate(precio_con_impuesto=ExpressionWrapper(F('precio')*1.16, output_field=DecimalField(max_digits=10, decimal_places=2)))

for producto in productos_con_impuesto:
    print(f'{producto.nombre}: Precio: ${producto.precio} - Precio con Impuesto: ${producto.precio_con_impuesto}')

# 8.- Pasando Parámetros a raw()
# 8.1- Ejecuta una consulta con raw(), pero esta vez utilizando parámetros en lugar de valores fijos.
productos_raw = Producto.objects.raw("SELECT * FROM productos_producto WHERE precio < %s", [1000])

# 8.2- La diferencia de usar parámetros es que los valores en que se realizan las consultas en SQL no se indican directamente. El beneficio es que mejora la seguridad, previniendo la inyección de SQL. Permite la reutilización de consultas con distintos valores y transforma los datos a los tipos adecuados automáticamente.


# 9.- Ejecutado SQL Personalizado Directamente
# 9.1- Usa connection.cursor() para ejecutar un SQL INSERT, UPDATE o DELETE directamente en la base de datos.
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute('DELETE FROM productos_producto WHERE nombre="Platanos"')

#9.2- En general se recomienda utilizar las herramientas del ORM de Django, sin embargo, hay excepciones para consultas demasiado complejas, utilización de procedimientos almacenados y ocaciones de base de datos muy grandes en que el rendimiento es claramente superior al uso del ORM.


#10.- Lo mismo que 9.