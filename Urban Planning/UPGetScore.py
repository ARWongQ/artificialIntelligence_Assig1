import UPParser;


# noinspection PyRedundantParentheses
def getElementsInMDist(mapToScore, row, col, dist): #map, 0, 0, 2
    #dist += 1; #this is here because the curC for loop would terminate immediately otherwise, same with curR but at a different time
    elementsFound = [];
    maxRow = len(mapToScore);
    maxCol = len(mapToScore[0]);

    for curR in range((-1 * dist), (1 * dist) + 1, 1):
        for curC in range(((-1 * dist) + abs(curR)), ((1 * dist) - abs(curR)) + 1, 1):
            coordR = row + curR;
            coordC = col + curC;
            if (0 <= coordR < maxRow and 0 <= coordC < maxCol):
                if (not (coordR == row and coordC == col)):
                    #print(coordR, coordC);
                    currentElement = mapToScore[coordR][coordC][1];
                    if (currentElement != '-'):
                        #print("Symbol: " + currentElement + " is in range at Coords: " + str(coordR) + ", " + str(coordC) + ".");
                        elementsFound.append(currentElement);

    #print(elementsFound);
    return elementsFound;


# noinspection PyRedundantParentheses
def getMapScore(map):
    mapToScore = map.map
    print("Scoring the following map:");
    mapToScore[0][3][1] = 'R';
    mapToScore[2][1][1] = 'I';
    mapToScore[2][2][1] = 'C';
    UPParser.printMapNicely(map);

    #Using X, S, I, C, R as markers for the map-overlay to represent building types
    # Rules for Scoring
    # 0..9: Building anything on any tile with value X = -X
    # X: I within 2 tiles = -10, C within 2 tiles = -20, R within 2 tiles = -20
    # S: R within 2 tiles = +10, can be built upon, but loses bonus
    # I: I within 2 tiles = + 3
    # C: R within 3 tiles = + 5, C within 2 tiles = - 5
    # R: I within 3 tiles = - 5, C within 3 tiles = + 5

    #initialize the score at 0
    currentScore = 0;

    #go through the overlay of the map, ignoring black spaces
    for row in range(len(mapToScore)):
        for col in range(len(mapToScore[0])):
            mapElement = mapToScore[row][col][1];
            # noinspection PyRedundantParentheses
            if(mapElement != '-'):
                #print("\nFound Symbol: "+mapElement+" at Coords: "+str(row)+", "+str(col)+".");
                #handle Toxic Waste Zone (X)
                # X: I within 2 tiles = -10, C within 2 tiles = -20, R within 2 tiles = -20
                if (mapElement == 'X'):
                    #check for all elements within 2 manhatten distance of [row][col][1]
                    elementsNearbyX = getElementsInMDist(mapToScore, row, col, 2);
                    for i in range(len(elementsNearbyX)):
                        if elementsNearbyX[i] == 'I':
                            currentScore -= 10;
                        if elementsNearbyX[i] == 'C' or elementsNearbyX[i] == 'R':
                            currentScore -= 20;
                #handle Scenic Views (S)
                # S: R within 2 tiles = +10, can be built upon, but loses bonus
                if (mapElement == 'S'):
                    elementsNearbyS = getElementsInMDist(mapToScore, row, col, 2);
                    for i in range(len(elementsNearbyS)):
                        if elementsNearbyS[i] == 'R':
                            currentScore += 10;
                #handle Industrial Zone
                # I: I within 2 tiles = + 3
                if (mapElement == 'I'):
                    if mapToScore[row][col][0] != 'S':
                        currentScore -= int(mapToScore[row][col][0]);
                    elementsNearbyI = getElementsInMDist(mapToScore, row, col, 2);
                    for i in range(len(elementsNearbyI)):
                        if elementsNearbyI[i] == 'I':
                            currentScore += 3;
                #handle Commercial Zone
                # C: R within 3 tiles = + 5, C within 2 tiles = - 5
                if (mapElement == 'C'):
                    if mapToScore[row][col][0] != 'S':
                        currentScore -= int(mapToScore[row][col][0]);
                    elementsNearbyC3 = getElementsInMDist(mapToScore, row, col, 3);
                    for i in range(len(elementsNearbyC3)):
                        if elementsNearbyC3[i] == 'R':
                            currentScore += 5;
                    elementsNearbyC2 = getElementsInMDist(mapToScore, row, col, 2);
                    for i in range(len(elementsNearbyC2)):
                        if elementsNearbyC2[i] == 'C':
                            currentScore -= 5;
                #handle Residential Zone
                # R: I within 3 tiles = - 5, C within 3 tiles = + 5
                if (mapElement == 'R'):
                    if mapToScore[row][col][0] != 'S':
                        currentScore -= int(mapToScore[row][col][0]);
                    elementsNearbyR = getElementsInMDist(mapToScore, row, col, 3);
                    for i in range(len(elementsNearbyR)):
                        if elementsNearbyR[i] == 'I':
                            currentScore -= 5;
                        if elementsNearbyR[i] == 'C':
                            currentScore += 5;
    #print("\nThe Score is: " + str(currentScore));
    return currentScore







if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("must provide a file name")
        sys.exit(1)
    getMapScore(UPParser.parseUrbanMap((sys.argv[1])))
