def convertToTitle(columnNumber):
    columnTitle = ""
    while columnNumber > 0:
          columnNumber -= 1
          print(f"1. {columnNumber}")
          print(f"2. {columnTitle}")
          print(f"3. {columnNumber % 26}")
          columnNumber -= 1
          print(f"4. {columnNumber}")
          print(f"5  {chr(columnNumber % 26)}")
          print(f"6 {ord('A')}")
          print(f"7 {columnTitle}")

          columnTitle = chr((columnNumber % 26) + ord('A')) + columnTitle
          print(f"8 {columnTitle}")
          columnNumber //= 26
          print(f"9 {columnNumber}")
    return columnTitle

if __name__ =="__main__":
    print(convertToTitle(408))