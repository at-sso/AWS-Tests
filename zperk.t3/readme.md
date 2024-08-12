### S3 File Manager

1. **Set Up AWS Credentials**  
   Before running the script, ensure your AWS credentials are properly configured. You can do this by using the AWS CLI or setting environment variables. These credentials are essential for accessing your S3 bucket.

2. **Install Dependencies**  
   Install the required Python libraries by running:

   ```bash
   pip install -r ./env/requirements.txt
   ```

3. **Run the Script**  
   Execute the script to interact with your S3 bucket and local files:

   ```bash
   python3 ./zperk.t3/src/main.py -H -w
   ```

   - **Menu Options:**

     - **1**: Upload a file to S3.
     - **2**: Download a file from S3.
     - **3**: List all files in the S3 bucket.
     - **4**: Display the local file directory tree.
     - **5**: Delete all files in the S3 bucket.
     - **6**: Convert an image from the local download folder to ASCII art.
     - **0**: Exit the program.

   - **Note:** If your S3 credentials are incomplete or incorrect, you will see a prompt indicating the issue. Ensure your credentials are accurate before proceeding.

4. **Convert Images to ASCII Art**  
   After downloading an image from S3 or using an existing one in the local directory, select option **6** to convert it into ASCII art. The script will prompt you to enter the filename. The ASCII art will then be displayed in the terminal.

   - **Example:**
     ```text
     > 6
     Filename: locked_in.png
     (ASCII art of the image)
     ```

5. **Delete Files in S3**  
   Use option **5** to delete all files in your S3 bucket. This action is irreversible, so ensure you have backups of any important files before proceeding.
