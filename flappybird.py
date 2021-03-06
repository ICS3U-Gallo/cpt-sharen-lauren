import arcade
import random
import sys
import os

# Defining all the variables
WIDTH = 350
HEIGHT = 600

restart = False

jumping = False

jump_speed = 5
fall_speed = 3

y_velocity = 0

max_jump_height = 20
max_fall_velocity = 15

key_pressed = False
pos_x = 40
pos_y = HEIGHT / 2

player_points = 0

pipe_width = 45
pipe_height = 60
pipe_gap = 200
pipe_speed = 5
pipes_on_screen_numb = 6

list_of_pipes = []

screen = "playing"

def setup():
    
    # Create all the pipes before the game actually starts
    for pipe_multiplyer in range(1, pipes_on_screen_numb):
        list_of_pipes.append([WIDTH + pipe_gap * pipe_multiplyer, random.randint(100, HEIGHT -100), False])
    
    arcade.open_window(WIDTH, HEIGHT, "Flappy Bird") 
    arcade.set_background_color(arcade.color.LIGHT_BLUE)
    arcade.schedule(update, 1 / 100)
    
    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    
    arcade.run()
    
def update(delta_time):
    
    global screen
    
    global jump_speed
    global fall_speed
    global jumping
    global y_velocity
    global max_fall_velocity
    
    global player_points
    global pos_y
    global pos_x
    
    global list_of_pipes
    global pipe_speed
    global pipe_width
    
    if screen == "playing":
        
        # Manage the jumping and falling
        if jumping == True:
            y_velocity = 0
            y_velocity += jump_speed
            
            if y_velocity >= max_fall_velocity:
                jumping = False
            
        else: 
            y_velocity -= fall_speed
            
            if y_velocity <= max_fall_velocity:
                y_velocity = y_velocity
             
        pos_y += y_velocity        
 
        # Deleting pipes that are out of range
        for pipe in range(len(list_of_pipes)):
            if list_of_pipes[pipe][0] <= -25:
                del list_of_pipes[pipe]
                list_of_pipes.append([WIDTH + 500, random.randint(0, HEIGHT), False])
            
        # Moving all the pipes
        for pipe in list_of_pipes:
            pipe[0] -= pipe_speed
            
        # Checking all pipes for the addtion of points
        for pipe in range(len(list_of_pipes)):
            if pos_x >= list_of_pipes[pipe][0] + pipe_width:
                if list_of_pipes[pipe][2] is False:
                    
                    list_of_pipes[pipe][2] = True
                    player_points += 1

        # Checking if the player hit a pipe
        for pipe in range(len(list_of_pipes)):
            if pos_x >= list_of_pipes[pipe][0] and pos_x <= list_of_pipes[pipe][0] + pipe_width:
                if pos_y >= list_of_pipes[pipe][1] + pipe_height or pos_y <= list_of_pipes[pipe][1]:
                    screen = "death"
        
        # Checking if the player hit the ground
        if pos_y < 0:
            screen = "death"
        
        # Capping the height of the player
        elif pos_y >= HEIGHT:
            pos_y = HEIGHT
    
    # Restart the program if you are dead and the player hits enter
    if screen == "death":
        if restart is True:
            os.execl(sys.executable, sys.executable, *sys.argv)
            
def on_draw():
    
    global screen
    
    arcade.start_render()
    
    if screen == "death":
        arcade.draw_text(f"You got {str(player_points)}!", 60, 60, arcade.color.BLACK, 12)
        arcade.draw_text("Press enter to restart the game", 60, 30, arcade.color.BLACK, 12)
        
    elif screen == "playing":
    
        # Draw the player
        arcade.draw_ellipse_filled(pos_x, pos_y, 8, 5, arcade.color.SCHOOL_BUS_YELLOW)
    
        # Draw all the pipes
        for pipe in list_of_pipes:
            arcade.draw_xywh_rectangle_filled(pipe[0], pipe[1] + pipe_height, pipe_width, HEIGHT, arcade.color.GO_GREEN)
            arcade.draw_xywh_rectangle_filled(pipe [0], 0, pipe_width, pipe[1], arcade.color.GO_GREEN)
    
        arcade.draw_text(str(player_points), WIDTH / 2, HEIGHT - 15, arcade.color.BLACK, 12)
    
def on_key_press(key, modifiers):
    global restart
    
    global pos_y
    global jump_speed
    global jumping
    
    if arcade.key.SPACE == key:
        jumping = True
        jump_speed = 20
        
    if arcade.key.ENTER == key:
        restart = True


if __name__ == '__main__':
    setup()
