

def main():
    cases = int(input())

    for i in range(1, cases+1):
        case = input()
        stalls,people = case.split()
        ans = solve(int(stalls),int(people))
        s = "Case #" + repr(i) + ":"
        print(s, ans)

def solve(num_stalls, people):
    stalls = []

    stalls.append(Stall(0, num_stalls, True))
    for i in range(0, num_stalls):
        stalls.append(Stall(0,0, False))
    stalls.append(Stall(num_stalls, 0, True))

    update_spaces(stalls)

    for j in range(0, people):
        choose_stall(stalls)


def choose_stall(stalls):
    possible = []
    for stall in stalls:
        if stall.occupied == False:
            possible.append(stall)

    possible2 = []
    num_pos = 0
    for stall in possible:
        min(stall.L, stall.R)

    print(mins)


def update_spaces(stalls):
    for i in range(1, len(stalls)-1):
        stalls[i].L = check_l(stalls, i)
        stalls[i].R = check_r(stalls,i)


def check_l(stalls, i):
    count = 0
    for j in range(i, -1, -1):
        if stalls[j-1].occupied or j < 0:
            return count
        count += 1

def check_r(stalls, i):
    count = 0
    for j in range(i, len(stalls)-1):
        if stalls[j+1].occupied:
            return count
        count += 1
    

class Stall: 
    def __init__(self, L, R, occupied):
        self.L = L
        self.R = R
        self.occupied = occupied 



if __name__ == '__main__':
    main()
