import tempfile
import os
from pathlib import Path

path = (Path(__file__).parent).joinpath(r'new') 

try:
    path.mkdir(parents=True, exist_ok=True)
except FileExistsError:
    pass

