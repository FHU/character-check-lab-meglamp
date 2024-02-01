#Remove pass and complete the code
def check_character(word, index):
    thing = word[index]
    if thing.isalpha():
        return("letter")
    elif thing.isdigit():
        return("digit")
    elif thing.isspace():
        return("white space")
    else:
        return("unknown")
      

in1 = input()
in2 = int(input())
print(check_character(in1,in2))