from os.path import join
from os import walk
from src.data.path import lang_path
from src.assets.settings.settings import *
from json import load

global_lang = {}

def init_lang() -> None:
    global global_lang
    
    lang = get_settings('lang')
    read_settings(lang)
    
def read_settings(lang: str) -> None:
    global global_lang
    
    fp = get_lang_file(lang)
    with open(fp, 'r', encoding='utf-8') as f:
        global_lang = load(f)
    
def get_lang(v: str) -> dict:
    global global_lang

    for k, va in global_lang.items():
        if k == v:
            s = global_lang[k]
            return s
    
def is_lang(lang: str) -> bool:
    global global_lang
    
    for root, dirs, files in walk(lang_path):
        for file in files:
            if file.endswith('.json'):
                if file.split('.')[0] == lang:
                    return True
                
    return False
    
def get_lang_file(lang: str) -> str:
    global global_lang
    
    for root, dirs, files in walk(lang_path):
        for file in files:
            if file.endswith('.json'):
                if file.split('.')[0] == lang:
                    return join(root, file)