import os
import sys
import subprocess

file_name = os.path.basename(__file__)
path = os.path.realpath(__file__)
real_path = path.split(file_name)[0]

subprocess.run([sys.executable, "-m", "venv", "myvenv"])
venv_pip = real_path + "myvenv/bin/pip" if os.name != 'nt' else "myvenv\\Scripts\\pip"
subprocess.run([venv_pip, "install", "-r", "requirements.txt"])

venv_python = real_path + "myvenv/bin/python" if os.name != 'nt' else "myvenv\\Scripts\\python"
subprocess.run([venv_python, "free_qr.py"])
