# setup_paths.py
import os
from pathlib import Path
import sys
from dotenv import load_dotenv

def setup_project_paths():
    """
    Dynamically detect project root, set key directories, ensure they exist,
    and return them as a dictionary.
    """
    # Load environment variables
    load_dotenv()

    # Try current working directory
    try:
        CURRENT_DIR = Path.cwd()
    except OSError:
        CURRENT_DIR = Path.home()

    # Detect project root dynamically
    if (CURRENT_DIR / "notebooks").exists() and (CURRENT_DIR / "data").exists():
        ROOT_DIR = CURRENT_DIR
    elif (CURRENT_DIR.name == "notebooks") and (CURRENT_DIR.parent / "data").exists():
        ROOT_DIR = CURRENT_DIR.parent
    else:
        # fallback to known project path, edit if necessary
        ROOT_DIR = Path("/Users/saniyaacharya/YouTube-Trending-Video-Analyzer")

    # Ensure writable
    try:
        os.chdir(ROOT_DIR)
    except PermissionError:
        ROOT_DIR = Path.home() / "YouTube-Trending-Video-Analyzer"
        ROOT_DIR.mkdir(parents=True, exist_ok=True)
        os.chdir(ROOT_DIR)

    # Add src/ to Python path
    SRC_DIR = ROOT_DIR / "src"
    if SRC_DIR.exists() and str(SRC_DIR) not in sys.path:
        sys.path.append(str(SRC_DIR))

    # Define key directories
    DATA_DIR = ROOT_DIR / "data"
    RAW_DIR = DATA_DIR / "raw"
    PROCESSED_DIR = DATA_DIR / "processed"
    NOTEBOOKS_DIR = ROOT_DIR / "notebooks"

    # Create directories if missing
    for folder in [DATA_DIR, RAW_DIR, PROCESSED_DIR]:
        folder.mkdir(parents=True, exist_ok=True)

    return {
        "ROOT_DIR": ROOT_DIR,
        "DATA_DIR": DATA_DIR,
        "RAW_DIR": RAW_DIR,
        "PROCESSED_DIR": PROCESSED_DIR,
        "NOTEBOOKS_DIR": NOTEBOOKS_DIR,
        "SRC_DIR": SRC_DIR
    }

# If executed directly, print paths for verification
if __name__ == "__main__":
    paths = setup_project_paths()
    for k, v in paths.items():
        print(f"{k}: {v}")
