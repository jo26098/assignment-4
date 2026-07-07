def fib(sequence_num):
    """
    Determines the number at a location in the fibonacci sequence
    given what the location should be.

    Arguments:
    sequence_num (int): The target location in the fibonacci sequence.

    Returns:
    result (int): The number at the given location.
    """
    if sequence_num == 1 or sequence_num == 2:
        return 1
    else:
        a = 1
        b = 1
        location = 2
        while location < sequence_num:
            location += 1
            c = a + b
            a = b
            b = c
        return b

num = int(input())
print(fib(num))