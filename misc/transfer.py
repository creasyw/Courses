import re, sys
from subprocess import call


def main():
    if len(sys.argv)!=2:
        print "The command line should be \"transfer.py filename\""
        return
    filename = re.sub(".html", ".markdown",sys.argv[1])
    input = open(sys.argv[1], 'r')
    output = open(filename, 'w')
    for line in input:
        if line=="<div class='post'>\n": continue
        newline = re.sub("<br />", "\n", line)
        newline = re.sub("&nbsp;"," ", newline)
        newline = re.sub(r"_", r"\_", newline)
        output.write(newline)
    input.close()
    output.close()
    call(["rm", sys.argv[1]])

if __name__=="__main__":
    main()


