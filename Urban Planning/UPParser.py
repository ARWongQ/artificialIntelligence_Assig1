def parseUrbanMap(textfile):
    # This function reads in a textfile and parses the content into
    # 3 integers and a 3D array

    # Read in the file, pull apart the lines
    f = open(textfile, 'r');
    industrialCount = f.readline();
    commercialCount = f.readline();
    residentialCount = f.readline();
    urbanMap = f.readlines();
    f.close();

    #print(industrialCount);
    #print(commercialCount);
    #print(residentialCount);
    #print(urbanMap);

    #This subfunction splits the urbanMap into an array
    # First, create the empty 3D array...
    #   Get the X-size from urbanMap[0]

    mapLengthString = urbanMap[0];
    # split the string
    mapLengthArray = mapLengthString.split(',');
    #we now have the dimensions required to make the array

    urbanMapArray = [[["-" for dep in range(2)] for col in range(len(mapLengthArray))] for row in range(len(urbanMap))];
    #now we have an empty array with dimensions CxRx2
    print(urbanMapArray);

    #Now we move data from the urbanMap array of strings into the 3darray
    for row in range(len(urbanMap)):
        #pull the data from urbanMap like we did above
        mapString = urbanMap[row];
        mapArray = mapString.split(",");
        #print(mapArray);
        #move data from this array into the columns in the row
        for col in range(len(mapArray)):
            print(row, col, 0);
            currentElement = mapArray[col].rstrip();
            print(currentElement);
            urbanMapArray[row][col][0] = currentElement;
    #Assuming this works, we now can print this

    print(urbanMapArray);






if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("must provide a file name")
        sys.exit(1)
    parseUrbanMap(sys.argv[1])