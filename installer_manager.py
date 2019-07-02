from subprocess_manager import subprocess_call


def install_repository(repositories_list, install_repo_cmd):
    for item in repositories_list:
        subprocess_call(install_repo_cmd, item)


def install_dependencies(dependencies_list, install_dependencies_cmd):
    for item in dependencies_list:
        subprocess_call(install_dependencies_cmd, item)


def install_package(package_name, install_package_cmd):
    subprocess_call(install_package_cmd, package_name)


def execute_script(script_name, script_cmd):
    subprocess_call(script_cmd, script_name)