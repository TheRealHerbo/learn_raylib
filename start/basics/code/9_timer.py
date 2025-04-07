from pyray import *
from raylib import *
from random import choice, randint

class Timer:
    def __init__(self, duration: int, repeat = False, autostart = False, func = None):
        self.duration = duration
        self.start_time = 0
        self.active = False
        self.repeat = repeat
        self.func = func
		
        if autostart:
            self.activate()

    def activate(self):
        self.active = True
        self.start_time = get_time()

    def deactivate(self):
        self.active = False
        self.start_time = 0
        if self.repeat:
            self.activate()

    def update(self):
        if self.active:
            if get_time() - self.start_time >= self.duration:
                if self.func and self.start_time: self.func()
                self.deactivate()

class Sprite:
    def __init__(self, pos, size):
        self.rec = Rectangle(pos[0], pos[1], size[0], size[1])
        self.color = WHITE
        self.timers = {
            'color': Timer(1.5, True, True, self.randomize_color),
            'pos': Timer(4, True, True, self.move)
        }

    def update(self):
        for timer in self.timers.values():
            timer.update()

    def randomize_color(self):
        print("color triggered")
        self.color = choice([RED, YELLOW, GREEN, ORANGE, MAGENTA, BLUE, GRAY, MAROON])

    def draw(self):
        draw_rectangle_rec(self.rec, self.color) 

    def move(self):
        print('move triggered')
        self.rec.x = randint(0, 100)
        self.rec.y = randint(0, 500)

def trigger_timer():
    print("timer triggered")

init_window(1280, 720, 'Timer')

sprite = Sprite((100, 50), (100, 200))
while not window_should_close():
    sprite.update()
    begin_drawing()
    clear_background(BLACK)
    sprite.draw()
    end_drawing()

close_window()