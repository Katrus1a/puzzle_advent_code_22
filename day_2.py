result=0
print("Введіть")

while True:
    round_input=input()
    if round_input=="":
        break

    u_step, my_step=round_input.split()
    if u_step=="A":
        u_step="Rock"
    elif u_step=="B":
        u_step="Paper"
    elif u_step=="C":
        u_step="Scissors"

    if my_step=="X":
        my_step="Rock"
    elif my_step=="Y":
        my_step="Paper"
    elif my_step=="Z":
        my_step="Scissors"

    if my_step=="Rock":
        result+=1
    elif my_step=="Paper":
        result+=2
    elif my_step=="Scissors":
        result+=3

    if (my_step=="Rock" and u_step=="Scissors") or \
       (my_step=="Scissors" and u_step=="Paper") or \
       (my_step=="Paper" and u_step=="Rock"):
        result+=6 
    elif my_step==u_step:
        result+=3 
    else:
        result+=0  

print("Загальний рахунок:", result)
