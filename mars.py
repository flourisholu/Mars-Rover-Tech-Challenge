"""
Author: Flourish Oluwamakinde
Date: 23 June 2022
Challenge name: Mars Rover Technical Challenge

This solution takes in three inputs: upper-right coordinates of plateau on Mars, 
the rover's position (made up of two integers and a letter), and a series of instructions
telling the rover how to explore the plateau.

L = turn 90 degrees left without moving from current spot
R = turn 90 degrees right without moving from current spot
M = move forward one grid point and maintain the same heading

upperRCoord, roverPosition, exploreInstructions
"""
def main():
    # Get coordinates and rover's information
    upperRCoord = input('Enter upper-right coordinates: ')
    roverPosition = input('Enter rover\'s position: ')
    exploreInstructions = input('Enter series of instructions: ')
        
    # Store information in arrays
    arrayURCoord = upperRCoord.split(' ')
    print('The plateau\'s upper-right coordinates are: ', arrayURCoord)
    arrayRoverPosition = roverPosition.split(' ')
    print('The rover\'s position is: ', arrayRoverPosition)
    arrayInstructions = list(exploreInstructions)
    print('The instructions for the rover\'s movements are: ', arrayInstructions)
    
    # Store coordinates in new variables for easy use
    xCoord = int(arrayRoverPosition[0])
    yCoord = int(arrayRoverPosition[1])
    direction = arrayRoverPosition[2]
    xUpperRight = int(arrayURCoord[0])
    yUpperRight = int(arrayURCoord[1])
    
    # Determine how the rover moves
    size = len(arrayInstructions)
    # If the rover in facing North initially
    if direction == 'N':
        for i in range(size):
            if arrayInstructions[i] == 'L':
                if direction == 'N':
                    direction = 'W'
                    arrayRoverPosition[2] = direction #update array
                elif direction == 'S':
                    direction = 'E'
                    arrayRoverPosition[2] = direction #update array
                elif direction == 'E':
                    direction = 'N'
                    arrayRoverPosition[2] = direction #update array
                elif direction == 'W':
                    direction = 'S'
                    arrayRoverPosition[2] = direction #update array
            elif arrayInstructions[i] == 'R':
                if direction == 'N':
                    direction = 'E'
                    arrayRoverPosition[2] = direction #update array
                elif direction == 'S':
                    direction = 'W'
                    arrayRoverPosition[2] = direction #update array
                elif direction == 'E':
                    direction = 'S'
                    arrayRoverPosition[2] = direction #update array
                elif direction == 'W':
                    direction = 'N'
                    arrayRoverPosition[2] = direction #update array
            elif arrayInstructions[i] == 'M':
                # Check to see that we are not moving beyond the boundary then move it one grid space
                if xCoord <= xUpperRight and yCoord <= yUpperRight and direction == 'N':
                    yCoord = yCoord + 1
                    arrayRoverPosition[1] = yCoord
                elif xCoord <= xUpperRight and yCoord <= yUpperRight and direction == 'S':
                    yCoord = yCoord - 1
                    arrayRoverPosition[1] = yCoord
                elif xCoord <= xUpperRight and yCoord <= yUpperRight and direction == 'E':
                    xCoord = xCoord + 1
                    arrayRoverPosition[0] = xCoord
                elif xCoord <= xUpperRight and yCoord <= yUpperRight and direction == 'W':
                    xCoord = xCoord - 1
                    arrayRoverPosition[0] = xCoord
                elif xCoord > xUpperRight or yCoord > yUpperRight:
                    print('Error! You\'re going to far.')                
        print('The rover\'s final position is: ', arrayRoverPosition)
 
    # If the rover in facing South initially    
    elif direction == 'S':
        for i in range(size):
            if arrayInstructions[i] == 'L':
                if direction == 'N':
                    direction = 'W'
                    arrayRoverPosition[2] = direction #update array
                elif direction == 'S':
                    direction = 'E'
                    arrayRoverPosition[2] = direction #update array
                elif direction == 'E':
                    direction = 'N'
                    arrayRoverPosition[2] = direction #update array
                elif direction == 'W':
                    direction = 'S'
                    arrayRoverPosition[2] = direction #update array
            elif arrayInstructions[i] == 'R':
                if direction == 'N':
                    direction = 'E'
                    arrayRoverPosition[2] = direction #update array
                elif direction == 'S':
                    direction = 'W'
                    arrayRoverPosition[2] = direction #update array
                elif direction == 'E':
                    direction = 'S'
                    arrayRoverPosition[2] = direction #update array
                elif direction == 'W':
                    direction = 'N'
                    arrayRoverPosition[2] = direction #update array
            elif arrayInstructions[i] == 'M':
                # Check to see that we are not moving beyond the boundary then move it one grid space
                if xCoord <= xUpperRight and yCoord <= yUpperRight and direction == 'N':
                    yCoord = yCoord + 1
                    arrayRoverPosition[1] = yCoord
                elif xCoord <= xUpperRight and yCoord <= yUpperRight and direction == 'S':
                    yCoord = yCoord - 1
                    arrayRoverPosition[1] = yCoord
                elif xCoord <= xUpperRight and yCoord <= yUpperRight and direction == 'E':
                    xCoord = xCoord + 1
                    arrayRoverPosition[0] = xCoord
                elif xCoord <= xUpperRight and yCoord <= yUpperRight and direction == 'W':
                    xCoord = xCoord - 1
                    arrayRoverPosition[0] = xCoord
                elif xCoord > xUpperRight or yCoord > yUpperRight:
                    print('Error! You\'re going to far.')                
        print('The rover\'s final position is: ', arrayRoverPosition)
    
    # If the rover in facing East initially   
    elif direction == 'E':
        for i in range(size):
            if arrayInstructions[i] == 'L':
                if direction == 'N':
                    direction = 'W'
                    arrayRoverPosition[2] = direction #update array
                elif direction == 'S':
                    direction = 'E'
                    arrayRoverPosition[2] = direction #update array
                elif direction == 'E':
                    direction = 'N'
                    arrayRoverPosition[2] = direction #update array
                elif direction == 'W':
                    direction = 'S'
                    arrayRoverPosition[2] = direction #update array
            elif arrayInstructions[i] == 'R':
                if direction == 'N':
                    direction = 'E'
                    arrayRoverPosition[2] = direction #update array
                elif direction == 'S':
                    direction = 'W'
                    arrayRoverPosition[2] = direction #update array
                elif direction == 'E':
                    direction = 'S'
                    arrayRoverPosition[2] = direction #update array
                elif direction == 'W':
                    direction = 'N'
                    arrayRoverPosition[2] = direction #update array
            elif arrayInstructions[i] == 'M':
                # Check to see that we are not moving beyond the boundary then move it one grid space
                if xCoord <= xUpperRight and yCoord <= yUpperRight and direction == 'N':
                    yCoord = yCoord + 1
                    arrayRoverPosition[1] = yCoord
                elif xCoord <= xUpperRight and yCoord <= yUpperRight and direction == 'S':
                    yCoord = yCoord - 1
                    arrayRoverPosition[1] = yCoord
                elif xCoord <= xUpperRight and yCoord <= yUpperRight and direction == 'E':
                    xCoord = xCoord + 1
                    arrayRoverPosition[0] = xCoord
                elif xCoord <= xUpperRight and yCoord <= yUpperRight and direction == 'W':
                    xCoord = xCoord - 1
                    arrayRoverPosition[0] = xCoord
                elif xCoord > xUpperRight or yCoord > yUpperRight:
                    print('Error! You\'re going to far.')                
        print('The rover\'s final position is: ', arrayRoverPosition)
    
    # If the rover in facing West initially
    elif direction == 'W':
        for i in range(size):
            if arrayInstructions[i] == 'L':
                if direction == 'N':
                    direction = 'W'
                    arrayRoverPosition[2] = direction #update array
                elif direction == 'S':
                    direction = 'E'
                    arrayRoverPosition[2] = direction #update array
                elif direction == 'E':
                    direction = 'N'
                    arrayRoverPosition[2] = direction #update array
                elif direction == 'W':
                    direction = 'S'
                    arrayRoverPosition[2] = direction #update array
            elif arrayInstructions[i] == 'R':
                if direction == 'N':
                    direction = 'E'
                    arrayRoverPosition[2] = direction #update array
                elif direction == 'S':
                    direction = 'W'
                    arrayRoverPosition[2] = direction #update array
                elif direction == 'E':
                    direction = 'S'
                    arrayRoverPosition[2] = direction #update array
                elif direction == 'W':
                    direction = 'N'
                    arrayRoverPosition[2] = direction #update array
            elif arrayInstructions[i] == 'M':
                # Check to see that we are not moving beyond the boundary then move it one grid space
                if xCoord <= xUpperRight and yCoord <= yUpperRight and direction == 'N':
                    yCoord = yCoord + 1
                    arrayRoverPosition[1] = yCoord
                elif xCoord <= xUpperRight and yCoord <= yUpperRight and direction == 'S':
                    yCoord = yCoord - 1
                    arrayRoverPosition[1] = yCoord
                elif xCoord <= xUpperRight and yCoord <= yUpperRight and direction == 'E':
                    xCoord = xCoord + 1
                    arrayRoverPosition[0] = xCoord
                elif xCoord <= xUpperRight and yCoord <= yUpperRight and direction == 'W':
                    xCoord = xCoord - 1
                    arrayRoverPosition[0] = xCoord
                elif xCoord > xUpperRight or yCoord > yUpperRight:
                    print('Error! You\'re going to far.')                
        print('The rover\'s final position is: ', arrayRoverPosition)
main()