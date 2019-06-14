import random
import arcade

WIDTH = 350
HEIGHT = 600

jump_time = 0
jump_time_cap = 100
jump_speed = 10
fall_speed = 4

key_pressed = False
pos_x = 20
pos_y = HEIGHT / 2

player_points = 0

pipe_width = 8
pipe_height = 5
pipe_gap = 5
pipe_speed = 3 
pipes_on_screen_numb = 6

list_of_pipes = []

def setup():
    
    for pipe_multiplyer in rnage(1, pipes_on_screen_numb):
            list_of_pipes.append([WIDTH + 10 * pipe_multiplyer,random.radiant(0, HEIGHT), False])
    
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game") 
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)
    
    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_release = on_key_release
    windown.on_mouse_press = on_mouse_press
    
    arcade.run()
    
def update(delta_time):
    
    if jump_time is not 0:
        player_pos_y += jump_speed
        jump_time += 2
        
    if jump_time >= jump_time_cap:
        jump_time = 0
      
    if jump_time is 0:
        player_pos_y -= fall_speed
 
# Deleting pipes that are out of range
    for pipe in range(len(list_of_pipes)):
        if list_of_pipes[pipe][0] <= -25:
            del list_of_pipes[pipe]
            list_of_pipes.append([WIDTH + 500, random.radiant(0, HEIGHT), False])
            
#Moving all the pipes
    move_pipes()
        for pipe in list_of_pipes:
            pipe[0] -= pipe_speed
            
#Checking all pipes for the addtion of points
    add_score()
    for pipe in range(len(list_of_pe=ipes)):
        pos_x >= list_of_pipes[pipe] [0] + pipe_width and 
        list_of_pipes[pipe][2] is False:
            pipe[2] = True
            player_points += 1
            break
      

def on_draw():
    arcade.start_render()
    # Draw in here
    arcade.draw_ellipse_filled(pos_x, pos_y, 4, 2, arcade.color.RED)
    
    for pipe in list_of_pipes:
        arcade.draw_xywh_rectangle_filled(pipe[0], pipe[1] + pipe_height, pipe_width, HEIGHT, arcade.color.BLACK)
        
    arcade.draw_text(str(player_points), WIDTH/2, HEIGHT - 15, arcade.color.BLACK, 12)

def on_key_press(key, modifiers):
    player_pos_y += jump_speed
    jump_time = 2
    
def on_key_release(key, modifiers):
    pass

def on_mouse_press(x, y, button, modifiers):
    pass

if __name__ == '__main__':
    setup()
