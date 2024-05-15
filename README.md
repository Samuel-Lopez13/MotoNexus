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

### Paso 6

**Crear usuario**

```Bash Git
python manage.py createsuperuser
```

---

# Base de Datos MYSQL

**Inserta dato llamado Admin**

```Bash
INSERT INTO `auth_group` (`name`) VALUES ('Admin');
```
**Con el Id del usuario creado y del auto_group creado**

```Bash
INSERT INTO `svc_db`.`auth_user_groups` (`user_id`, `group_id`) VALUES ('idUser', idGroup');
```
