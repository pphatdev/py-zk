import subprocess
import os
import sys

CWD         = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR    = os.path.dirname(CWD)
sys.path.append(ROOT_DIR)
from src.database.helpers import defined_path, get_processor

subprocess.call(
    [
        get_processor(),
        "{}/src/test/db.py".format(defined_path())
    ],
    text = True
)