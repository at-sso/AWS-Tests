# Chatbot para la Librería

Esta aplicación de Python interactúa con un bot de Amazon Lex y una función de AWS Lambda para proporcionar un chatbot funcional para el equipo interno de una librería. El chatbot permite a los usuarios registrar nuevos usuarios y editar usuarios existentes a través de comandos conversacionales simples.

## Tabla de Contenidos

- [Chatbot para la Librería](#chatbot-para-la-librería)
  - [Tabla de Contenidos](#tabla-de-contenidos)
  - [Visión General](#visión-general)
  - [Arquitectura](#arquitectura)
  - [Instrucciones de Configuración](#instrucciones-de-configuración)
    - [Requisitos Previos](#requisitos-previos)
    - [Configuración del Bot de Amazon Lex](#configuración-del-bot-de-amazon-lex)
    - [Configuración de la Función AWS Lambda](#configuración-de-la-función-aws-lambda)
  - [Cómo Funciona](#cómo-funciona)
  - [Ejecutando la Aplicación](#ejecutando-la-aplicación)
  - [Servicios de AWS](#servicios-de-aws)
    - [Amazon Lex](#amazon-lex)
    - [AWS Lambda](#aws-lambda)
  - [Consideraciones Importantes](#consideraciones-importantes)

## Visión General

La aplicación está diseñada para interactuar con un bot de Amazon Lex, que procesa la entrada de lenguaje natural de los usuarios. El bot maneja dos intenciones principales: registrar un nuevo usuario y editar los detalles de un usuario existente. Cuando se activan estas intenciones, el bot de Lex se comunica con una función de AWS Lambda que procesa la lógica para la gestión de usuarios.

## Arquitectura

1. **Entrada del Usuario**: El usuario interactúa con el chatbot a través de la interfaz de línea de comandos (CLI) de Python.
2. **Amazon Lex**: La aplicación de Python envía la entrada del usuario a un bot de Amazon Lex utilizando la biblioteca `boto3`.
3. **AWS Lambda**: Dependiendo de la intención del usuario (por ejemplo, RegisterUserIntent, EditUserIntent), el bot de Lex activa una función de AWS Lambda. Esta función Lambda realiza las acciones necesarias, como registrar o editar un usuario.
4. **Respuesta**: La función Lambda envía una respuesta de vuelta al bot de Lex, que luego se devuelve al usuario a través de la aplicación de Python.

## Instrucciones de Configuración

### Requisitos Previos

- **Cuenta de AWS**: Asegúrate de tener una cuenta de AWS.
- **AWS CLI**: Configura AWS CLI en tu máquina local y configúralo con tus credenciales.
- **Python**: Asegúrate de que Python 3.x esté instalado en tu máquina.
- **Boto3**: Instala el SDK de AWS para Python (Boto3) utilizando el comando:

  ```bash
  pip install boto3
  ```

### Configuración del Bot de Amazon Lex

1. **Crear Intenciones**: Define las intenciones `RegisterUserIntent` y `EditUserIntent` en Amazon Lex. Estas intenciones deben tener ranuras para capturar información del usuario como nombre de usuario y correo electrónico.
2. **Crear el Bot**: Crea el bot de Lex e incluye las intenciones que has definido.
3. **Configurar la Realización**: Para ambas intenciones, configura un CodeHook que active una función de AWS Lambda para el procesamiento.

### Configuración de la Función AWS Lambda

1. **Crear una Función Lambda**: En AWS Lambda, crea una nueva función que maneje la lógica para el registro y la edición de usuarios.
2. **Código de Lambda**: Utiliza el código de la función Lambda proporcionado para procesar los eventos enviados por Lex. Esta función debe tomar datos de usuario de Lex, realizar la operación requerida (por ejemplo, almacenar en una base de datos) y devolver una respuesta.
3. **Rol IAM**: Asegúrate de que la función Lambda tenga el rol IAM necesario para interactuar con otros servicios de AWS si es necesario.

## Cómo Funciona

1. **Interacción del Usuario**: El usuario escribe un mensaje en la CLI de Python, como "Registrar un usuario con el nombre John y correo john@example.com".
2. **Procesamiento del Bot de Lex**: El mensaje se envía al bot de Amazon Lex utilizando el método `post_text` del cliente `lex-runtime` de Boto3. Lex procesa la entrada en función de las intenciones predefinidas.
3. **Manejo de Intenciones**: Si la entrada coincide con una intención, Lex activa la función Lambda asociada.
4. **Ejecución de Lambda**: La función Lambda procesa la entrada, realiza las operaciones necesarias (por ejemplo, almacenar el usuario en una base de datos) y devuelve un resultado.
5. **Entrega de la Respuesta**: Lex envía la respuesta de la función Lambda de vuelta a la aplicación de Python, que se muestra al usuario.

## Ejecutando la Aplicación

1. Clona el repositorio que contiene el script de Python.
2. Abre una terminal y navega al directorio que contiene el script.
3. Ejecuta el script:

   ```bash
   python chatbot.py
   ```

4. Sigue las instrucciones en pantalla para interactuar con el chatbot.

## Servicios de AWS

### Amazon Lex

Amazon Lex es un servicio para construir interfaces conversacionales utilizando voz y texto. En esta aplicación, Lex es responsable de interpretar la entrada del usuario y determinar la intención correcta a ejecutar (registrar o editar un usuario).

- **Intenciones**: Las intenciones son objetivos predefinidos que el usuario puede lograr interactuando con el bot. Cada intención está asociada con solicitudes específicas del usuario.
- **Ranuras**: Las ranuras se utilizan para capturar piezas específicas de información del usuario, como nombres de usuario o direcciones de correo electrónico.

### AWS Lambda

AWS Lambda es un servicio de computación sin servidor que te permite ejecutar código sin aprovisionar o gestionar servidores. En esta aplicación, las funciones Lambda se utilizan para manejar la lógica de registro y edición de usuarios cuando son activadas por el bot de Lex.

- **CodeHook**: Una función Lambda está conectada a Lex utilizando un CodeHook, que se activa cuando Lex determina que una intención debe ser realizada.

## Consideraciones Importantes

- **Seguridad**: Asegúrate de que los roles y permisos de IAM estén configurados correctamente para proteger tus recursos de AWS.
- **Manejo de Errores**: Considera agregar un manejo de errores más robusto tanto en la función Lambda como en la aplicación de Python.
- **Escalabilidad**: La aplicación puede escalarse integrando más intenciones y mejorando la lógica dentro de las funciones Lambda.
