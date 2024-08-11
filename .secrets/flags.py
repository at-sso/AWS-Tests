__all__ = ["flag_decrypt", "flag_hide", "flag_win"]

from argparse import ArgumentParser, Namespace


def parse_arguments() -> Namespace:
    parser = ArgumentParser(description="Handle decryption and configuration options.")

    # Add the `-d` or `-decrypt` argument
    parser.add_argument(
        "-decrypt",
        "-d",
        nargs="+",
        type=str,
        help="Decrypts the files directly.",
    )

    # Add the `-H` or `-hide` argument
    parser.add_argument(
        "-hide",
        "-H",
        action="store_true",
        help="Doesn't show the secret data in the terminal.",
    )

    # Add the `-w` or `-win` argument
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
flag_hide = __args.hide
"""Doesn't show the secret data in the terminal."""
flag_win = __args.win
"""Skips the winget operation."""

if flag_decrypt:
    print(f"Decrypting files with keys: {'[secret]' if flag_hide else flag_decrypt}")
# Handle the `-H` or `-hide` argument
if flag_hide:
    print("Hiding secret data from the terminal.")
# Handle the `-w` or `-win` argument
if flag_win:
    print("Skipping the winget operation.")
