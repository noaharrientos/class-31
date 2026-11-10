import pygame
import random
pygame.init()
spritecolorchangeevent=pygame.USEREVENT+1
backgroundcolorchangeevent=pygame.USEREVENT+2
blue=pygame.Color("blue")
green=pygame.Color("green")
yellow=pygame.Color("yellow")
red=pygame.Color("red")
pink=pygame.Color("pink")
purple=pygame.Color("purple")
brown=pygame.Color("brown")
orange=pygame.Color("orange")
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.velocity=[random.choice([-1,1]),random.choice([-1,1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundaryhit=False
        if self.rect.left<=0 or self.rect.right>=500:
            self.velocity[0]=-self.velocity[0]
            boundaryhit=True
        if self.rect.top<=0 or self.rect.bottom>=400:
            self.velocity[1]=-self.velocity[1]
            boundaryhit=True
        if boundaryhit:
            pygame.event.post(pygame.event.Event(spritecolorchangeevent))
            pygame.event.post(pygame.event.Event(backgroundcolorchangeevent))
    def changecolor(self):
        self.image.fill(random.choice([orange,purple,yellow,brown]))
def changebackgroundcolor():
    global bgcolor
    bgcolor=random.choice([red,blue,green,pink])
allspritelist=pygame.sprite.Group()
s1=Sprite(orange,20,30)
s1.rect.x=random.randint(0,480)
s1.rect.y=random.randint(0,370)
allspritelist.add(s1)
screen=pygame.display.set_mode((500,400))
pygame.display.set_caption("boundarysprite")
bgcolor=blue
clock=pygame.time.Clock()
exit=False
while not exit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit=True
        elif event.type==spritecolorchangeevent:
            s1.changecolor()
        elif event.type==backgroundcolorchangeevent:
            changebackgroundcolor()
    allspritelist.update()
    screen.fill(bgcolor)
    allspritelist.draw(screen)
    pygame.display.flip()
    clock.tick(240)
pygame.quit()