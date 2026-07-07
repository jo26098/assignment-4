def hailstone(start):
    """
    Determines the number of steps it takes to reach 1 in the hailstone
    sequence given a starting number.

    Arguments:
    start (int): The starting number in the hailstone sequence.

    Returns:
    steps (int): The number of steps it took to get to 1.
    """
    steps = 0
    num = start
    while num > 1:
        steps +=1
        if num % 2 == 0:
            num = num / 2
        else:
            num = (num * 3) + 1
    return(steps)

    

#result = int(input())
#print(hailstone(result))