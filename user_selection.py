from pick import pick

def get_label(option):
    return option.get('label')

title = 'Please choose the programs you want to install (press SPACE to mark, ENTER to continue):'

options = [
    {'label': 'vim'},
    {'label': 'neovim'},
    {'label': 'vlc'},
    {'label': 'google-chrome'},
    {'label': 'spotify'},
    {'label': 'virtualbox'},
    {'label': 'weechat'},
    {'label': 'gimp'},
    {'label': 'touchpad-enable'}
]

def ask_user():
    return pick(options, title, multi_select=True, min_selection_count=1, options_map_func=get_label)