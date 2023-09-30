word = input()

letters=""
num=""
t_l = ""
for i in range(len(word)):
    if word[i].isalpha():
        letters+=word[i]
    elif word[i].isdigit():
        num+=word[i]
    elif word[i]=='-':
        t_l = "loosen"
    else:
        t_l = "tighten"
    
    if i<len(word)-1:
        if not(num=="") and not(t_l=="") and word[i].isdigit() and word[i+1].isalpha():
            print(letters, t_l, num)
            letters = ""
            num = ""
            t_l = ""
print(letters, t_l, num)