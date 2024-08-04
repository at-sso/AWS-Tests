from typing import Dict, List
import pandas as pd
from pandas import DataFrame
import os

THIS_PATH: str = f"{os.path.abspath(".")}/.secrets/zperk@sso_".replace('\\', '/')


def main() -> int:
    # Load paths
    paths: Dict[str, str] = {
        "accessKeys": f"{THIS_PATH}accessKeys.csv",
        "credentials": f"{THIS_PATH}credentials.csv",
    }

    # Check if any of the paths exist
    path_exists: List[str] = [
        key for key, path in paths.items() if os.path.exists(path)
    ]

    # Check if paths exists.
    if path_exists:
        print(f"Loaded paths: {paths}\n")
    else:
        raise FileNotFoundError(f"Paths '{paths}', could not be found.")

    # Start operation

    def loader(row: str = "", abspath: str = "") -> DataFrame:
        if abspath == "":
            raise RuntimeError(f"{loader.__name__}: An absolute path was not set.")

        # Read the CSV file
        df: DataFrame = pd.read_csv(abspath)  # type: ignore[reportUnknownMemberType]
        # Mask the secret keys (assuming the column name is 'secret_key') <- chatgpt moment
        if row != "":
            df[row] = df[row].apply(  # type: ignore[reportUnknownMemberType]
                lambda x: "****" + x[-4:]  # type: ignore[reportUnknownLambdaType]
            )
        return df

    a: DataFrame = loader("Secret access key", paths["accessKeys"])
    b: DataFrame = loader("Password", paths["credentials"])

    print(a, '\n')
    print(b, '\n')

    return 0


if __name__ == "__main__":
    main()
