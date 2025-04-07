from raylib import *
from pyray import *

def collision(axis):
    for block in blocks:
        if check_collision_recs(block, player):
            if axis == 'x':
                if direction.x > 0: # the player is moving right
                    player.x = block.x - player.width
                if direction.x < 0: # move left
                    player.x = block.x + block.width
            else:
                if direction.y > 0: # the player is moving down
                    player.y = block.y - player.height
                if direction.y < 0: # move up
                    player.y = block.y + block.height

init_window(1280, 720, "Collision resolution")

level_map = [
    '1111111111111111',
    '1010000000000001',
    '1010000000111111',
    '1000000200000011',
    '1001100000010001',
    '1001100000010001',
    '1001100000010001',
    '1111111111111111'
]

player = Rectangle(400,300,60,60)
speed = 300
direction = Vector2()

blocks = []
block_size = 100
for row_index, row in enumerate(level_map):
    for col_index, cell in enumerate(row):
        if cell == '1':
            x = col_index * block_size
            y = row_index * block_size
            block = Rectangle(x,y,block_size,block_size)
            blocks.append(block)


while not window_should_close():
    direction.x = int(is_key_down(KEY_RIGHT)) - int(is_key_down(KEY_LEFT))
    direction.y = int(is_key_down(KEY_DOWN)) - int(is_key_down(KEY_UP))
    
    # movement
    dt = get_frame_time()
    player.x += direction.x * speed * dt
    collision('x')
    player.y += direction.y * speed * dt
    collision('y')

    begin_drawing()    
    clear_background(BLACK)
    for block in blocks:
        draw_rectangle_rec(block, GRAY)
    draw_rectangle_rec(player, RED)
    end_drawing()
close_window()