import sys
import types
import importlib
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


pkg = sys.modules.get("praktikum")
if pkg is None:
    pkg = types.ModuleType("praktikum")
    pkg.__path__ = []
    sys.modules["praktikum"] = pkg

bun_mod = importlib.import_module("bun")
ingredient_mod = importlib.import_module("ingredient")
ingredient_types_mod = importlib.import_module("ingredient_types")


sys.modules.setdefault("praktikum.bun", bun_mod)
sys.modules.setdefault("praktikum.ingredient", ingredient_mod)
sys.modules.setdefault("praktikum.ingredient_types", ingredient_types_mod)


@pytest.fixture()
def burger_module():
    return importlib.import_module("burger")


@pytest.fixture()
def database_module():
    return importlib.import_module("database")
