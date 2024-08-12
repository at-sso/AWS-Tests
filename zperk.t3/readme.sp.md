### Gestor de Archivos S3

1. **Configura las Credenciales de AWS**  
   Antes de ejecutar el script, asegúrate de que tus credenciales de AWS estén configuradas correctamente. Puedes hacerlo utilizando la CLI de AWS o configurando variables de entorno. Estas credenciales son esenciales para acceder a tu bucket de S3.

2. **Instalar Dependencias**  
   Instala las bibliotecas de Python requeridas ejecutando:

   ```bash
   pip install -r ./env/requirements.txt
   ```

3. **Ejecutar el Script**  
   Ejecuta el script para interactuar con tu bucket de S3 y archivos locales:

   ```bash
   python3 ./zperk.t3/src/main.py -H -w
   ```

   - **Opciones del Menú:**

     - **1**: Subir un archivo a S3.
     - **2**: Descargar un archivo desde S3.
     - **3**: Listar todos los archivos en el bucket de S3.
     - **4**: Mostrar el árbol de directorios local.
     - **5**: Eliminar todos los archivos en el bucket de S3.
     - **6**: Convertir una imagen de la carpeta de descargas local a arte ASCII.
     - **0**: Salir del programa.

   - **Nota:** Si tus credenciales de S3 están incompletas o son incorrectas, verás un aviso indicando el problema. Asegúrate de que tus credenciales sean precisas antes de continuar.

4. **Convertir Imágenes a Arte ASCII**  
   Después de descargar una imagen de S3 o usar una existente en el directorio local, selecciona la opción **6** para convertirla en arte ASCII. El script te pedirá que ingreses el nombre del archivo. Luego, se mostrará el arte ASCII en la terminal.

   - **Ejemplo:**
     ```text
     > 6
     Nombre del archivo: ejemplo.jpg
     (Arte ASCII de la imagen)
     ```

5. **Eliminar Archivos en S3**  
   Utiliza la opción **5** para eliminar todos los archivos en tu bucket de S3. Esta acción es irreversible, así que asegúrate de tener copias de seguridad de cualquier archivo importante antes de continuar.
