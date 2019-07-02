from pick import pick

def get_label(option):
    return option.get('label')

title = 'Please choose the programs you want to install (press SPACE to mark, ENTER to continue):'

options = [
    {'label': 'adobe-flash-plugin'},
    {'label': 'ffmpeg'},
    {'label': 'gimp'},
    {'label': 'google-chrome'},
    {'label': 'neovim'},
    {'label': 'simplescreenrecorder'},
    {'label': 'spotify'},
    {'label': 'touchpad-enable'},
    {'label': 'vim'},
    {'label': 'virtualbox'},
    {'label': 'vlc'},
    {'label': 'weechat'},
]

def ask_user():
    return pick(options, title, multi_select=True, min_selection_count=1, options_map_func=get_label)