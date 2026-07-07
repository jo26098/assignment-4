def fall_distance(seconds):
    """
    Calculates the distance in meters that an object has fallen given 
    the amount of time in seconds that it's been falling.

    Arguments: 
        seconds (float): The amount of time fallen in seconds.

    Returns:
        distance (float): The distance in meters that the object has
        fallen.
    """
    distance = (1/2)*9.8*(seconds**2)
    return distance

#seconds = float(input("Enter a number of seconds: "))
#distance = fall_distance(seconds)
#print("The object has fallen", distance, "meters.")