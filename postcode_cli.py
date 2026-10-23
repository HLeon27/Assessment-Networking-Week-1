"""A CLI application for interacting with the Postcode API."""

from argparse import ArgumentParser
from postcode_functions import validate_postcode, get_postcode_completions

if __name__ == "__main__":
    parser = ArgumentParser(
        description="Let's you validate and complete a postcode.")
    parser.add_argument("--mode", "-m", choices=['validate', 'complete'], required=True,
                        help="Required argument mode")
    parser.add_argument("postcode", type=str,
                        help="Required argument postcode string.")
    arg = parser.parse_args()
    formatted_postcode = arg.postcode.rstrip().lstrip().upper()
    if arg.mode == "validate":
        if not validate_postcode(formatted_postcode):
            print(f"{formatted_postcode.upper()} is not a valid postcode.")
        else:
            print(f"{formatted_postcode} is a valid postcode.")

    elif arg.mode == "complete":
        if not validate_postcode(formatted_postcode) and len(formatted_postcode) > 5:
            print(f"No matches for {formatted_postcode}.")
        else:
            postcode_completions = get_postcode_completions(formatted_postcode)
            counter = 0
            for a_postcode in postcode_completions:
                if counter == 5:
                    break
                print(a_postcode)
                counter += 1
