# Gestor de Clientes (CRM) 👥

Un sistema sencillo y eficiente para la gestión de clientes desarrollado en **Python**. Esta herramienta permite administrar una base de datos de contactos de forma local, ideal para pequeños negocios o proyectos personales que requieren un control organizado de su cartera de clientes.

## ✨ Características

* **Gestión de Datos**: Permite registrar, consultar, actualizar y eliminar información de clientes.
* **Base de Datos Local**: Utiliza **SQLite** (`crm.db`), lo que significa que no requiere una configuración compleja de servidores externos.
* **Interfaz Intuitiva**: Diseñado para ser ejecutado de forma sencilla desde el entorno de Python.
* **Persistencia Total**: Todos los cambios se guardan automáticamente en el archivo de base de datos incluido.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* **Base de Datos:** SQLite3 (Integrado en Python)

## 🚀 Instalación y Ejecucion

### 1. Requisitos Previos
Asegúrate de tener instalado Python en tu sistema. Puedes verificarlo con:
```
python --version
```
### 2. Utilizacion
Para utilizar este gestor en tu equipo local, sigue estos pasos:

  1. **Clonar el repositorio:**
     ```
     git clone https://github.com/EmaSanro/gestor-clientes.git
     ```
  2. **Ingresar a la carpeta:**
     ```
      cd gestor-clientes
     ```
  3. **Ejecutar el script**
     ```
      python gestor.py
     ```

## 📂 Estructura del Repositorio
El proyecto se compone de los siguientes elementos clave:

**gestor.py**: El script principal. Contiene toda la lógica de la aplicación, el menú de usuario y las sentencias SQL para interactuar con los datos.

**crm.db**: El archivo de base de datos. Es donde reside toda la información de tus clientes de manera estructurada.

## 📝 Notas de Uso
Al ejecutar el sistema, podrás gestionar los siguientes datos de tus clientes:
  - **Información Personal**: Nombres y apellidos completos.
  - **Contacto**: Teléfonos y direcciones de correo electrónico.
  - **Detalles Profesionales**: Nombre de la empresa y notas adicionales para un seguimiento personalizado.

## ✒️ Autor
Emanuel San Roman - Desarrollador del Proyecto - [Github Profile](https://github.com/EmaSanro)
