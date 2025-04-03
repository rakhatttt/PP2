import pygame

pygame.init()

WIDTH, HEIGHT= 800, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Paint")

WHITE=(255,255,255)
GRAY=(255,200,200)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BlUE=(0,0,255)
Yellow=(255,255,0)

screen.fill(BLACK)
LMBpressed= False
RMBpressed = False
THICKNESS=5
mode = "brush"

prevX=prevY=0
startX=startY=0

rects=[]
circles=[]
squares = []
right_triangles=[]
equilateral_triangles=[]
rhombuses=[]

drawing_surface=screen.copy()
curr_color=RED
clock=pygame.time.Clock()

done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_1:
                mode="brush"
            elif event.key==pygame.K_2:
                mode="rect"
            elif event.key==pygame.K_3:
                mode="circle"
            elif event.key==pygame.K_4:
                mode="square"
            elif event.key==pygame.K_5:
                mode="right_triangle"
            elif event.key==pygame.K_6:
                mode="equilateral_triangle"
            elif event.key==pygame.K_7:
                mode="rhombus"
            elif event.key==pygame.K_EQUALS:
                THICKNESS+=1
            elif evnet.key==pygame.K_MINUS:
                THICKNESS=max(1,THICKNESS-1)
            elif event.key==pygame.K_c:
                screen.fill(BLACK)
                rects.clear()
                circles.clear()
                squares.clear()
                right_triangles.clear()
                equilateral_triangles.clear()
                rhombuses.clear()
                drawing_surface=screen.copy()
            elif event.key==pygame.K_r:
                curr_color=RED
            elif event.key==pygame.K_g:
                curr_color=GREEN
            elif event.key==pygame.K_b:
                curr_color=BlUE

        elif event.type == pygame.MOUSEBUTTONDOWN:  #нажатие мыши
            if event.button == 1:
                LMBpressed = True
                prevX, prevY = event.pos
                startX, startY = event.pos
    
        elif event.type == pygame.MOUSEMOTION:  #Движение мыши
            currX, currY = event.pos
            if LMBpressed:
                if mode == "brush":
                    pygame.draw.line(drawing_surface, curr_color, (prevX, prevY), (currX, currY), THICKNESS)
                    prevX, prevY = currX, currY
                elif mode in ["rect", "square"]:
                    size = abs(currX - startX)
                    rect = pygame.Rect(min(startX, currX), min(startY, currY), size if mode == "square" else abs(currX - startX), size if mode == "square" else abs(currY - startY))
                elif mode == "circle":
                    radius = max(abs(currX - startX), abs(currY - startY)) // 2
                    circle = pygame.Rect(startX - radius, startY - radius, radius * 2, radius * 2)
                elif mode == "right_triangle":
                    right_tri = [(startX, startY), (currX, startY), (startX, currY)]
                elif mode == "equilateral_triangle":
                    side = abs(currX - startX)
                    equilateral_tri = [(startX, startY), (startX + side, startY), (startX + side // 2, startY - int(side * (3 ** 0.5) / 2))]
                elif mode == "rhombus":
                    rhombus = [(startX, startY - 50), (startX + 50, startY), (startX, startY + 50), (startX - 50, startY)]


        elif event.type==pygame.MOUSEBUTTONUP:
            if event.button==1:
                LMBpressed=False
                if mode =="rect":
                    rects.append((rect.copy(),curr_color))
                elif mode=="square":
                    squares.append((rect.copy(),curr_color))
                elif mode == "circle":
                    circles.append((circles.copy(),curr_color))
                elif mode == "right_triangles":
                    right_triangles.append((right_triangles.copy(),curr_color))
                elif mode == "equilateral_triangle":
                    equilateral_triangles.append((equilateral_triangles.copy(),curr_color))
                elif mode == "rhombus":
                    rhombuses.append((rhombuses.copy(),curr_color))
    
    screen.blit(drawing_surface,(0,0))
    for r,color in rects:
        pygame.draw.rect(screen,color,r,2)
    for s, color in squares:
        pygame.draw.rect(screen,color,s,2)
    for c,color in circles:
        pygame.draw.ellipse(screen,color,c,2)
    for tri,color in right_triangles:
        pygame.draw.polygon(screen,color,c,2)
    for tri,color in equilateral_triangles:
        pygame.draw.polygon(screen,color,tri,2)
    for rhomb, color in rhombuses:
        pygam.draw.polygon(screen,color,rhomb,2)
    

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
            

