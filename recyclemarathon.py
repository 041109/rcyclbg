import pygame
import random
import time
pygame.init()

WIDTH = 500
HEIGHT = 500

def changeBackground(img):
    background = pygame.image.load(img)
    bg = pygame.transform.scale(background,(WIDTH,HEIGHT))
    screen.blit(bg,(0,0))

pygame.display.set_caption("Recycle Marathon")
screen = pygame.display.set_mode([WIDTH,HEIGHT])

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("RecycleMarathon/bin.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(50,80))
        self.rect = self.image.get_rect()

class Recycable(pygame.sprite.Sprite):
    def __init__(self,img):
        # super init function used to call to initialise the pygame.sprite.Sprite class
        # ensuring that recycable class is properly initialised as a sprite
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image,(50,80))
        self.rect = self.image.get_rect()

class Non_Recycable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("RecycleMarathon/redbag.png")
        self.image = pygame.transform.scale(self.image,(50,80))
        self.rect = self.image.get_rect()


# list of images for recyclable items
images = ["RecycleMarathon/wodenbox.png" , "RecycleMarathon/paperbag.png" , "RecycleMarathon/pencil.png"]

# create sprite groups
item_list = pygame.sprite.Group()
allsprites = pygame.sprite.Group()
plastic_list = pygame.sprite.Group() 

# creating sprites
for i in range(20):
    item = Recycable(random.choice(images))
    item.rect.x = random.randrange(WIDTH)
    item.rect.y = random.randrange(HEIGHT)
    item_list.add(item)
    allsprites.add(item)

# create plastic bags
for i in range(15):
    plastic = Non_Recycable()
    plastic.rect.x = random.randrange(WIDTH)
    plastic.rect.y = random.randrange(HEIGHT)
    plastic_list.add(plastic)
    allsprites.add(plastic)




bin = Bin()
allsprites.add(bin)

#variables
wht = (255,255,255)
rd = (255,0,0)
grn = (0,255,0)
blck = (0,0,0)

run = True
score = 0
clock = pygame.time.Clock()
start_time = time.time()
myFont = pygame.font.SysFont("Times New Roman",22)
timingFont = pygame.font.SysFont("TimesNew Roman" , 22)
text = myFont.render("Score = " +str(0),True,grn)



#--------Main Prog. loop--------------------

while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run =False
    
    timeElapsed=time.time()-start_time
    if timeElapsed >= 60:
        if score > 5:
            text = myFont.render("Congratulations,you won!", True, rd)
            changeBackground("RecycleMarathon/winnerwindow.jpg")
            screen.blit(text,(250,250))
        else:
            text = myFont.render("Unfortunately you lost!",True,blck)
            changeBackground("RecycleMarathon/loserwindow.png")
            screen.blit(text,(250,50))
    
    else:
        changeBackground("RecycleMarathon/background.png")
        countDown = timingFont.render("Time Left: " +str(60-int(timeElapsed)),True,wht)
        screen.blit(countDown,(20,20))


        #To move bin as per key pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if bin.rect.y > 0:
                bin.rect.y -= 5
                
        if keys[pygame.K_DOWN]:
            if bin.rect.y < 500:
                bin.rect.y += 5
                
        if keys[pygame.K_LEFT]:
            if bin.rect.x > 0:
                bin.rect.x -= 5
        
        if keys[pygame.K_RIGHT]:
            if bin.rect.x < 500:
                bin.rect.x += 5
    
        item_hit_list = pygame.sprite.spritecollide(bin,item_list,True)
        plastic_hit_list = pygame.sprite.spritecollide(bin,plastic_list,True)

        for item in item_hit_list:
            score += 1
            text = myFont.render("Score: "+str(score),True,wht)

        for item in plastic_hit_list:
            score -= 1
            text = myFont.render("Score: "+str(score),True,wht)

        screen.blit(text,(50,50))

    
    allsprites.draw(screen)
    











    pygame.display.update()
pygame.quit()