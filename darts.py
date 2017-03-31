# darts.py
# a dart scoring simulation

from graphics import *
import math

score = 0
scoreboard = Text(Point(65, 35), 'Score: {0}'.format(score))

def init():
    win = GraphWin('Darts!', 800, 500)
    win.setCoords(0.0, 0.0, 80.0, 50.0)
    ctr = Point(25, 25)
    drawBoard(win, ctr)
    handler(win, ctr)

def drawBoard(window, center):
    global score, scoreboard
    colors = ['white', 'black', 'blue', 'red', 'yellow']
    Rectangle(Point(55, 5), Point(75, 45)).draw(window)
    Text(Point(65, 40), "Click on the dartboard 5 times \n and see what your score is.").draw(window)
    scoreboard.draw(window)
    for c in range(len(colors)):
        circles = Circle(center, .05 * window.getHeight() - 5 * c)
        circles.setFill(colors[c])
        circles.draw(window)

def handler(window, center):
    for i in range(5):
        click = window.getMouse()
        score = scoreKeeper(click, center)
        scoreboard.setText('Score: {0}'.format(score))
    done_message = Text(Point(65, 25), 'Your darts score would be \n {0} in 5 attempts'.format(score)).draw(window)
    button = Text(Point(65, 18), 'Exit').draw(window)
    Rectangle(Point(62, 20), Point(68, 16)).draw(window)
    window.getMouse()
    window.close()

def dist(p1, p2):
    p1x, p1y = p1.getX(), p1.getY()
    p2x, p2y = p2.getX(), p2.getY()
    return math.sqrt(((p2x - p1x) ** 2) + ((p2y - p1y) ** 2))

def scoreKeeper(click, center):
    length = dist(click, center)
    global score
    if length <= 25 and length > 20:
        score += 1
        return score
    elif length <= 20 and length > 15:
        score += 3
        return score
    elif length <= 15 and length > 10:
        score += 5
        return score
    elif length <= 10 and length > 5:
        score += 7
        return score
    elif length <= 5:
        score += 9
        return score
    else:
        print('sorry, no score')
