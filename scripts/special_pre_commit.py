"""Pre-commit script."""
# pylint: disable=import-error,import-outside-toplevel

import logging
import os
import sys


def check_if_dependencies_are_right() -> bool:
    """Check if names in the commit."""
    # Load the requirements from setup.py and from requirements.txt

    from shortprint.requirements import REQUIREMENTS as real_requirements

    with open(
        os.path.join(os.path.dirname(__file__), "..", "requirements.txt"),
        "r",
        encoding="utf-8",
    ) as file:
        txt_requirements = list(filter(lambda x: len(x) > 0, file.read().split("\n")))
    if set(real_requirements) != set(txt_requirements):
        logging.warning(
            (
                "The requirements in the setup.py do not match the ones "
                "from the requirements.txt\n\n"
                "=== setup.py ===\n%s\n"
                "=== requirements.txt ===\n%s\n======"
            ),
            real_requirements,
            txt_requirements,
        )
        return True
    return False


sys.path.append(".")
sys.exit(int(check_if_dependencies_are_right()))
