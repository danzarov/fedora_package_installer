import subprocess

def subprocess_call(command, item):
    print('DEBUGGING -> ', command + item)
    try:
        subprocess.check_output(command + item, stderr=subprocess.STDOUT, shell=True)
    except Exception as e:
        raise e