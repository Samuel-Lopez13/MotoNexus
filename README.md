# MotoNexus

Software de control de inventario y carrito de compras

### Paso 1

**Clonar el proyecto**

```Bash Git
git clone https://github.com/Samuel-Lopez13/MotoNexus.git
```

### Paso 2

**Montar en .venv**

```Bash Git
python3.12 -m venv .venv
```

Si se prestenta algun conflicto sobre la politica de ejecucion ejecutar el comando

```Bash Git
Set-ExecutionPolicy Unrestricted -Scope Process
```

Si todo bien ejecutr el siguiente comando

```Bash Git
.venv\Scripts\Activate
```

### Paso 3

**Generar documento de requerimientos**

```Bash Git
pip freeze > requerimientos.txt
```

### Paso 4

**Instalar requerimientos**

```Bash Git
pip install -r requerimientos.txt
```

### Paso 5

**Instalar dependencias que no se aplicaron**

- pip install mysqlclient
- pip install crispy-bootstrap5
- pip install django-cloudinary-storage
- pip install django-crispy-forms  
