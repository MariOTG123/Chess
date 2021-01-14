import pygame as pg

pg.init()
w = 8
h = 8
l = 80
m = 5
k = 10

screen = pg.display.set_mode((w*l+2*k,h*l+2*k))
screen.fill((0,0,0))


black = (0,0,0)
white = (255,255,255)

odd = 0,1,0,1,0,1,0,1
even = 1,0,1,0,1,0,1,0

grid = [odd, even, odd, even, odd, even, odd, even]
        

print(grid)

running = True
while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    if event.type == pg.MOUSEBUTTONDOWN:
        pos = pg.mouse.get_pos()
        c = pos[0] // (l+m)
        r = pos[1] // (l+m)
        grid[c][r] == 1
        print(pos,c,r)


    for c in range(w):
        for r in range(h):
            color = white
            pg.draw.rect(screen, color, pg.Rect(c*l+m+k,r*l+m+k,l-m,l-m))


    pg.display.flip()

pg.display.quit()
