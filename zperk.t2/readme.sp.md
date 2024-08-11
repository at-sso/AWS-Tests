## Cómo usar RDS

1. **Crear una base de datos Amazon RDS**

Sigue este [video tutorial](https://youtu.be/Ng_zi11N4_c) para crear una base de datos Amazon RDS. Asegúrate de seleccionar **MariaDB** en lugar de MySQL, como se requiere.

2. **Probar la conexión**

Ejecuta el [script de prueba](./src/rds_test.py) para verificar la conexión a la base de datos.

- **Nota:** Si necesitas desencriptar datos sensibles, necesitarás la frase de contraseña correcta. El script a continuación maneja el proceso de desencriptación:

```py
if input_passphrase:
  try:
    print("Nota: Se está usando la función `getpass`. La entrada SE está recibiendo.")
    __dot_secrets = __decrypt(input(".secrets: "), ".secrets")
    __access_keys = __decrypt(input("accessKeys: "), "accessKeys.gpg")
    __credentials = __decrypt(input("credentials: "), "credentials.gpg")
    with open(__dot_secrets, "r") as file:
      ...
  except Exception as e:
    print(f"Error de desencriptación: {e}")
    exit(1)
```

- Si **no eres yo**, puedes usar tus propias credenciales de AWS. Ten en cuenta que el código proporcionado está diseñado para funcionar con mis datos encriptados, por lo que es posible que necesites adaptarlo para tu propio uso.

3. **Administrar la base de datos de la librería**

Después de probar la conexión, ejecuta el [script principal](./src/main.py) para crear, ver y eliminar la base de datos de la librería.
