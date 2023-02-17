import sys
import timeit

if len(sys.argv) < 2:
    print("please imput in form (each newline is a arg):\ndicParser.py \nfile to read from \n1 :if no repeat letters wanted, 0 or anything else otherwise\nletters not in word\nletters in word\nletter position\n\nexmaple:\ndicParser.py wordleWords.txt 1 abc d p____") 
    sys.exit()

start = timeit.default_timer()

totalWords = 0
letters = {}

noRepeat = len(sys.argv) >= 3 and sys.argv[2] == '1'
letters_out = len(sys.argv) >= 4 and sys.argv[3].isalpha()
letters_in = len(sys.argv) >= 5 and sys.argv[4].isalpha()
letter_position = len(sys.argv) >= 6

print('num args:', len(sys.argv))
print(str(sys.argv))

noRepeat and print('noRepeat:'.rjust(20), sys.argv[2]) #short circuit method
letters_out and print('letters_out:'.rjust(20), sys.argv[3])
letters_in and print('letters_in:'.rjust(20), sys.argv[4])
letter_position and print('letter_position:'.rjust(20), sys.argv[5])

file = open(sys.argv[1], "r")

for line in file:
    word = (line.strip()).lower()
    if len(word) == 5:
        valid = True
        for i in range(0, 5): #test last char becasue it makes everything easier, prvieously went to 4
            if not word[i].isalpha(): #checks if letter is a alphabetic letter
                valid = False
                break
            if noRepeat: #contents of this if check if word has repeat letters
                for j in range(i+1, 5): #excludes testint itself
                    #print(word[i], "==", word[j], " ? ", i, "==", j)
                    if word[i] == word[j]: #checking if word has no letters that repeat
                        valid = False
                        break
            if letters_out:
                for j in range(0, len(sys.argv[3])): #not in word
                    if word[i] == sys.argv[3][j]: #
                        valid = False
                        break
            if letter_position:
                if sys.argv[5][i].isalpha() and sys.argv[5][i] != word[i]:
                    valid = False
                    break
                    
        if letters_in and valid: # checks that these letters are in the word, ooof, def figure this out, not clean
            for i in range(0, len(sys.argv[4])):
                valid = False # sets valid as false so that the sys arg element must be in the word for it to reset as true
                for j in range(0, 5):
                    if word[j] == sys.argv[4][i]:
                        valid = True
                        break
                if not valid:
                    break
               
        if valid: #if makes it past all other vars end up here
            totalWords += 1
            for char in word:
                if not char in letters: # done so that it can add dictionary key
                    letters[char] = 0
                letters[char] += 1
            if letters_out or letters_in: #only print out if there is some sort of constraint
                print(word, "", len(word))
            
file.close()
print(totalWords)
#print(letters)
for key in dict(sorted(letters.items(), key=lambda item: item[1], reverse=True)):
    print(key, ":", round((letters[key]/totalWords), 5))

stop = timeit.default_timer()
execution_time = stop - start

print("Program Executed in "+str(execution_time)) # It returns time in seconds