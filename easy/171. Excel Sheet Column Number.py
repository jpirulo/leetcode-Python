def convertToTitle(columnTitle):
    columnNumber = 0
    for i in range(len(columnTitle)):
        columnNumber = columnNumber * 26 + ord(columnTitle[i]) - ord('A') + 1
    return columnNumber
if __name__ =="__main__":
    print(convertToTitle('ZZ'))