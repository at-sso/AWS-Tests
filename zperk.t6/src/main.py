# I ******* hate AWS man what a piece of **** service just use docker its way better than this ********
# Btw I'm not fixing this ****

import sys
import os
import subprocess
import frontend

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.secrets"))
)

from clownkey import this_path, dynamo_secret, lambda_id, lambda_role, LE_SECRETS, flag_secrets  # type: ignore


def run_script(script_name: str, *args: str, do_exit: bool = False) -> None:
    try:
        result = subprocess.run(
            f"{this_path}/zperk.t6/src/aws/{script_name} {' '.join(args)}",
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        print(result.stdout.decode())
    except subprocess.CalledProcessError as err:
        this_err: str = err.stderr.decode()
        print(
            f"Error running {script_name}"
            f"{args if not flag_secrets else f' {LE_SECRETS}'}:"
            f"\n{this_err if this_err else 'Unkown'}"
        )
        if do_exit:
            sys.exit(1)


def main() -> None:
    rpath: str = "zperk.t6/src/backend"
    print("Creating DynamoDB table...")
    run_script(
        "create.sh",
        dynamo_secret,
    )

    print("Zipping Lambda function...")
    run_script(
        "zip.sh",
        f"{this_path}/{rpath}",
        do_exit=True,
    )

    print("Deploying Lambda function...")
    lambda_execution_role: str = lambda_role
    zip_abspath: str = f"{this_path}/{rpath}/init.zip"
    run_script(
        "deploy.sh",
        lambda_id,
        lambda_execution_role,
        zip_abspath,
    )

    print("Testing Lambda function...")
    run_script(
        "test.sh",
        do_exit=True,
    )

    print("Testing frontend...")
    try:
        frontend.init()
    except Exception as err:
        print(str(err).replace(lambda_execution_role, LE_SECRETS))
        sys.exit(1)


if __name__ == "__main__":
    main()
