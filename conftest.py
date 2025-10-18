# Flexible import shim for both layouts:
# 1) Package: praktikum/ with __init__.py and submodules (burger.py etc.)
# 2) Root modules + praktikum.py file in root (no package)
import sys, os, importlib, types

HERE = os.path.abspath(os.path.dirname(__file__))
ROOT = os.path.abspath(os.path.join(HERE, os.pardir))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

def ensure_praktikum_package():
    """Ensure that `praktikum` behaves like a package exposing submodules
    (burger, bun, ingredient, ingredient_types, database) even if the project
    provides a single `praktikum.py` file or places modules at the root.
    """
    try:
        import praktikum as existing  # may be a module file or a package
    except ModuleNotFoundError:
        existing = None

    # Build a synthetic package that proxies to real submodules
    pkg = types.ModuleType("praktikum")
    pkg.__path__ = [ROOT]  # mark as package-like

    # Prefer submodules in package directory if it exists
    submods = ("burger", "bun", "ingredient", "ingredient_types", "database")
    for name in submods:
        # First, try praktikum/<name>.py
        mod = None
        pkg_dir = os.path.join(ROOT, "praktikum")
        candidate_pkg = os.path.join(pkg_dir, f"{name}.py")
        if os.path.isfile(candidate_pkg):
            mod = importlib.import_module(f"praktikum.{name}")
        else:
            # Then, try root-level <name>.py
            candidate_root = os.path.join(ROOT, f"{name}.py")
            if os.path.isfile(candidate_root):
                mod = importlib.import_module(name)
        if mod is not None:
            setattr(pkg, name, mod)
            sys.modules[f"praktikum.{name}"] = mod

    # If there is an existing `praktikum.py` file with attributes, keep it accessible
    if existing and getattr(existing, "__file__", "").endswith("praktikum.py"):
        # copy over attributes (non-dunder)
        for k, v in existing.__dict__.items():
            if not k.startswith("__") and not hasattr(pkg, k):
                setattr(pkg, k, v)

    # Replace/insert into sys.modules
    sys.modules["praktikum"] = pkg

ensure_praktikum_package()
