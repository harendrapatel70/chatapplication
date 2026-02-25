# main/rules.py

C_RULES = {
    "what is c": "C is a procedural programming language developed by Dennis Ritchie.",
    "features of c": "C is fast, portable, and memory efficient.",
    "who invented c": "C was invented by Dennis Ritchie in 1972.",
    "what is pointer": "Pointer stores address of another variable.",
    "what is array": "Array stores multiple values of same data type.",
    "what is structure": "Structure groups different data types.",
    "what is union": "Union shares memory among different data types.",
    "what is malloc": "malloc allocates memory dynamically.",
    "what is free": "free deallocates memory.",
    "what is compiler": "Compiler converts code into machine language."
}

def chatbot_response(message):
    message = message.lower()
    for key in C_RULES:
        if message in key :
            return C_RULES[key]
    return "Sorry, I answer only basic C language questions."