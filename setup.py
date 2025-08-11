import os
import sys
import subprocess

subprocess.run([sys.executable, "-m", "venv", "myvenv"])
venv_pip = "myvenv/bin/pip" if os.name != 'nt' else "myvenv\\Scripts\\pip"
subprocess.run([venv_pip, "install", "-r", "requirements.txt"])

venv_python = "myvenv/bin/python" if os.name != 'nt' else "myvenv\\Scripts\\python"
subprocess.run([venv_python, "free_qr.py"])
