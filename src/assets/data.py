from os.path import join, exists
from os import mkdir
from src.data.path import main_path, core_path, settings_path
from src.assets.settings.create import create_settings

def init_data():
    def main():
        def core():
            def settings():
                if exists(settings_path):
                    print(f'{settings_path} exists')
                else:
                    print(f'{settings_path} does not exist, creating it')
                    with open(settings_path, 'w', encoding='utf-8') as f:
                        create_settings(f)
            
            if exists(core_path):
                print(f'{core_path} exists')
                settings()
            else:
                print(f'{core_path} does not exist, creating it')
                mkdir(core_path)
                settings()
        
        if exists(main_path):
            print(f'{main_path} exists')
            core()
        else:
            print(f'{main_path} does not exist, creating it')
            mkdir(main_path)
            core()
    
    main()