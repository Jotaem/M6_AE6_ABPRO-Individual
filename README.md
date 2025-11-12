# Proyecto Django: Plataforma de Gestión de Productos

Este proyecto es una plataforma de gestión de productos desarrollada con Django. Permite a los usuarios administrar un inventario de productos, con diferentes niveles de acceso y permisos para distintas operaciones (crear, editar, eliminar).

La interfaz de usuario está diseñada con Bootstrap y se inspira en el estilo visual de Mercado Libre para ofrecer una experiencia familiar y amigable.

## Características Principales

- **Gestión de Productos:** Funcionalidades completas de CRUD (Crear, Leer, Actualizar, Eliminar) para los productos.
- **Sistema de Autenticación:** Registro e inicio de sesión de usuarios.
- **Control de Acceso Basado en Roles:**
    - **Superusuario:** Acceso total al sitio administrativo de Django.
    - **Administradores:** Pueden gestionar productos (crear, editar, eliminar) y usuarios.
    - **Gestores de Productos:** Pueden agregar y modificar productos, pero no eliminarlos.
    - **Usuarios Normales:** Solo pueden ver la lista de productos.
- **Sitio Administrativo Personalizado:** El admin de Django está configurado para una gestión eficiente de productos, usuarios y grupos.
- **Interfaz Inspirada en Mercado Libre:** El frontend utiliza Bootstrap para crear una interfaz de usuario limpia y reconocible.

## Requerimientos Implementados

1.  **Creación de Superusuario:**
    - Se ha creado un superusuario con acceso completo al sitio administrativo (`/admin/`).

2.  **Modelo `Producto`:**
    - Se definió un modelo `Producto` con los campos: `nombre`, `descripción`, `precio`, `stock` y `fecha de creación`.
    - El modelo fue registrado en `admin.py` para su gestión a través del panel de administración.

3.  **Manejo de Usuarios y Grupos:**
    - Se crearon grupos ("Administradores", "Gestores de Productos") con permisos específicos.
    - Los usuarios de prueba fueron asignados a estos grupos para probar los distintos niveles de acceso.

4.  **Configuración de Permisos:**
    - Se configuraron permisos para que solo los administradores puedan eliminar productos.
    - Los usuarios sin los permisos adecuados son redirigidos a una página de "acceso denegado" si intentan realizar acciones no autorizadas.

5.  **Seguridad y Acceso:**
    - El acceso al sitio administrativo está restringido solo a personal autorizado (`is_staff`).
    - El sistema de autenticación maneja errores de inicio de sesión, mostrando mensajes claros al usuario.

## Cómo Empezar

1.  **Clona el repositorio:**
    ```bash
    git clone [M6_AE6_ABPRO-Individual](https://github.com/Jotaem/M6_AE6_ABPRO-Individual)
    cd M6_AE6_ABP_Individual
    ```

2.  **Crea y activa un entorno virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplica las migraciones:**
    ```bash
    python manage.py migrate
    ```

5.  **Crea un superusuario:**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Ejecuta los comandos para configurar grupos:**
    ```bash
    python manage.py setup_groups
    ```

7.  **Inicia el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```

8.  **Accede a la aplicación:**
    - **Sitio principal:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
    - **Sitio administrativo:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)