### How to RDS

1. **Create an Amazon RDS Database**  
   Follow this [video tutorial](https://youtu.be/Ng_zi11N4_c) to create an Amazon RDS database. Make sure to select **MariaDB** instead of MySQL, as required.

2. **Test the Connection**  
   Run the [test script](./src/test.py) to verify the connection to the database.

   - **Note:** If you need to decrypt sensitive data, you'll need the correct passphrase. The script below handles the decryption process:
     ```py
     if input_passphrase:
         try:
             print("Note: `getpass` function is being used. Input IS being received.")
             __dot_secrets = __decrypt(input(".secrets: "), ".secrets")
             __access_keys = __decrypt(input("accessKeys: "), "accessKeys.gpg")
             __credentials = __decrypt(input("credentials: "), "credentials.gpg")
             with open(__dot_secrets, "r") as file:
                 ...
         except Exception as e:
             print(f"Decryption failed: {e}")
             exit(1)
     ```
   - If you're **not me**, you can use your own AWS credentials. Keep in mind that the provided code is designed to work with my encrypted data, so you may need to adapt it for your own use.

3. **Manage the Bookstore Database**  
   After testing the connection, run the [main script](./src/main.py) to create, view, and delete the bookstore database.
