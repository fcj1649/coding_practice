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
        for word in words:
            if(len(word) == 0):
                output = 'Error!'

        if(output == ''):        
            output = words[0]
            for i in range(1, len(words)):
                output = output + words[i].capitalize()            
    elif(jav):
        i = 0
        while(i < len(input)):
            if(input[i].isupper()):
                if( i == 0):
                    output = 'Error!'
                    break
                else:    
                    output = output + '_' + input[i].lower()
            else:
                output = output + input[i]
            i += 1
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