from src.data.path import settings_path
from json import load, dump

global_settings = {}

def init_settings():
    global global_settings
    
    read_settings()
    
def read_settings():
    global global_settings
    
    with open(settings_path, 'r', encoding='utf-8') as f:
        s = load(f)
        global_settings = s

def get_settings(v: str):
    global global_settings
    
    for k, va in global_settings.items():
        if k == v:
            s = global_settings[k]
            return s

def set_settings(key: str, value: any):
    global global_settings
    
    for k, v in global_settings.items():
        if k == key:
            print(value)
            global_settings[k] = value
            with open(settings_path, 'w', encoding='utf-8') as f:
                dump(global_settings, f, indent=4, ensure_ascii=False)
            return