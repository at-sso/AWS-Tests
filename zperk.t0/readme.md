<!--BOOM!-->

### How to Configure the AWS CLI

1. **Install AWS CLI:**
   - Download and install the AWS CLI from [here](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
2. **Windows Installation:**
   - On Windows, install the AWS CLI using this command:
     ```sh
     msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi
     ```
   - Follow common sense in the Windows installer.
     <img src="./img/cli.png" alt="cli" width="400"/>
3. **Create an AWS Account:**
   - Go to [AWS](https://aws.amazon.com/) and create an account if you don't have one.
4. **Manage Access to AWS Resources (IAM):**
   - After creating your account, search for "Manage access to AWS resources" (IAM):
     <img src="./img/aws-iam.png" alt="aws-iam" width="400"/>
5. **Create a User:**
   - In the IAM dashboard, create a new user:
     <img src="./img/aws-user.png" alt="aws-user" width="400"/>
6. **Set User Permissions:**
   - Assign appropriate permissions to the new user:
     <img src="./img/aws-user-perms.png" alt="aws-user-perms" width="400"/>
7. **Add Tags (Optional):**
   - Add tags to the user if needed.
8. **Review User Summary:**
   - Review the summary information for the new user:
     <img src="./img/aws-user-summ.png" alt="aws-user-summ" width="400"/>
9. **Configure AWS CLI:**
   - Configure your AWS CLI console using the credentials:
     <img src="./img/aws-secrets.png" alt="aws-secrets" width="400"/>
10. **Completion:**
    - Your AWS CLI is now configured.
    - Congrats.
11. **Tests:**
    - Check a lists of instances using `aws ec2 list-instances`:
      <img src="./img/cli-instances.png" alt="cli-instances" width="400"/>
    - Test an instance using `aws ec2 describe-instances` and `aws ec2 describe-hosts`:
      <img src="./img/cli-instances-test.png" alt="cli-instances-test" width="400"/>
12. **That's it:**
    - Congrats again.
