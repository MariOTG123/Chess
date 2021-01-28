import pygame as pg
import time

pg.init()
w = 8
h = 8
l = 80
m = 5
k = 10
drag = 0

clock = pg.time.Clock()

screen = pg.display.set_mode((w*l+2*k,h*l+2*k))
screen.fill((0,0,0))

gpb = pg.image.load("Game_Piece_Black.xcf")
gpw = pg.image.load("Game_Piece_White.xcf")
x = 75
y = 75

def imageb(x,y):
    screen.blit(gpb,(int(x),int(y)))
def imagew(x,y):
    screen.blit(gpw,(int(x),int(y)))

black = (0,0,0)
white = (255,255,255)

odd = 0,1,0,1,0,1,0,1
even = 1,0,1,0,1,0,1,0

grid = [odd, even, odd, even, odd, even, odd, even]

print(grid)

def movableImg():
    global drag,x,y
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    imageb(x,y)
    imagew(x,y)
    if click[0] == 0:
        drag = 0
    if click[0] == 1 and x + l > mouse[0] > x and y + l > mouse[1] > y:
        drag = 1
    if drag == 1:
        x = mouse[0] - (l/2)
        y = mouse[1] - (l/2)



def main():
    while True:
        # Quit Game
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        # Mouse Coordinates Detection
        if event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            c = pos[0] // (l+2)
            r = pos[1] // (l+2)
            #print(pos,c,r)
        if event.type == pg.MOUSEBUTTONUP:
            if k + l > x > k and k + l > y > k:
                pass

        screen.fill(black)
        # Draw Board
        for c in range(w):
            for r in range(h):
                color = white
                pg.draw.rect(screen, color, pg.Rect(c*l+m+k,r*l+m+k,l-m,l-m))

        # Draw Game Piece
        screen.blit(gpb,pg.Rect(0*l+m+k,7*l+m+k,l-m,l-m))

        movableImg()

        pg.display.flip()
        clock.tick(60)

main()
pg.quit()
