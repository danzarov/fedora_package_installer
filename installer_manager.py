from subprocess_manager import subprocess_call


def install_repository(_repositories_list, _install_repo_cmd):
    for item in _repositories_list:
        subprocess_call(_install_repo_cmd, item)


def install_dependencies(_dependencies_list, _install_dependencies_cmd):
    for item in _dependencies_list:
        subprocess_call(_install_dependencies_cmd, item)


def install_package(_package_name, _install_package_cmd):
    subprocess_call(_install_package_cmd, _package_name)


def execute_script(_script_name, _script_cmd):
    subprocess_call(_script_cmd, _script_name)