def display_message(packages_list):
    for item, _ in packages_list:
        print('{0} is going to be installed.'.format(item['label']))