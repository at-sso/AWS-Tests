## Gestión de préstamos de libros con AWS Lambda

Este proyecto proporciona un backend simple basado en AWS Lambda para administrar registros de préstamos de usuarios y libros utilizando DynamoDB. La configuración incluye scripts bash para crear los recursos necesarios de AWS, implementar la función Lambda y probar la configuración.

## Estructura del proyecto

```
.
├── README.md
└── src
    ├── aws
    │   ├── create.sh          # Script para crear la tabla de DynamoDB
    │   ├── deploy.sh          # Script para implementar la función Lambda
    │   ├── test.sh            # Script para probar la función Lambda
    │   └── zip.sh             # Script para empaquetar la función Lambda
    ├── backend
    │   └── __init__.py        # Lógica del backend (código de la función Lambda)
    ├── frontend
    │   └── __init__.py        # Código frontend para interactuar con la función Lambda
    └── main.py                # Script principal para automatizar la configuración y la prueba
```

## Requisitos previos

1. **AWS CLI**: Asegúrate de tener AWS CLI instalado y configurado con los permisos necesarios.
2. **Python 3.x**: Necesario para ejecutar el script `main.py` y cualquier código Python en `frontend` y `backend`.
3. **Rol de IAM**: Crea un rol de IAM con las siguientes políticas:
      - `AWSLambdaBasicExecutionRole`
      - `AmazonDynamoDBFullAccess`
       Usa el ARN de este rol en el script de implementación.

## Configuración e implementación

Sigue estos pasos para configurar e implementar el proyecto:

### 1. Crear la tabla de DynamoDB

Navega al directorio del proyecto y ejecuta el script `create.sh` para crear la tabla de DynamoDB:

```bash
bash src/aws/create.sh
```

Esto creará una tabla `LoansTable` en DynamoDB con `user_id` y `book_id` como claves primarias.

### 2. Empaquetar la función Lambda

Ejecuta el script `zip.sh` para empaquetar la función Lambda:

```bash
bash src/aws/zip.sh
```

Esto creará un archivo `fn.zip` que contiene el código de la función Lambda.

### 3. Implementar la función Lambda

Implementa la función Lambda usando el script `deploy.sh`:

```bash
bash src/aws/deploy.sh <tu-identificador-de-cuenta> <tu-rol-de-ejecución-lambda>
```

Reemplaza `<tu-identificador-de-cuenta>` y `<tu-rol-de-ejecución-lambda>` con tu ID de cuenta de AWS real y el ARN del rol de IAM creado anteriormente.

### 4. Probar la función Lambda

Después de la implementación, puedes probar la función Lambda ejecutando el script `test.sh`:

```bash
bash src/aws/test.sh
```

Este script invoca la función Lambda con una carga de prueba e imprime la respuesta.

### 5. Ejecutar el script principal

Para automatizar todo el proceso de configuración y garantizar que todo funcione correctamente, ejecuta el script `main.py`:

```bash
python3 src/main.py
```

Este script ejecutará secuencialmente todos los scripts bash, manejará errores y probará la funcionalidad del frontend.

## Uso del frontend

El código frontend en `src/frontend/__init__.py` interactúa con la función Lambda. Personalízalo de acuerdo a tus necesidades y asegúrate de que invoque correctamente la función Lambda utilizando el SDK de AWS adecuado (por ejemplo, `boto3`).

## Notas

- Asegúrate de que tus credenciales de AWS estén configuradas correctamente antes de ejecutar estos scripts.
- Ajusta las políticas y roles de IAM según sea necesario para cumplir con tus requisitos de seguridad.

## Solución de problemas

- **Errores de Base64 no válida**: Asegúrate de que la carga enviada a la función Lambda tenga el formato correcto y que la función en sí no requiera codificación Base64 a menos que sea estrictamente necesario.
- **Problemas de permisos**: Comprueba dos veces que el rol de IAM adjunto a tu función Lambda tenga los permisos necesarios para acceder a DynamoDB y CloudWatch.
