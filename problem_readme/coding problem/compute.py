import sys

def main():
    threshold = int(sys.argv[1])
    limit = int(sys.argv[2])


    cumulative = 0
    isLimitHit = False;

    for i in range(0, 101):
        inputnum = float(input())

        output = 0
        if(inputnum > threshold):
            output = inputnum - threshold
        
        if(not isLimitHit):
            cumulative += output
        
        if(cumulative > limit and not isLimitHit):
            isLimitHit = True
            cumulative -= output
            output = limit - cumulative
            print(output)
        elif isLimitHit:
            print(0)
        else:
            print(output)
    
    if(isLimitHit):
        print(limit)
    else:
        print(cumulative)


if __name__=="__main__":
    main()
