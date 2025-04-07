from pyray import *
from raylib import * 

init_window(1280, 720, "Collisions")
player_pos = Vector2(0,0)
obstacle_pos = Vector2(500,400) 
player_radius = 50
obstacle_radius = 30

r1 = Rectangle(0,0,100,200)
r2 = Rectangle(800,300,200,300)

while not window_should_close():
    
    # input 
    player_pos = get_mouse_position()
    r1.x = get_mouse_x()
    r1.y = get_mouse_y()


    #collision
    # print(check_collision_circle_rec(player_pos, player_radius,r1))
    print(check_collision_recs(r2, r1))
    
    # drawing
    begin_drawing()
    clear_background(BLACK)
    # draw_circle_v(player_pos, player_radius, WHITE)
    draw_circle_v(obstacle_pos, obstacle_radius, RED)    
    draw_rectangle_rec(r1, BLUE)
    draw_rectangle_rec(r2, GREEN)
    draw_rectangle_rec(get_collision_rec(r1,r2), RED)
    end_drawing()

close_window()