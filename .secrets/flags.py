__all__ = ["flag_decrypt", "flag_skip_decrypt", "flag_secrets", "flag_win"]

from argparse import ArgumentParser, Namespace


def parse_arguments() -> Namespace:
    parser = ArgumentParser(description="Handle decryption and configuration options.")

    # Useful if you are me and want to decrypt the files directly.
    parser.add_argument(
        "-decrypt",
        "-d",
        nargs="+",
        type=str,
        help="Decrypts the files directly.",
    )

    # Useful if you've already set your personal keys in 'clownkey'.
    parser.add_argument(
        "-skip_decrypt",
        "-D",
        action="store_true",
        help="Skips file decryption.",
    )

    # Censors all secret data in the terminal.
    parser.add_argument(
        "-hide",
        "-H",
        action="store_true",
        help="Doesn't show the secret data in the terminal.",
    )

    # Skips the winget operation on Windows.
    parser.add_argument(
        "-win",
        "-w",
        action="store_true",
        help="Skips the winget operation.",
    )

    return parser.parse_args()


__args: Namespace = parse_arguments()
flag_decrypt = __args.decrypt
"""Decrypts the files directly."""
flag_skip_decrypt = __args.skip_decrypt
"""Skips file decryption."""
flag_secrets = __args.hide
"""Doesn't show the secret data in the terminal."""
flag_win = __args.win
"""Skips the winget operation."""

if flag_decrypt and flag_skip_decrypt:
    raise SyntaxError("Do not combine '-decrypt' and '-skip_decrypt'.")
if flag_decrypt:
    a = "[secrets]" if flag_secrets else flag_decrypt
    print(f"Decrypting files with keys: {a}")
if flag_skip_decrypt:
    print("Skipping file decryption")
if flag_secrets:
    print("Hiding secret data from the terminal. Don't try to debug now!")
if flag_win:
    print("Skipping the winget operation.")
