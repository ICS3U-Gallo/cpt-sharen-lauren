import random
import arcade

WIDTH = 350
HEIGHT = 600

jump_time = 0
jump_time_cap = 10
jump_speed = 10
fall_speed = 15

key_pressed = False
pos_x = 40
pos_y = HEIGHT / 2

player_points = 0

pipe_width = 45
pipe_height = 60
pipe_gap = 150
pipe_speed = 8
pipes_on_screen_numb = 6

list_of_pipes = []

screen = "playing"

def setup():
    
    for pipe_multiplyer in range(1, pipes_on_screen_numb):
            list_of_pipes.append([WIDTH + 10 * pipe_multiplyer,random.radiant(0, HEIGHT), False])
    
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game") 
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/100)
    
    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    windown.on_mouse_press = on_mouse_press
    
    arcade.run()
    
def update(delta_time):
    
    # Manage the smooth jumping mechanism
    if jump_time is not 0:
        player_pos_y += jump_speed
        jump_time += 2
        
    if jump_time >= jump_time_cap:
        jump_time = 0
      
    if jump_time is 0:
        pos_y -= fall_speed
 
    # Deleting pipes that are out of range
    for pipe in range(len(list_of_pipes)):
        if list_of_pipes[pipe][0] <= -25:
            del list_of_pipes[pipe]
            list_of_pipes.append([WIDTH + 500, random.radiant(0, HEIGHT), False])
            
    #Moving all the pipes
        for pipe in list_of_pipes:
            pipe[0] -= pipe_speed
            
    #Checking all pipes for the addtion of points
    for pipe in range(len(list_of_pipes)):
        if pos_x >= list_of_pipes[pipe] [0] + pipe_width:
            if list_of_pipes [pipe] [2] is False:
                list_of_pipes [pipe] [2] = True
                player_points += 1
                print("scored")
            else:
                
                print('ded')
                screen = "death"
                
 if screen == "death":
    print('ded')
            
def on_draw():
    arcade.start_render()
    
    
    # Draw in here...
    arcade.draw_ellipse_filled(pos_x, pos_y, 4, 2, arcade.color.RED)
    
    for pipe in list_of_pipes:
        arcade.draw_xywh_rectangle_filled(pipe[0], pipe[1] + pipe_height, pipe_width, HEIGHT, arcade.color.BLACK) #x,y,w,h
        arcade.draw_xywh_rectangle_filled(pipe [0], 0, pipe_width, pipe[1], arcade.color.BLACK)
    
    arcade.draw_text(str(player_points), WIDTH / 2, HEIGHT - 15, arcade.color.BLACK, 12)

def on_key_press(key, modifiers):
    global pos_y
    gloabl jump_speed
    global jump_time
    
    if arcade.key.SPACE == key:
        pos_y += jump_speed
        jump_time = 2

    
def on_key_release(key, modifiers):
    pass

def on_mouse_press(x, y, button, modifiers):
    pass

if __name__ == '__main__':
    setup()
