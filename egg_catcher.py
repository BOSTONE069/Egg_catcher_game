from itertools import cycle
from random import randint, randrange
from tkinter import Tk , Canvas, messagebox, font

canvas_width = 800
canvas_height = 400

win = Tk()
c = Canvas(win , width=canvas_width, height=canvas_height, background='deep sky blue') #This for creating the primary background
c.create_rectangle(-5, canvas_height -100 , canvas_width +5, canvas_height +5, fill='sea green', width=0) #this greated the green background
c.create_oval(-80,-80,120,120,fill='orange' , width=0) #this for creating the sun
c.pack()

color_cycle = cycle(['light blue', 'light pink', 'light yellow',
                    'light green', 'red', 'blue', 'green', 'black'])
egg_width = 45
egg_height = 55
egg_score = 10
egg_speed = 500
egg_interval = 4000
difficulty_factor = 0.95

#This defines the outlook of the catcher and its colors and dimentions
catcher_color = 'blue' 
catcher_width = 100
catcher_height = 100
catcher_start_x = canvas_width / 2 - catcher_width / 2
catcher_start_y = canvas_height - catcher_height - 20
catcher_start_x2 = catcher_start_x + catcher_width
catcher_start_y2 = catcher_start_y + catcher_height

catcher = c.create_arc(catcher_start_x, catcher_start_y, catcher_start_x2, catcher_start_y2,
                       start=200, extent=140, style='arc', outline=catcher_color, width=3)

#This is used to determine the score interface
score = 0
score_text = c.create_text(10, 10, anchor='nw', font=(
    'Arial', 18, 'bold'), fill='darkblue', text='Score : ' + str(score))

#This is used to determine the lives interface
lives_remaning = 3
lives_text = c.create_text(canvas_width-10, 10, anchor='ne', font=(
    'Arial', 18, 'bold'), fill='darkblue', text='Lives : ' + str(lives_remaning))
win.mainloop()
