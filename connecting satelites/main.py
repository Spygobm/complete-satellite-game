import pgzrun 
import random 

HEIGHT = 600
WIDTH = 800

satellites = []
number_of_satellites = 10
next_satellite = 0
lines = []

def creating_satellites():
    global satellites
    for i in range (number_of_satellites):
        satellite = Actor("satellite")
        satellite.pos = (random.randint(20,WIDTH - 20),random.randint(20,HEIGHT - 20))
        satellites.append(satellite)

def draw():
    screen.clear()
    screen.blit("backround",(0,0))
    for item in satellites:
        item.draw()
    number = 1 
    for item in satellites:
        screen.draw.text(str(number),(item.pos[0],item.pos[1]+20))
        number += 1
    for i in lines:
        screen.draw.line(i[0],i[1],"white")
        

def on_mouse_down(pos):
    global lines,next_satellite
    if next_satellite < number_of_satellites:
        if satellites[next_satellite].collidepoint(pos):
            if next_satellite:
                lines.append((satellites[next_satellite-1].pos,satellites[next_satellite].pos))
            next_satellite += 1
        else:
            next_satellite = 0
            lines = []

def update():
    pass 
    


creating_satellites()

pgzrun.go()