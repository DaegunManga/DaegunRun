import pygame as pg
import OBJpy
import RNDpy
import ATKpy
import random 
import openpyxlpy

windowSize = [1020,680] 

opx = openpyxlpy.load_xl()

id_t = opx.id_return()

L1 = ['교실', '음악실', '미술실', '컴퓨터실', 'AI실', '체육관']


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
    global gamepad, clock,MANGA,id_t, Large_font,font,light_beam, x_mark, opx, atk, graph, graph_button, boss_img, fire, daegune1, daegune2, beam, daegune_slide, chair, whiteboard, obj, rnd, background, option_button, staff_button, quit_button, SOUND_ON, SOUND_OFF, daegunmark, sound, music
    global line, white
    pg.init()
    gamepad = pg.display.set_mode(windowSize)
    pg.display.set_caption("DaeGunRun")
    font = pg.font.Font('./font/CookieRunBlack.ttf',20)
    Large_font = pg.font.Font('./font/CookieRunBlack.ttf',40)

    id_t += 1

    round_L=[]

    daegune1=pg.image.load ('./img/daegune1.gif')
    daegune1 = pg.transform.scale(daegune1,(180,225))

    daegune2=pg.image.load ('./img/daegune2.png')
    daegune2 = pg.transform.scale(daegune2,(180,225))

    daegune_slide=pg.image.load ('./img/daegune_slide.gif')
    daegune_slide = pg.transform.scale(daegune_slide,(225,180))

    option_button=pg.image.load ('./img/obtion_button.png')
    option_button = pg.transform.scale(option_button,(163,48))

    staff_button=pg.image.load ('./img/staff_button.png')
    staff_button = pg.transform.scale(staff_button,(163,48)) 

    graph_button=pg.image.load ('./img/Button_data.png')
    graph_button = pg.transform.scale(graph_button,(163,48)) 

    quit_button=pg.image.load ('./img/Quit_Button.png')
    quit_button = pg.transform.scale(quit_button,(163,48))

    MANGA=pg.image.load ('./img/MANGA.png')
    MANGA = pg.transform.scale(MANGA,(163,48))

    SOUND_OFF=pg.image.load ('./img/ON_PLAY.png')
    SOUND_OFF = pg.transform.scale(SOUND_OFF,(180,40))

    SOUND_ON=pg.image.load ('./img/OFF_PLAY.png')
    SOUND_ON = pg.transform.scale(SOUND_ON,(180,40))

    daegunmark=pg.image.load("./img/Daegun.png")
    daegunmark = pg.transform.scale(daegunmark,(100,100))

    piano=pg.image.load ('./img/piano.png')
    piano = pg.transform.scale(piano,(120,120))

    chair=pg.image.load ('./img/chair.png')
    chair = pg.transform.scale(chair,(80,96))

    music=pg.image.load ('./img/music.png')
    music = pg.transform.scale(music,(360,360))

    roller_paint=pg.image.load ('./img/roller-paint.png')
    roller_paint = pg.transform.scale(roller_paint,(151,128))

    canvas=pg.image.load ('./img/canvas.png')
    canvas = pg.transform.scale(canvas,(309,384))

    computer=pg.image.load ('./img/computer.png')
    computer = pg.transform.scale(computer,(461,360))

    television=pg.image.load ('./img/television.png')
    television = pg.transform.scale(television,(128,128))

    error=pg.image.load ('./img/error-404.png')
    error = pg.transform.scale(error,(128,115))

    ai=pg.image.load ('./img/ai.png')
    ai = pg.transform.scale(ai,(360,360))

    ball=pg.image.load ('./img/basketball.png')
    ball = pg.transform.scale(ball,(128,128))

    beam=pg.image.load ('./img/beam.png') 
    beam = pg.transform.scale(beam,(920,220))

    light_beam=pg.image.load ('./img/light_image_sharp.jpg') 
    light_beam = pg.transform.scale(light_beam,(600,220))

    scoreboard=pg.image.load ('./img/scoreboard.png') 
    scoreboard = pg.transform.scale(scoreboard,(439,360))

    boss_img=pg.image.load ('./img/boss_img.png') 
    boss_img = pg.transform.scale(boss_img,(136,169))

    fire=pg.image.load ('./img/gun.png') 
    fire = pg.transform.scale(fire,(40,40))

    whiteboard=pg.image.load ('./img/whiteboard.png')
    whiteboard = pg.transform.scale(whiteboard,(540,360))

    background=pg.image.load ('./img/background.png')
    background = pg.transform.scale(background,(960,540))

    line=pg.image.load ('./img/line.png') 
    line = pg.transform.scale(line,(600,50))

    white=pg.image.load ('./img/white.png')
    white = pg.transform.scale(white,(600,50))

    x_mark=pg.image.load ('./img/close.png')
    x_mark = pg.transform.scale(x_mark,(50,50))

    graph = pg.image.load('./img/DATA_IMG.png')
    graph = pg.transform.scale(graph, (900, 600))

    round_L.append([[chair, 80, 96, 'down'], [whiteboard, 540, 360, 'up']])
    round_L.append([[piano, 120, 120, 'down'],[music, 360, 360, 'up']])
    round_L.append([[roller_paint, 151, 128, 'down'],[canvas, 309, 384, 'up']])
    round_L.append([[television, 128, 128, 'down'], [computer, 461, 360, 'up']])
    round_L.append([[error, 128, 115, 'down'], [ai, 360, 360, 'up']])
    round_L.append([[ball, 128, 128, 'down'], [scoreboard, 439, 360, 'up']])


    obj = OBJpy.object()
    rnd = RNDpy.round(round_L)
    atk = ATKpy.ATK()

    clock = pg.time.Clock()


def startGame (): #게
    global gamepad, clock, background, option_button, staff_button, MUSIC_TOF
    pg.init()
    done = False 
    t=0
    MUSIC_TOF = True
    gamepad = pg.display.set_mode((1020, 680))
    while not done :
        for event in pg.event.get ():
            if event.type == pg.QUIT:
                done = True
                break
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

        TOF = Button(option_button,430,300,163,48,option_button,423,298)   # option
        
        if TOF : option()

        TOF2 = Button(staff_button,430,360,163,48,staff_button,423,358)   # staff

        if TOF2 : staff()
        if TOF : option()

        TOF3 = Button(graph_button,430,420,163,48,graph_button,423,418)   # graph

        if TOF3 : Graph()



        #OptionButton = Button(start_button2,445,260,60,20,start_button2,440,258) #참조 : https://m.blog.naver.com/scyan2011/221998190058

        pg.display.update() 
        t+=5
        if t == 510 :
            t = 0
            
        clock.tick (60)
    pg.quit()


def Graph() :
    global gamepad, clock, background
    pg.init()
    done = False 
    t=0
    t1=0
    while not done :
        for event in pg.event.get ():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.KEYDOWN :
                if event.key == pg.K_SPACE  :
                    runGame()
        gamepad.fill((255,255,255))
        gamepad.blit(background,(30+t, -50))

        LargeText = pg.font.SysFont( "arial", 40, True, False)
        SmallText = pg.font.SysFont( "arial", 20, True, False)

        if t1 <= 255 :
            textSurface = LargeText.render("PRESS 'SPACE BAR' TO START",True,(0,t1,0))
        else :
            textSurface = LargeText.render("PRESS 'SPACE BAR' TO START",True,(0,510 - t1,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (windowSize[0]/2+t,windowSize[1]*4/5)
        gamepad.blit(TextSurf , TextRect)
        TOF = Button(option_button,430+t,300,163,48,option_button,423+t,298)   # option

        TOF2 = Button(staff_button,430+t,360,163,48,staff_button,423+t,368)   # staff
        
        TOF3 = Button(graph_button,430+t,420,163,48,graph_button,423+t,418)   # graph

        gamepad.blit(graph, (-960+t,20)) #450, 300

        TOF3 = Button(quit_button,-1013+t,2,163,48,quit_button,-1020+t,0)   # Quit

        if TOF3 : done = True

        if t < 1020 :
            t+=2
        t1+=5
        if t1 == 510 :
            t1=0
        pg.display.update() 
        clock.tick (60)


def staff () :
    global gamepad, clock, background, font
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

        textSurface = font.render("MANGA",True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (windowSize[0]/2,900-t)
        gamepad.blit(TextSurf , TextRect)

        textSurface = font.render("담당 T : 권순찬 선생님",True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (windowSize[0]/2,920-t)
        gamepad.blit(TextSurf , TextRect)

        textSurface = font.render("FONT FROM : COOKIERUN",True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (windowSize[0]/2,960-t)
        gamepad.blit(TextSurf , TextRect)

        textSurface = font.render("IMG FROM : flaticon.com",True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (windowSize[0]/2,980-t)
        gamepad.blit(TextSurf , TextRect)

        textSurface = font.render("(C) Copyright in MANGA",True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (windowSize[0]/2,1300-t)
        gamepad.blit(TextSurf , TextRect)

        TOF = Button(option_button,430,300-t,163,48,option_button,423,298-t)   # option

        TOF2 = Button(staff_button,430,360-t,163,48,staff_button,423,358-t)   # staff

        TOF3 = Button(graph_button,430,420-t,163,48,graph_button,423,418-t)   # graph

        TOF3 = Button(quit_button,7,700-t,163,48,quit_button,0,698-t)   # Quit

        if TOF3 : done = True

        gamepad.blit(MANGA,(290, 1100-t)) #1124
        gamepad.blit(x_mark,(496, 1099-t))
        gamepad.blit(daegunmark,(600, 1074-t))

        #OptionButton = Button(start_button2,445,260,60,20,start_button2,440,258) #참조 : https://m.blog.naver.com/scyan2011/221998190058
        if t < 680 :
            t+=2
        t1+=5
        if t1 == 510 :
            t1=0
        pg.display.update() 

            
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

        TOF = Button(option_button,430,300+t,163,48,option_button,423,298+t)   # option

        TOF2 = Button(staff_button,430,360+t,163,48,staff_button,423,358+t)   # staff

        TOF3 = Button(graph_button,430,420+t,163,48,graph_button,423,418+t)   # graph

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

        
        L, round_n, a = rnd.startgame(t)
        if a :
            gamepad.fill((255,0,0))
        
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
        
        if round_n == 6 :
            done = True
            boss()
            break
        
        t += 1
        daegune_t += 1

        print_massage = "장소 : " + str(L1[round_n]) 
        textSurface = font.render(print_massage,True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (120,50)
        gamepad.blit(TextSurf , TextRect)


        print_massage = "crahsed time : " + str(crahed_time) 
        textSurface = font.render(print_massage,True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (120,80)
        gamepad.blit(TextSurf , TextRect)

        #if MUSIC_TOF :
            #sound.play(-1)

        pg.display.update ()
        clock.tick (60)


def boss () :
    global gamepad, clock, crahed_time, t
    done=False
    Boss_Y = 0
    shoot = False
    jump_motion=False
    slide_motion=False
    daegune_t=0
    MycharY = 355
    health = 200
    Boss_t = False 
    boss_t = 0
    Beam_Y=0
    crashed = False
    crahed_t = 0
    SmallText = pg.font.SysFont( "arial", 30, True, False)
    t=0
    while not done:
        shoot = False
        for event in pg.event.get ():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.KEYDOWN :
                if event.key == pg.K_SPACE and not jump_motion :
                    jump_motion=True
                    jump_t = 0
                if event.key == pg.K_LCTRL  :
                    slide_motion=True
                if event.key == pg.K_w :
                    shoot=True
            if event.type == pg.KEYUP :
                if event.key == pg.K_LCTRL :
                    slide_motion = False

        gamepad.fill((255,255,255)) #걍 뜬다고?

        if jump_motion :
            MycharY += (jump_t - 19) * 2
            jump_t += 1
            if jump_t == 39 :
                jump_motion = False
                jump_t = 0

        ATK_L = atk.move_ATK()
        if Boss_t :
            boss_t += 1
            if not crashed and 30 < boss_t:           
                if slide_motion and not jump_motion :
                    TOF = judge_conflict(40, 265, 400, 580, 0, 920, Beam_Y, Beam_Y + 220) 
                else:
                    TOF = judge_conflict(40, 220, MycharY, MycharY + 225, 0, 920, Beam_Y, Beam_Y + 220)
                if TOF : 
                    crahed_time += 1 
                    crashed = True  
            if boss_t <= 30 :
                gamepad.blit(light_beam, (300, Beam_Y)) 
            elif boss_t <= 45 :
                gamepad.blit(beam, (0, Beam_Y))
            else :
                Boss_t = False 
                boss_t = 0
        for L in ATK_L :
            gamepad.blit(fire, (L[0], L[1]))


        for L in ATK_L :
            TOF = judge_conflict(900, 1036, Boss_Y, Boss_Y + 169, L[0], L[0] + 40, L[1], L[1] + 40) 
            if TOF : #judge_conflict(40, 265, 400, 580, e[0], e[0] + e[3], e[1], e[1] + e[4]) 
                health -= 5
                atk.del_ATK(L)

        if Boss_Y == 0 or Boss_Y == 412 or Boss_Y == 150:
            n = random.randint(0, 1)        
            if n == 1 :
              Boss_t = True 
              Beam_Y = Boss_Y
            else :
                continue
        

        if Boss_Y <= 411 :
            gamepad.blit(boss_img, (900, Boss_Y))
        else :
            gamepad.blit(boss_img, (900, 822-Boss_Y))

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

        if shoot :
            if slide_motion and not jump_motion :
                atk.create_ATK(265 , MycharY + 70)
            else :
                atk.create_ATK(220 , MycharY + 92)
        
        if crashed :
            crahed_t+= 1
        if crahed_t == 61 :
            crashed = False
            crahed_t = 0
                
        Boss_Y += 2
        if Boss_Y == 822 :
            Boss_Y = 0

        # 136,169 보스
        t += 1
        daegune_t += 1
        print_massage = "Time : " + str(round(t/60, 1)) 

        textSurface = font.render(print_massage,True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (120,50)
        gamepad.blit(TextSurf , TextRect)

        print_massage = "crahsed time : " + str(crahed_time) 
        textSurface = font.render(print_massage,True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (120,80)
        gamepad.blit(TextSurf , TextRect)

        print_massage = "health : " + str(health) 
        textSurface = font.render(print_massage,True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (120,110)
        gamepad.blit(TextSurf , TextRect)

        if health == 0 :
            end()
            break
        pg.display.update()             
        clock.tick (60)


def end ():
    global crahed_time, t, f, line, white 
    done = False
    opx.save_value(id_t, round(t/60, 1) + crahed_time)
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

        if id_t != t_id :
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

        textSurface = Large_font.render("YOUR ID : "+str(t_id),True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (500,150)
        gamepad.blit(TextSurf , TextRect)
        
        textSurface = Large_font.render("TIME : "+str(round(t_time,1)),True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (500,320)
        gamepad.blit(TextSurf , TextRect)

        textSurface = Large_font.render("Crashed Time : "+str(round(t_crash,1)),True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (500,370)
        gamepad.blit(TextSurf , TextRect)
        
        textSurface = Large_font.render("Score : "+str(round(t_sum,1)),True,(0,0,0))
        TextSurf , TextRect = textSurface ,textSurface.get_rect ()
        TextRect.center = (490,430)
        gamepad.blit(TextSurf , TextRect) 

        if t_sum == 0 :
            gamepad.blit (white,(190,410))
        TOF3 = Button(quit_button,7,10,163,48,quit_button,0,8)   # Quit

        if TOF3 : 
            break
        pg.display.update ()
        clock.tick (180)
    
    opx.save_Data_IMG()

    initGame()
    startGame()

initGame ()
startGame()

#git add .
#git commit -m origin
#git push
