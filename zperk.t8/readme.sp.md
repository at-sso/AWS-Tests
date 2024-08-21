## Reconocimiento de imágenes con Amazon Rekognition

Este script Python utiliza el servicio Amazon Rekognition para analizar imágenes y recuperar etiquetas con puntajes de confianza.

## Características

- **Selección de imagen:** Seleccione imágenes a través de un cuadro de diálogo de archivos.
- **Integración con Amazon Rekognition:** Detecta etiquetas en imágenes usando la API Rekognition de Amazon.
- **Salida personalizable:** Vea una respuesta JSON simplificada o completa.
- **Manejo de errores:** Registra errores y proporciona valores predeterminados para datos faltantes.

## Requisitos previos

- Python 3.x instalado
- Boto3 instalado: `pip install boto3`
- Tkinter instalado: Generalmente se incluye con Python, pero asegúrese de que esté disponible.

## Configuración

1. Clone o descargue el proyecto.
2. Asegúrese de tener configuradas las credenciales de AWS necesarias para acceder a Rekognition.
3. Coloque los secretos requeridos en el directorio `.secrets` y ajuste las rutas según sea necesario.

## Uso

1. Ejecute el script:

   ```bash
   python3 ./zperk.t8/src/main.py -H -w
   ```

2. Seleccione una imagen del cuadro de diálogo.
3. Elija si desea ver la respuesta JSON completa o solo un resumen.

## Notas

- Este script funciona por defecto con imágenes ubicadas en [`./zperk.t8/src/img`](./src/img).
- Asegúrese de que sus credenciales de AWS tengan los permisos adecuados para usar Rekognition.
