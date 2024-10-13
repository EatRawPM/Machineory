from json import dump

# create a default settings file

value = {
    'lang': 'en_us',
}

def create_settings(fp) -> None:
    dump(value, fp, indent=4)