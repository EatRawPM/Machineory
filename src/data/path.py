from os.path import join, dirname, realpath
from sys import argv
from pathlib import Path

#assets

base_path = dirname(realpath(argv[0]))

assets_path = join(base_path, 'assets')

lang_path = join(assets_path, 'lang')

#data

user_path = Path.home()

main_path = join(user_path, 'AppData', 'LocalLow', 'EatRawPM')

core_path = join(main_path, 'Machineory')

settings_path = join(core_path,'settings.json')