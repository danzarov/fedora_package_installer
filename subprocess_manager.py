import subprocess

def subprocess_call(command, item):
    subprocess.check_output(command + item, stderr=subprocess.STDOUT, shell=True)

