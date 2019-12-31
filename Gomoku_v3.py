from collections import deque
import numpy as np

size = 15
win = 5
stack = 8
    
def init():
    global t
    global l
    global b
    t = 0
    l = deque(maxlen=stack)
    b = [['.' for _ in range(size)] for _ in range(size)]
    for _ in range(stack):
        l.append([['.' for _ in range(size)] for _ in range(size)])


def read_b_bin(ob):
    base = np.zeros((size,size))
    for i in range(len(ob)):
        for ii in range(len(ob[i])):
            if ob[i][ii] == 'o':
                base[i][ii] = 1
    return base
                
def read_w_bin(ob):
    base = np.zeros((size,size))
    for i in range(len(ob)):
        for ii in range(len(ob[i])):
            if ob[i][ii] == 'x':
                base[i][ii] = 1
    return base

def get_state():
    global l
    state = []
    for iii in l:
        state.append(read_b_bin(iii))
        state.append(read_w_bin(iii))
    state.append([[t for _ in range(size)] for _ in range(size)])
    return np.array(state)

def render():
    for i in b:
        print(*i)
    for _ in range(5):
        print('')

def step(x, y):
    global t
    global l
    global b
    if b[x][y] != '.':
        return check_win()
    
    if t == 0:
        b[x][y] = 'o'
        t = 1
    else:
        b[x][y] = 'x'
        t = 0
    l.append(b)
    return check_win()

def check_win():
    global b
    b_succ = []
    w_succ = []
    for x in range(len(b)):
        for y in range(len(b[x])):
            try:
                s = []
                for i in range(win):
                    s.append(b[x+i][y+i])
                b_succ.append(s==['o' for _ in range(win)])
                w_succ.append(s==['x' for _ in range(win)])

            except:
                pass
            
            try:
                s = []
                for i in range(win):
                    s.append(b[x+i][y-i])
                b_succ.append(s==['o' for _ in range(win)])
                w_succ.append(s==['x' for _ in range(win)])

            except:
                pass
            
            try:
                s = []
                for i in range(win):
                    s.append(b[x][y+i])
                b_succ.append(s==['o' for _ in range(win)])
                w_succ.append(s==['x' for _ in range(win)])

            except:
                pass
            
            try:
                s = []
                for i in range(win):
                    s.append(b[x+i][y])
                b_succ.append(s==['o' for _ in range(win)])
                w_succ.append(s==['x' for _ in range(win)])
            except:
                pass
        

    return any(b_succ), any(w_succ)


#+++++++++++++++++++++++++++++++++Usage++++++++++++++++++++++++++++++++++++++++++++++
for _ in range(10):
    ww = False
    bw = False
    init()
    render()
    while not (bw or ww):
        get_state()
        x = int(input('x? '))
        y = int(input('y? '))
        bw, ww = step(x, y)
        render()
