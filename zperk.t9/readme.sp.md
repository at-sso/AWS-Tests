## Aplicación web para gestión de biblioteca en Docker

Este proyecto es una aplicación web basada en Flask diseñada para gestionar usuarios, libros y préstamos en una biblioteca. Incluye funcionalidades para agregar, actualizar, eliminar y visualizar estas entidades. La aplicación se puede ejecutar localmente utilizando Docker.

## Índice

- [Aplicación web para gestión de biblioteca en Docker](#aplicación-web-para-gestión-de-biblioteca-en-docker)
- [Índice](#índice)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Instalación](#instalación)
    - [Prerrequisitos](#prerrequisitos)
    - [Clonar el repositorio](#clonar-el-repositorio)
- [Ejecutar la aplicación](#ejecutar-la-aplicación)
    - [Usando Docker](#usando-docker)
- [Características](#características)

## Estructura del proyecto

```
.
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── templates/
│       ├── base.html
│       ├── books.html
│       ├── index.html
│       ├── loans.html
│       ├── update_book.html
│       ├── update_loan.html
│       ├── update_user.html
│       └── users.html
├── manage.py
├── Dockerfile
└── README.md
```

- **`./app/__init__.py`**: Inicializa la aplicación Flask y configura la base de datos.
- **`./app/models.py`**: Define los modelos de base de datos para usuarios, libros y préstamos.
- **`./app/routes.py`**: Contiene las rutas para gestionar usuarios, libros y préstamos.
- **`./templates/*`**: Contiene las plantillas HTML utilizadas por la aplicación.

## Instalación

### Prerrequisitos

- Tener Docker instalado en su máquina.

### Clonar el repositorio

```bash
git clone https://github.com/at-sso/AWS-Tests.git
cd AWS-Tests
```

## Ejecutar la aplicación

### Usando Docker

1. [**Construir la imagen de Docker:**](run.sh)

```bash
./zperk.t9/run.sh
```

2. **Acceder a la aplicación:**

Abra su navegador y navegue a `http://127.0.0.1:5000/` para acceder a la aplicación.

## Características

Puede encontrar la documentación completa [aquí](../zperk.t4/readme.md).
