#!/usr/bin/env python3
import os
import sys
import subprocess
from pathlib import Path

def main():
    script_dir = Path(__file__).parent.absolute()
    original_cwd = Path.cwd()
    os.chdir(script_dir)
    try:
        venv_path = script_dir / "myvenv"
        if os.name == 'nt':
            venv_python = venv_path / "Scripts" / "python"
        else:
            venv_python = venv_path / "bin" / "python"
        
        if not venv_python.exists():
            print("Setting up environment...")
            subprocess.run([sys.executable, "setup.py"])    

        if venv_python.exists():
            subprocess.run([str(venv_python), "qr_runner.py"])
        else:
            print("Setup failed. Please run setup.py manually.")
            sys.exit(1)
            
    finally:
        os.chdir(original_cwd)

if __name__ == "__main__":
    main()