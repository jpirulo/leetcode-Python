def convertToTitle(columnTitle):
    columnNumber = 0
    for i in range(len(columnTitle)):
        print('-----------------')
        print(i)
        print(f"1. {columnNumber}")
        print(f"2. {columnNumber}*26")
        print(f"3.{columnTitle[i]} ,ord= {ord(columnTitle[i])}")
        print(f"4. {ord('A')}")
        columnNumber = columnNumber * 26 + ord(columnTitle[i]) - ord('A') + 1
        print(f"5. {columnNumber}")

    return columnNumber
if __name__ =="__main__":
    print(convertToTitle('AAA'))