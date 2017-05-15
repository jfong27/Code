
def main():
    cases = int(input())

    for i in range(1, cases + 1):
        case = input()
        stalls,people = case.split()
        ans = solve(int(stalls), int(int(people)/2))
        s = "Case #" + repr(i) + "(" + repr(stalls) + repr(people) +"):"
        counter = 0

        print(s,ans[0], ans[1])


def solve(stalls, levels):
    if stalls%2 == 0:
        a = stalls/2
        b = (stalls/2)-1
    else:
        a = (stalls-1)/2
        b = (stalls-1)/2

    
    if 0 >= levels:
        return a,b
    else:
        return solve(a,levels-1),solve(b, levels-2)
        


def divide(stalls):
    if stalls % 2 == 0:
        a = stalls/2
        b = (stalls/2) - 1
    else:
        a = (stalls-1)/2
        b = (stalls-1)/2
    
    return a,b


if __name__ == '__main__':
    main()
