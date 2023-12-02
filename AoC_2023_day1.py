import sys

def firstnum (mystring, patterns):
    wordIndex = 0
    lowIndex = len(mystring)+1
    firstWordnr = len(patterns.split('|'))+1
    words = patterns.split('|')
    for word in words:
        thisIndex = mystring.find (word)
        if thisIndex >= 0 and thisIndex < lowIndex:
            lowIndex = thisIndex
            firstWordnr = wordIndex
        wordIndex += 1
    w = words[0]
    if w == '1':
        return firstWordnr % 10 + 1
    else:
        return (len(words) - firstWordnr) % 10

if __name__ == "__main__":
    
    nroflines = 7
    infile = "day1_input.txt"
    myinstring = ""
    if len (sys.argv) == 2:
        infile = sys.argv[1]
    if len (sys.argv) == 3:
        infile = sys.argv[1]
        nroflines = int(sys.argv[2])
    
    
    allpatterns = "1|2|3|4|5|6|7|8|9|jonaswidell|one|two|three|four|five|six|seven|eight|nine"
    total_a = 0
    total_b = 0
    lines = 0
    for line in open (infile):
        if lines < nroflines:
            firstFirst = firstnum (line, allpatterns[:9*2-1:])
            firstSecond = firstnum (line[::-1], allpatterns[9*2-2::-1])
            linevalue_a = (firstFirst *10 + firstSecond)
            total_a += linevalue_a
            aFirst = firstnum (line, allpatterns)
            aSecond = firstnum (line[::-1], allpatterns[::-1])
            linevalue_b = aFirst*10 + aSecond
            total_b += linevalue_b
        lines += 1
    print ("Part 1 = " + str(total_a) + " and Part 2 = " + str(total_b))
