def metrics(dictfile):
    # reading from a file
    dic = open(dictfile, 'r') 
    
    longest_word = ''
    shortest_word = 'abcdefghijklmnopqrstuvwxyz'
    
    currword = dic.readline()          # read a line
    while currword != '':               # while not the end, do
        if(len(currword) < len(shortest_word)):
            shortest_word = currword    # found a shortest word
        if(len(currword) > len(longest_word)):
            longest_word = currword     # found a longest word
        currword = dic.readline()      # read the next line

    dic.close()

    # writing to a file
    output = open("output.txt", "w")
    output.write("# longest word: "+longest_word)
    output.write("# shortest word: "+shortest_word)
    output.close()

# suppose dictionary.txt contains the following lines
# CS1010X
# BEST
# MODULE
# WORLD

metrics("dictionary.txt")
# produces the output.txt file with the following lines
# longest word: # CS1010X
# shortest word: # BEST
