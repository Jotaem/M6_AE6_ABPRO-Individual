# Plataforma de Gestión de Eventos

Este proyecto es una Plataforma de Gestión de Eventos desarrollada en Django como parte del ejercicio M6_AE5_ABPRO.

## Descripción

La plataforma permite a los usuarios registrarse y gestionar eventos como conferencias, conciertos y seminarios. Se implementa un sistema de autenticación y autorización para controlar el acceso a diferentes funcionalidades según el tipo de usuario.

## Características Principales

*   **Autenticación de Usuarios:** Sistema completo de registro, inicio de sesión y cierre de sesión.
*   **Gestión de Eventos:** Funcionalidades para crear, ver, editar y eliminar eventos.
*   **Roles y Permisos:** Tres tipos de usuarios con diferentes niveles de acceso:
    *   **Administradores:** Acceso total a todas las funcionalidades.
    *   **Organizadores de eventos:** Pueden crear y gestionar sus propios eventos, pero no eliminarlos.
    *   **Asistentes:** Pueden ver los eventos a los que están registrados.
*   **Acceso Restringido:** Uso de `LoginRequiredMixin` y `PermissionRequiredMixin` para proteger las vistas.
*   **Manejo de Errores:** Mensajes claros para acciones no permitidas y redirección en caso de acceso no autorizado.

## Configuración y Uso

1.  **Clonar el repositorio.**
2.  **Instalar las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Ejecutar las migraciones:**
    ```bash
    python manage.py migrate
    ```
4.  **Crear un superusuario (administrador):**
    ```bash
    python manage.py createsuperuser
    ```
5.  **Configurar los grupos y permisos iniciales:**
    ```bash
    python manage.py setup_groups
    ```
6.  **Iniciar el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```

## Rutas Importantes

*   `/login/`: Inicio de sesión.
*   `/logout/`: Cierre de sesión.
*   `/registro/`: Registro de nuevos usuarios.

## Configuración Adicional

El archivo `gestor_eventos/settings.py` contiene la configuración principal del proyecto, incluyendo:

*   `LOGIN_REDIRECT_URL = '/'`
*   `LOGOUT_REDIRECT_URL = '/'`

Esto asegura que los usuarios sean redirigidos a la página principal después de iniciar o cerrar sesión.
