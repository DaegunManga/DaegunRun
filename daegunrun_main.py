import pygame as pg
import OBJpy
import RNDpy
import time

windowSize = [1020,680]

def judge_conflict (a_x1, a_x2, a_y1, a_y2, b_x1, b_x2, b_y1, b_y2) : # 충돌 판단 함수
    if (a_x2 < b_x1) or (a_x1 > b_x2) or (a_y1 > b_y2) or (a_y2 < b_y1):
        return False
    else :
        return True


# x1, y1          x2, y1

# x1, y2          x2, y2

def Button (img_in, x, y, width, height, img_act, x_act, y_act) : # 버튼 생성 함수
    mouse = pg.mouse.get_pos()   

    click = pg.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y: 

        gamepad.blit(img_act,(x_act, y_act)) 

        if click[0] :

            return True             

    else:

        gamepad.blit(img_in,(x,y))      
        return False        







def initGame (): # 게임 기본 설정
    global gamepad, clock,MANGA, daegune1, daegune2, daegune_slide, chair, whiteboard, obj, rnd, background, option_button, staff_button, quit_button, SOUND_ON, SOUND_OFF, daegunmark, sound, music
    global line, white
    pg.init()
    gamepad = pg.display.set_mode (windowSize)
    pg.display.set_caption("DaeGunRun")

    round_L=[]

    daegune1=pg.image.load ('daegune1.gif')
    daegune1 = pg.transform.scale(daegune1,(180,225))

    daegune2=pg.image.load ('daegune2.png')
    daegune2 = pg.transform.scale(daegune2,(180,225))

    daegune_slide=pg.image.load ('daegune_slide.gif')
    daegune_slide = pg.transform.scale(daegune_slide,(225,180))

    option_button=pg.image.load ('obtion_button.png')
    option_button = pg.transform.scale(option_button,(163,48))

    staff_button=pg.image.load ('staff_button.png')
    staff_button = pg.transform.scale(staff_button,(163,48)) 

    quit_button=pg.image.load ('Quit_Button.png')
    quit_button = pg.transform.scale(quit_button,(163,48))

    MANGA=pg.image.load ('MANGA.png')
    MANGA = pg.transform.scale(MANGA,(163,48))

    SOUND_OFF=pg.image.load ('ON_PLAY.png')
    SOUND_OFF = pg.transform.scale(SOUND_OFF,(180,40))

    SOUND_ON=pg.image.load ('OFF_PLAY.png')
    SOUND_ON = pg.transform.scale(SOUND_ON,(180,40))

    daegunmark=pg.image.load("Daegun.png")
    daegunmark = pg.transform.scale(daegunmark,(100,100))

    piano=pg.image.load ('piano.png')
    piano = pg.transform.scale(piano,(120,120))

    chair=pg.image.load ('chair.png')
    chair = pg.transform.scale(chair,(80,96))

    music=pg.image.load ('music.png')
    music = pg.transform.scale(music,(360,360))

    roller_paint=pg.image.load ('roller-paint.png')
    roller_paint = pg.transform.scale(roller_paint,(151,128))

    canvas=pg.image.load ('canvas.png')
    canvas = pg.transform.scale(canvas,(309,384))

    whiteboard=pg.image.load ('whiteboard.png')
    whiteboard = pg.transform.scale(whiteboard,(540,360))

    background=pg.image.load ('background.png')
    background = pg.transform.scale(background,(960,540))

    line=pg.image.load ('line.png') 
    line = pg.transform.scale(line,(600,50))

    white=pg.image.load ('white.png')
    white = pg.transform.scale(white,(600,50))

    round_L.append([[chair, 80, 96, 'down'], [whiteboard, 540, 360, 'up']])
    round_L.append([[piano, 120, 120, 'down'],[music, 360, 360, 'up']])
    round_L.append([[roller_paint, 151, 128, 'down'],[canvas, 309, 384, 'up']])


    obj = OBJpy.object()
    rnd = RNDpy.round(round_L)

    clock = pg.time.Clock()





















def startGame (): #게
    global gamepad, clock, background, option_button, staff_button, MUSIC_TOF
    pg.init()
    done = False 
    t=0
    MUSIC_TOF = True
    while not done :
        for event in pg.event.get ():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.KEYDOWN :
                if event.key == pg.K_SPACE  :
                    runGame()


        gamepad.fill((255,255,255))
        gamepad.blit(background,(30, -50))

        LargeText = pg.font.SysFont( "arial", 40, True, False)
        #SmallText = pg.font.SysFont( "arial", 12, True, False)

        if t <= 255 :
            textSurface = LargeText.render("PRESS 'SPACE BAR' TO START",True,(0,t,0))
        else :
            textSurface = LargeText.render("PRESS 'SPACE BAR' TO START",True,(0,510 - t,0))
        
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (windowSize[0]/2,windowSize[1]*4/5)
        gamepad.blit(TextSurf , TextRect)

        #textSurface = SmallText.render("MAIN DEVELOPER : LeeDoWon",True,(0,0,0))
        #TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        #TextRect.center = (windowSize[0]/2,430)
        #gamepad.blit(TextSurf , TextRect)

        #textSurface = SmallText.render(" SUB DEVELOPER : LeeJuHo",True,(0,0,0))
        #TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        #TextRect.center = (windowSize[0]/2,450)
        #gamepad.blit(TextSurf , TextRect)

        TOF = Button(option_button,430,325,163,48,option_button,423,323)   # option
        
        if TOF : option()

        TOF2 = Button(staff_button,430,400,163,48,staff_button,423,398)   # staff

        if TOF2 : staff()



        #OptionButton = Button(start_button2,445,260,60,20,start_button2,440,258) #참조 : https://m.blog.naver.com/scyan2011/221998190058

        pg.display.update() 
        t+=5
        if t == 510 :
            t = 0
            
        clock.tick (60)







def staff () :
    global gamepad, clock, background
    pg.init()
    done = False 
    t=0
    t1=0
    t2 = 0
    while not done :
        for event in pg.event.get ():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.KEYDOWN :
                if event.key == pg.K_SPACE  :
                    runGame()


        gamepad.fill((255,255,255))
        gamepad.blit(background,(30, -50-t))

        LargeText = pg.font.SysFont( "arial", 40, True, False)
        SmallText = pg.font.SysFont( "arial", 20, True, False)

        if t1 <= 255 :
            textSurface = LargeText.render("PRESS 'SPACE BAR' TO START",True,(0,t1,0))
        else :
            textSurface = LargeText.render("PRESS 'SPACE BAR' TO START",True,(0,510 - t1,0))
        
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (windowSize[0]/2,windowSize[1]*4/5-t)
        gamepad.blit(TextSurf , TextRect)

        textSurface = SmallText.render("MAIN DEVELOPER : LeeDoWon",True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (windowSize[0]/2,700-t2)
        gamepad.blit(TextSurf , TextRect)

        textSurface = SmallText.render("SUB DEVELOPER : LeeJuHo",True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (windowSize[0]/2,720-t2)
        gamepad.blit(TextSurf , TextRect)

        textSurface = SmallText.render("FONT FROM : COOKIERUN",True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (windowSize[0]/2,760-t2)
        gamepad.blit(TextSurf , TextRect)

        textSurface = SmallText.render("IMG FROM : flaticon.com",True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (windowSize[0]/2,780-t2)
        gamepad.blit(TextSurf , TextRect)

        TOF = Button(option_button,430,325-t,163,48,option_button,423,323-t)   # option

        TOF2 = Button(staff_button,430,400-t,163,48,staff_button,423,398-t)   # staff

        TOF3 = Button(quit_button,7,700-t,163,48,quit_button,0,698-t)   # Quit

        if TOF3 : done = True

        gamepad.blit(MANGA,(275, 1100-t))
        gamepad.blit(daegunmark,(600, 1075-t))

        #OptionButton = Button(start_button2,445,260,60,20,start_button2,440,258) #참조 : https://m.blog.naver.com/scyan2011/221998190058

        pg.display.update() 

        if t < 680 :
            t+=2
            t1+=5
            if t1 == 510 :
                t1 = 0
        if t2 < 480 :
            t2+=2
            
        clock.tick (60)





def option () :
    global gamepad, clock, background, MUSIC_TOF
    pg.init()
    done = False 
    t=0
    t1=0
    t2 = 0
    while not done :
        for event in pg.event.get ():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.KEYDOWN :
                if event.key == pg.K_SPACE  :
                    done = True


        gamepad.fill((255,255,255))
        gamepad.blit(background,(30, -50+t))

        LargeText = pg.font.SysFont( "arial", 40, True, False)
        SmallText = pg.font.SysFont( "arial", 20, True, False)

        if t1 <= 255 :
            textSurface = LargeText.render("PRESS 'SPACE BAR' TO START",True,(0,t1,0))
        else :
            textSurface = LargeText.render("PRESS 'SPACE BAR' TO START",True,(0,510 - t1,0))
        
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (windowSize[0]/2,windowSize[1]*4/5+t)
        gamepad.blit(TextSurf , TextRect)

        textSurface = SmallText.render("MAIN DEVELOPER : LeeDoWon",True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (windowSize[0]/2,700+t2)
        gamepad.blit(TextSurf , TextRect)

        textSurface = SmallText.render(" SUB DEVELOPER : LeeJuHo",True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (windowSize[0]/2,720+t2)
        gamepad.blit(TextSurf , TextRect)

        textSurface = SmallText.render(" TTF FROM : COOKIERUN",True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (windowSize[0]/2,760+t2)
        gamepad.blit(TextSurf , TextRect)

        textSurface = SmallText.render(" IMG FROM : flaticon.com",True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (windowSize[0]/2,780+t2)
        gamepad.blit(TextSurf , TextRect)

        TOF = Button(option_button,430,325+t,163,48,option_button,423,323+t)   # option

        TOF2 = Button(staff_button,430,400+t,163,48,staff_button,423,398+t)   # staff

        #OptionButton = Button(start_button2,445,260,60,20,start_button2,440,258) 
        # #참조 : https://m.blog.naver.com/scyan2011/221998190058

        MUSIC_ON = Button(SOUND_ON,430,-408+t,180,40,SOUND_ON,423,-410+t)   # ON

        
        MUSIC_OFF = Button(SOUND_OFF,430,-335+t,180,40,SOUND_OFF,423,-337+t)   # staff

        TOF3 = Button(quit_button,7,-660+t,163,48,quit_button,0,-662+t)   # Quit

        if TOF3 : done = True

        if MUSIC_ON : MUSIC_TOF = True        
        if MUSIC_OFF : MUSIC_TOF = False


    


        pg.display.update() 

        if t < 680 :
            t+=2
            t1+=5
            if t1 == 510 :
                t1 = 0
        t2+=2
            
        clock.tick (60)







def runGame ():
    global gamepad, clock, daegune1, daegune2, daegune_slide, chair, whiteboard, obj, rnd, piano, crahed_time, t, MUSIC_TOF
    done=False
    daegune_t = 0
    jump_motion = False
    slide_motion = False
    MycharY = 355
    t = 0
    SmallText = pg.font.SysFont( "arial", 30, True, False)
    crahed_time = 0
    crashed = False
    creahsed_time2 = 0
    round_n=0
    while not done:
        for event in pg.event.get ():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.KEYDOWN :
                if event.key == pg.K_SPACE and not jump_motion :
                    jump_motion=True
                    jump_t = 0
                if event.key == pg.K_LCTRL  :
                    slide_motion=True
            if event.type == pg.KEYUP :
                if event.key == pg.K_LCTRL :
                    slide_motion = False

        gamepad.fill((255,255,255))

        if jump_motion :
            MycharY += (jump_t - 19) * 2
            jump_t += 1
            if jump_t == 39 :
                jump_motion = False
                jump_t = 0


        if slide_motion :
            if jump_motion :
                if daegune_t <=9 :
                    gamepad.blit (daegune1,(40,MycharY))
                elif daegune_t <=19 :
                    gamepad.blit (daegune2,(40,MycharY))
                else :
                    daegune_t = -1
                    gamepad.blit (daegune2,(40, MycharY))
            else :
                gamepad.blit (daegune_slide,(40,400))
        else : 
            if daegune_t <=9 :
                gamepad.blit (daegune1,(40,MycharY))
            elif daegune_t <=19 :
                gamepad.blit (daegune2,(40,MycharY))
            else :
                daegune_t = -1
                gamepad.blit (daegune2,(40, MycharY))

        
        L, round_n = rnd.startgame(t)
        
        for e in L :
            gamepad.blit(e[2], (e[0], e[1]))
            if creahsed_time2 == 61 :
                crashed = False
                creahsed_time2 = 0
            if crashed :
                creahsed_time2 += 1
                continue
            if slide_motion and not jump_motion :
                TOF = judge_conflict(40, 265, 400, 580, e[0], e[0] + e[3], e[1], e[1] + e[4]) 
            else:
                TOF = judge_conflict(40, 220, MycharY, MycharY + 225, e[0], e[0] + e[3], e[1], e[1] + e[4]) 
            if TOF :
                crahed_time += 1
                crashed = True
        
        if round_n == 3 :
            done = True
            end()
            break
        
        t += 1
        daegune_t += 1
        
        print_massage = "Time : " + str(round(t/60, 1)) 

        textSurface = SmallText.render(print_massage,True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (120,50)
        gamepad.blit(TextSurf , TextRect)

        print_massage = "crahsed time : " + str(crahed_time) 
        textSurface = SmallText.render(print_massage,True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (120,80)
        gamepad.blit(TextSurf , TextRect)

        #if MUSIC_TOF :
            #sound.play(-1)

        pg.display.update ()
        clock.tick (60)
    pg.quit ()


def end ():
    global crahed_time, t, f, line, white 
    done = False
    #f = open("id.txt", 'w')
    #f.write(id)
    #f.close()
    #id+=1
    id=0
    t_id = 0
    t_time = 0
    t_crash = 0
    t_line = 0
    t_sum = 0
    while not done :
        for event in pg.event.get ():
            if event.type == pg.QUIT:
                done = True

        gamepad.fill((255,255,255))      

        LargeText = pg.font.SysFont( "arial", 40, True, False)

        if id != t_id :
            t_id += 1
        elif round(t/60, 1) != round(t_time,1) :
            t_time += 0.1
        elif round(t_crash, 1) != round(crahed_time, 1):
            t_crash+= 0.1
        elif t_line != 600 :
            t_line += 5
        elif round(t_sum, 1) != round(t/60, 1) + round(crahed_time, 1) :
            t_sum += 0.1
        

        gamepad.blit (line,(210,380))
        gamepad.blit (white,(210+t_line,380))

        textSurface = LargeText.render("YOUR ID : "+str(t_id),True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (500,150)
        gamepad.blit(TextSurf , TextRect)
        
        textSurface = LargeText.render("TIME : "+str(round(t_time,1)),True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (500,320)
        gamepad.blit(TextSurf , TextRect)

        textSurface = LargeText.render("Crashed Time : "+str(round(t_crash,1)),True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (500,370)
        gamepad.blit(TextSurf , TextRect)
        
        textSurface = LargeText.render("Score : "+str(round(t_sum,1)),True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (490,430)
        gamepad.blit(TextSurf , TextRect) 

        if t_sum == 0 :
            gamepad.blit (white,(190,410))

        pg.display.update ()
        clock.tick (60)

    initGame()
    startGame()

initGame ()
startGame()

#git add .
#git commit -m origin
#git push