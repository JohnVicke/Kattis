import sys

testCase = input()

def baseCase(testCase):
    previous = testCase[0]
    i = 0
    for c in testCase:
        if(previous is c):
            i += 1

    if(i is len(testCase)):
        print(1)
        sys.exit(0)

def solveProblem(period, testCase):
    print("before loop")
    j = len(period) - 1
    for c in testCase[len(period): (len(period) + len(period))]:
        print(c)
        if(period[j] is not c):
            print(1)
            sys.exit(0)
        if(j is 0):
            j+=1
        elif(j is len(period) -1):
            j -= 1
        else:
            j = 0


def findPeriodicString(testCase):
    i = 0
    previous = testCase[0]
    period = previous

    for c in testCase:
        if(c is not previous and c not in period):
            period += c

    return period

baseCase(testCase)
period = findPeriodicString(testCase)

if(len(period) is len(testCase)):
    print(len(period))
else:
    solveProblem(period, testCase)
    print(len(period))
