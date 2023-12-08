import re

def java_vs_c(input: str):
    output = ''
    #check cpp
    cpp = re.search("_", input)
    jav = re.search("[A-Z]", input)

    if(cpp and jav):
        output = 'Error!'
    elif(cpp):
        words = re.split("_", input)
        for x in words:
            x.capitalize()
        output = output.join(words)            
    elif(jav):
        words = re.split("[A-Z]", input)
        for x in words:
            x.lower()
        output = "_".join(words)
    else:
        output = input
    return output

def main():
    
    while(True):
        try:
            print(java_vs_c(input()))
        except EOFError:
            break

if __name__ == "__main__":
    main()        