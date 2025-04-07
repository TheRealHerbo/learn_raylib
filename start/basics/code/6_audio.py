from pyray import *
from raylib import *
from os.path import join

init_window(1280,720, 'Sound')
init_audio_device()

laser_sound = load_sound(join('assets', 'laser.wav'))
play_sound(laser_sound)
music = load_music_stream(join('assets', 'music.wav'))
play_music_stream(music)

while not window_should_close():
    update_music_stream(music)
    begin_drawing()
    clear_background(BLACK)
    end_drawing()

unload_music_stream(music)
close_audio_device()
close_window()