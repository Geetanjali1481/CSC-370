#!/usr/bin/env python
# coding: utf-8

# In[3]:


LETTER = 0
DIGIT = 1
UNKNOWN = 99
INT_LIT = 10
IDENT = 11
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
MULT_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26
EOF = -1
EOFCHR = ""


def main():
    global in_fp, cursor, nextToken
    file = open("Ex1.txt",'r')
    in_fp = file.read()
    cursor=-1
    getChar();
    nextToken="Not"
    while True:
        lex()
        if nextToken == EOF:
            break

def lookup(ch):
    global nextToken
    if ch == '(':
        addChar()
        nextToken = LEFT_PAREN
    elif ch == ')':
        addChar()
        nextToken = RIGHT_PAREN
    elif ch == '+':
        addChar()
        nextToken = ADD_OP
    elif ch == '-':
        addChar()
        nextToken = SUB_OP
    elif ch == '*':
        addChar()
        nextToken = MULT_OP
    elif ch == '/':
        addChar()
        nextToken = DIV_OP
    else:
        addChar()
        nextToken = EOF

    return nextToken

def addChar():
    global lexeme
    if len(lexeme) <= 98:
        lexeme += nextChar
    else:
        printf("Error - lexeme is too long \n")

def getChar():
    global nextChar, charClass
    nextChar = getc(in_fp)
    if nextChar != EOFCHR:
        if nextChar.isalpha():
            charClass = LETTER
        elif nextChar.isnumeric():
            charClass = DIGIT
        else:
            charClass = UNKNOWN
    else:
        charClass = EOF
    return nextChar

def getc(instring):
    global in_fp, cursor
    cursor +=1
    if cursor >= len(instring):
        return EOFCHR
    else:
        return instring[cursor]
    
def getNonBlank():
    while nextChar.isspace():
        getChar()

def lex():
    global lexeme, nextToken
    lexeme = ""
    getNonBlank()
    if charClass == LETTER:
        addChar()
        getChar()
        while charClass == LETTER or charClass == DIGIT:
            addChar()
            getChar()
        nextToken = IDENT
    elif charClass == DIGIT:
        addChar()
        getChar()
        while charClass == DIGIT:
            addChar()
            getChar()
        nextToken = INT_LIT
    elif charClass == UNKNOWN:
        lookup(nextChar)
        getChar()
    elif charClass == EOF:
        nextToken = EOF;
        lexeme = 'EOF'
    print("Next token is:",nextToken,", Next lexeme is", lexeme)
    return nextToken

if __name__ == '__main__':
    main()


# In[ ]:




