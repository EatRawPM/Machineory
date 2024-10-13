from src.data.assets.icon import icon
from src.lang.init import *
from src.assets.data import init_data
from src.assets.settings.settings import *
import pygame
import sys

init_data()
init_settings()
init_lang()

class App:
    def __init__(self):
        pygame.init()
        
        pygame.display.set_caption(get_lang('core.display.caption'))
        pygame.display.set_icon(icon)
        pygame.display.set_mode((1280, 720))
        
        self.surface_display = pygame.display.get_surface()
        
        self.clock = pygame.time.Clock()
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
    def update(self):
        self.clock.tick(60)
        pygame.display.update()
        
    def run(self):
        while True:
            self.handle_events()
            self.update()