from django.contrib import admin
from .models import Habitacion
from .models import Cliente
from .models import Productos
from .models import Post

admin.site.register(Habitacion)
admin.site.register(Cliente)
admin.site.register(Productos)
admin.site.register(Post)

# Register your models here.
