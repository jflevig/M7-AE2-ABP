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