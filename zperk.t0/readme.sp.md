<!--BOOM!-->

### Cómo configurar la CLI de AWS

1. **Instalar AWS CLI:**
   - Descarga e instala la CLI de AWS desde [aquí](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
2. **Instalación en Windows:**
   - En Windows, instala la CLI de AWS usando este comando:
     ```sh
     msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi
     ```
   - Sigue el sentido común en el instalador de Windows.
     <img src="./img/cli.png" alt="cli" width="400"/>
3. **Crear una cuenta de AWS:**
   - Ve a [AWS](https://aws.amazon.com/) y crea una cuenta si no tienes una.
4. **Gestionar el acceso a los recursos de AWS (IAM):**
   - Después de crear tu cuenta, busca "Gestionar el acceso a los recursos de AWS" (IAM):
     <img src="./img/aws-iam.png" alt="aws-iam" width="400"/>
5. **Crear un usuario:**
   - En el panel de IAM, crea un nuevo usuario:
     <img src="./img/aws-user.png" alt="aws-user" width="400"/>
6. **Establecer permisos de usuario:**
   - Asigna los permisos apropiados al nuevo usuario:
     <img src="./img/aws-user-perms.png" alt="aws-user-perms" width="400"/>
7. **Agregar etiquetas (opcional):**
   - Agrega etiquetas al usuario si es necesario.
8. **Revisar el resumen del usuario:**
   - Revisa la información resumida del nuevo usuario:
     <img src="./img/aws-user-summ.png" alt="aws-user-summ" width="400"/>
9. **Configurar la CLI de AWS:**
   - Configura tu consola CLI de AWS usando las credenciales:
     <img src="./img/aws-secrets.png" alt="aws-secrets" width="400"/>
10. **Finalización:**
    - Tu CLI de AWS ahora está configurada.
    - Felicitaciones.
11. **Pruebas:**
    - Verifica una lista de instancias usando `aws ec2 list-instances`:
      <img src="./img/cli-instances.png" alt="cli-instances" width="400"/>
    - Prueba una instancia usando `aws ec2 describe-instances` y `aws ec2 describe-hosts`:
      <img src="./img/cli-instances-test.png" alt="cli-instances-test" width="400"/>
12. **Eso es todo:**
    - Felicitaciones de nuevo.
