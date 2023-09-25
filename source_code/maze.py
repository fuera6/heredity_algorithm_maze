#maze.py

import turtle as t
import heredityAlgorithm as ha

mainx = -100; mainy = -50
subx1 = 120 ; suby1 = 150 ; subx2 = 120 ; suby2 = -50

t.speed(10000)
def makeMazeShape(): #미로 틀 생성
    t.pensize(3)
    t.color("black")
    t.penup()
    t.goto(mainx-200, mainy+200)
    t.pendown()
    t.forward(400)
    t.right(90)
    t.forward(350)
    t.penup()
    t.forward(50)
    t.pendown()
    t.right(90)
    t.forward(400)
    t.right(90)
    t.forward(350)
    t.right(180)
    t.penup()
    t.goto(subx1, suby1)
    t.pendown()
    t.left(90)
    t.forward(160)
    t.right(90)
    t.forward(140)
    t.penup()
    t.forward(20)
    t.pendown()
    t.right(90)
    t.forward(160)
    t.right(90)
    t.forward(140)
    t.right(180)
    t.penup()
    t.goto(subx2, suby2)
    t.pendown()
    t.left(90)
    t.forward(160)
    t.right(90)
    t.forward(140)
    t.penup()
    t.forward(20)
    t.pendown()
    t.right(90)
    t.forward(160)
    t.right(90)
    t.forward(140)
    t.right(180)
    t.penup()
    t.goto(170, -30)
    t.write("보조미로1", font = ("배달의민족 한나체 Pro 보통", 10))
    t.goto(170, -230)
    t.write("보조미로2", font = ("배달의민족 한나체 Pro 보통", 10))
    t.goto(-190, 200)
    t.write("**노란색: aa / 초록색: Aa / 파란색: AA**", font = ("배달의민족 한나체 Pro 보통", 14))
    t.goto(-192, 180)
    t.write("**유전자형이 Aa일 때 벽이 생성됩니다.**", font = ("배달의민족 한나체 Pro 보통", 14))


def makeNewMaze(list):
    t.color("brown")
    t.penup()
    x = mainx-200
    y = mainy+200
    nownum = 0
    for k in range(8):
        for i in range(7):
            x = x+50
            if(list[nownum+i] == 1):
                t.goto(x, y)
                t.pendown()
                t.forward(50)
                t.penup()
        nownum += 7
        if k == 7:
            break
        y = y-50
        x = mainx-200
        t.left(90)
        for i in range(8):
            if(list[nownum+i] == 1):
                t.goto(x, y)
                t.pendown()
                t.forward(50)
                t.penup()
            x += 50
        nownum += 8
        x = mainx-200
        t.right(90)
    t.color("black")

def changemazesub1(individual1) :
    t.color("brown")
    t.penup()
    x = subx1; y = suby1
    nownum = 0
    for k in range(8):
        for i in range(7):
            x = x+20
            t.color(setcolor(individual1[1][nownum+i], individual1[0][nownum+i]))
            t.goto(x, y)
            t.pendown()
            t.forward(20)
            t.penup()
        nownum += 7
        if k == 7:
            break
        y = y-20
        x = x-140
        t.left(90)
        for i in range(8):
            t.color(setcolor(individual1[1][nownum+i], individual1[0][nownum+i]))
            t.goto(x, y)
            t.pendown()
            t.forward(20)
            t.penup()
            x += 20
        nownum += 8
        x = x-160
        t.right(90)
    t.color("black")

def changemazesub2(individual2) :
    t.color("brown")
    t.penup()
    x = subx2; y = suby2
    nownum = 0
    for k in range(8):
        for i in range(7):
            x = x+20
            t.color(setcolor(individual2[1][nownum+i], individual2[0][nownum+i]))
            t.goto(x, y)
            t.pendown()
            t.forward(20)
            t.penup()
        nownum += 7
        if k == 7:
            break
        y = y-20
        x = x-140
        t.left(90)
        for i in range(8):
            t.color(setcolor(individual2[1][nownum+i], individual2[0][nownum+i]))
            t.goto(x, y)
            t.pendown()
            t.forward(20)
            t.penup()
            x += 20
        nownum += 8
        x = x-160
        t.right(90)
    t.color("black")

def setcolor(first, second) :
    str1 = "yellow"
    str2 = "green"
    str3 = "blue"
    if first == 0 and second == 0:
        return str1
    if first != second :
        return str2
    if first == 1 and second == 1:
        return str3

def changemaze(list):
    t.color("brown")
    t.penup()
    x = mainx-200
    y = mainy+200
    nownum = 0
    for k in range(8):
        for i in range(7):
            x = x+50
            if(list[nownum+i] == 1):
                t.goto(x, y)
                t.pendown()
                t.forward(50)
                t.penup()
        nownum += 7
        if k == 7:
            break
        y = y-50
        x = mainx-200
        t.left(90)
        for i in range(8):
            if(list[nownum+i] == 1):
                t.goto(x, y)
                t.pendown()
                t.forward(50)
                t.penup()
            x += 50
        nownum += 8
        x = mainx-200
        t.right(90)
    t.color("black")

def checkright(x, y, movedirct, list) :
    placex = int((-mainx+x+200)/50)
    placey = int(((-mainy+y)*(-1) + 200)/50)
    if movedirct == '1':
        if x == mainx+175 or list[placex + placey*15] == 1:
            return 0
    if movedirct == '2':
        if x == mainx-175 or list[placex+placey*15-1] == 1:
            return 0
    if movedirct == '3':
        if y == mainy+175 or list[placex+placey*15-8] == 1:
            return 0
    if movedirct == '4':
        if y == mainy-175 or list[placex+placey*15+7] == 1:
            return 0
    return 1

def main():
    t.title("유전 알고리즘 미로게임")
    t.hideturtle()
    t.color("black")
    t.penup()
    t.goto(-240, 70)
    t.write("유전 알고리즘 미로게임", font = ("배달의민족 한나체 Pro 보통", 36, "bold"))
    t.goto(-140, 30)
    t.write("시행을 Shell에 입력해주세요", font = ("배달의민족 한나체 Pro 보통", 18, "bold"))
    t.goto(-60, -10)
    t.write("1. 게임하기", font = ("배달의민족 한나체 Pro 보통", 16))
    t.goto(-60, -40)
    t.write("2. 게임 규칙", font = ("배달의민족 한나체 Pro 보통", 16))
    t.goto(-60, -70)
    t.write("3. 종료", font = ("배달의민족 한나체 Pro 보통", 16))

    print("===유전 알고리즘 미로게임===")
    while 1:
        print("1. 게임하기")
        print("2. 게임 규칙")
        print("3. 종료")
        choice = int(input("입력: "))
        if choice == 1:
            break
        elif choice == 2:
            print()
            print("게임규칙은 다음과 같습니다.")
            print("[미로]")
            print("1. 러너(runner)는 하루에 6번씩만 미로의 한 칸을 이동할 수 있습니다.")
            print("2. 밤이 끝날 때마다 미로는 재배치됩니다.")
            print("3. 최대한 빨리 미로를 탈출해야 합니다.")
            print("[전략]")
            print("1. 오른쪽 보조미로는 두 미로의 유전자형을 색깔로 나타낸 것이며, 위의 보조미로가 현재 주 미로입니다.")
            print("2. 미로의 유전자형에는 AA, Aa, aa가 있으며, 각각 파란색, 초록색, 노란색으로 나타납니다.")
            print("3. 유전자형이 Aa인 개체만 벽이 나타납니다.")
            print("4. 미로의 재배치는 오른쪽 보조 미로 2개의 교배로 나타납니다.")
            print("5. 보조미로의 유전자형을 통해 다음 미로의 배치를 예상할 수 있습니다.")
            input("아무거나 입력하면 메뉴로 돌아갑니다.")
            print()
        elif choice == 3:
            print()
            print("게임을 종료합니다.")
            return
        else:
            print("다시 입력해주세요.")

    print()
    print("===게임 시작===")

    t.clear()
    t.bgcolor("gray")
    t.shape("circle")
    t.hideturtle()
    makeMazeShape()
    
    pop = ha.createNewRandomPopulation()
    individual = ha.selectIndividual(pop)
    pheno = ha.phenotype(pop[0])
    makeNewMaze(pheno)
    changemazesub1(pop[0])
    changemazesub2(individual)

    movecnt = 0
    day=0
    x = mainx-175
    y = mainy+175
    
    while 1 :
        t.goto(x, y)
        t.showturtle()

        if movecnt%6==0:
            day+=1
            t.goto(-90, 230)
            t.write("[%d번째 날]" %day, font = ("배달의민족 한나체 Pro 보통", 24))
            t.goto(x,y)
            print()
            print("***%d번째 날이 밝았습니다.***" %day)
            print()
            print("[아침 8시]")
            t.bgcolor("white")
        elif movecnt%6==1:
            print()
            print("[낮 12시]")
        elif movecnt%6==2:
            print()
            print("[오후 4시]")
        elif movecnt%6==3:
            print()
            print("[저녁 8시]")
            t.bgcolor("gray")
        elif movecnt%6==4:
            print()
            print("[밤 12시]")
        elif movecnt%6==5:
            print()
            print("[새벽 4시]")
        
        while 1:
            n = input("어떻게 움직입니까? 1.오른쪽 / 2.왼쪽 / 3.위쪽/ 4.아래쪽 / 5.움직이지 않음")
            if n != '1' and n != '2' and n != '3' and n != '4' and n!='5':
                print("다시 입력해주세요.")
                print()
                continue
                
            if checkright(x, y, n, pheno) == 0:
                print("움직임이 불가능합니다. 다시 입력해주세요.")
                print()
                continue
            else:
                if n == '1':
                    x += 50
                if n == '2':
                    x -= 50
                if n == '3':
                    y += 50
                if n == '4':
                    y -= 50
                movecnt += 1
                break

        if x == mainx+175 and y == mainy-175:
            t.goto(x, y)
            print()
            
            print("===게임 종료===")
            if (movecnt-1)%6==0:
                print("기록: %d번째 날 아침 8시 탈출" %day)
                return
            elif (movecnt-1)%6==1:
                print("기록: %d번째 날 낮 12시 탈출" %day)
                return
            elif (movecnt-1)%6==2:
                print("기록: %d번째 날 오후 4시 탈출" %day)
                return
            elif (movecnt-1)%6==3:
                print("기록: %d번째 날 저녁 8시 탈출" %day)
                return
            elif (movecnt-1)%6==4:
                print("기록: %d번째 날 밤 12시 탈출" %day)
                return
            elif (movecnt-1)%6==5:
                print("기록: %d번째 날 새벽 4시 탈출" %day)
                return

        if movecnt%6 == 0:
            print()
            print("미로 재배치중...")
            print()
            t.hideturtle()
            pop = ha.createNextPopulation(pop)
            individual = pop[0]
            individualb = ha.selectIndividual(pop)
            pheno = ha.phenotype(pop[0])
            t.clear()
            t.right(270)
            makeMazeShape()
            changemaze(pheno)
            changemazesub1(pop[0])
            changemazesub2(individualb)
            t.goto(x, y)
            t.showturtle()

main()
