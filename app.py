import json
from installer_manager import *


def start(_selected_packages):
    for item, index in _selected_packages:
        with open(item['label'] + '/' + item['label'] + '.json') as json_file:
            metadata = json.load(json_file)


        if metadata['repo'] != False:
            install_repository(metadata['repo'], metadata['install_repo_cmd'])

        if metadata['dependencies'] != False:
            install_dependencies(metadata['dependencies'], metadata['command'])

        if metadata['package'] != False:
            install_package(metadata['package'], metadata['command'])

        if metadata['script'] != False:
            execute_script(metadata['script'], metadata['command'])