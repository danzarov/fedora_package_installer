import json
from installer_manager import *
from user_interaction import display_message


def start(selected_packages):
    display_message(selected_packages)

    for item, index in selected_packages:
        package_file_name = f"{'packages'}/{item['label']}/{item['label']}.json"

        with open(package_file_name) as json_file:
            metadata = json.load(json_file)

        if metadata['repo'] != False:
            install_repository(metadata['repo'], metadata['install_repo_cmd'])

        if metadata['dependencies'] != False:
            install_dependencies(metadata['dependencies'], metadata['command'])

        if metadata['package'] != False:
            install_package(metadata['package'], metadata['command'])

        if metadata['script'] != False:
            execute_script(metadata['script'], metadata['command'])