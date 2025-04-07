from pyray import *
from raylib import * 
from random import randint, choice

init_window(1280, 720, "Camera")

# player
pos = Vector2()
radius = 50
direction = Vector2()
speed = 400

# circles
circles = [
    (
        Vector2(randint(-2000,2000),randint(-1000,1000)), # pos
        randint(50,200), # radius
        choice([RED, GREEN, BLUE, YELLOW, ORANGE]) # color
    ) 
    for i in range(100)
]

# camera
camera = Camera2D()
camera.zoom = 0.7
camera.offset = Vector2(1280/2,720/2)
camera.rotation = 0


while not window_should_close():
    
    # input
    direction.x = int(is_key_down(KEY_RIGHT)) - int(is_key_down(KEY_LEFT))
    direction.y = int(is_key_down(KEY_DOWN)) - int(is_key_down(KEY_UP))
    direction = vector2_normalize(direction)

    # movement
    dt = get_frame_time()
    pos.x += direction.x * speed * dt
    pos.y += direction.y * speed * dt

    # camera update
    rotate_direction = int(is_key_down(KEY_A)) - int(is_key_down(KEY_S)) 
    zoom_level = int(is_key_down(KEY_Q)) - int(is_key_down(KEY_W)) 
    camera.target = pos
    camera.target = pos
    camera.rotation += rotate_direction * dt * 50
    camera.zoom += zoom_level * dt * 1
    camera.zoom = max(0.2, min(2, camera.zoom))

    # drawing
    begin_drawing()
    begin_mode_2d(camera)
    clear_background(WHITE)
    for circle in circles:
        draw_circle_v(*circle)
    draw_circle_v(pos, radius, BLACK)
    end_mode_2d()
    end_drawing()

close_window()