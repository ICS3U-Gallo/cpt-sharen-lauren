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
pos_y = HEIGHT /2

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

    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_release = on_key_release
    windown.on_mouse_press = on_mouse_press
    
'''
def jump():
    player_pos_y += jump_speed
    jump_time = 2

def fall():
    player_pos_y -= fall_speed

def move_pipes():
    for pipe in list_of_pipes:
        pipe[0] -= pipe_speed

def delete_pipes():
    for pipe in range(len(list_of_pipes)):

        if list_of_pipes[pipe][0] <= -25:
            del list_of_pipes[pipe]
            list_of_pipes.append([WIDTH + 500, random.randint(0,HEIGHT)])

def draw_pipes():
    for pipe in list_of_pipes:
        draw_rect(pipe[0],pipe[1] + pipe_height, pipe_width, HEIGHT) #x,y,w,h
        draw_rect(pipe[0], 0, pipe_width,pipe[1] )

def draw_player():
    draw_rect(pos_x, pos_y, -5, 2)

def draw_score():
    print(player_points)

def main():

    arcade.open_window(WIDTH, HEIGHT, "Flappy Bird")
    arcade.start_render()

    draw_background = (arcade.set_background_color(arcade.color.SKY_BLUE))

    if arcade.key is True:
        jump()

    if jump_time is not 0:
        player_pos_y += jump_speed
        jump_time += 2
    
    if jump_time >= jump_time_cap:
        jump_time = 0
    
    if jump_time is 0:
        fall()

    draw_player()

    delete_pipes()
    move_pipes()

    previous_pipe = 0

    for pipe in range(len(list_of_pipes)):
        in_x_range = False
        in_y_range = False

        if pos_x >= list_of_pipes[pipe][0] and pos_x <= list_of_pipes[pipe][0] + pipe_width:
            in_x_range = True

        if pos_y >= list_of_pipes[pipe][1] and pos_y <= list_of_pipes[pipe][1] + pipe_height:
         in_y_range = True

        if in_x_range and in_y_range and previous_pipe is not pipe:
            player_points += 1
            previous_pipe = pipe
            
            break

    draw_score()
    
    for pipe_multiplyer in range(1, pipes_on_screen_numb):
        list_of_pipes.append([WIDTH + 10 *pipe_multiplyer, random.randint(0,HEIGHT)])
    
    arcade.run()

    arcade.finish_render()

main()
'''
