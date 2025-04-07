from pyray import *
from raylib import *
from os.path import join


class Sprite:
    def __init__(self):
        self.x = 20
        self.y = 30
        self.color = WHITE
        self.animation_frames = [load_texture(join('assets', 'animation', f'{i}.png')) for i in range(8)]
        self.animation_index = 0
        self.animation_speed = 5
        self.index = 0

    def update(self, dt):
        self.index += self.animation_speed * dt

    def animate(self):
        draw_texture(animation_frames[int(self.index) % len(self.animation_frames)], self.x, self.y, WHITE)
    



init_window(1280, 720, 'Animations')

animation_frames = [load_texture(join('assets', 'animation', f'{i}.png')) for i in range(8)]
animation_index = 0
animation_speed = 5

sprite = Sprite()

while not window_should_close():
    dt = get_frame_time()
    sprite.update(dt)

    begin_drawing()
    clear_background(BLACK)
    sprite.animate()
    end_drawing()

close_window()