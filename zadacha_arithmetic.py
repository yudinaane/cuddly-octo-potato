def arithmetic(x,y,operator:str):
    if operator=='+':
        s=x+y
    elif operator=='-':
        s=x-y
    elif operator=='*':
        s=x*y
    elif operator=='/':
        s=x/y
    else: print('неизвестная операция')    
    return s
s=arithmetic(5,1,'+')
print(s)

p=arithmetic(10,0,'/')
print(p)

   