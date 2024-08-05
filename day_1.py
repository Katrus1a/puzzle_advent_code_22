info=[]
sum=0
print("Введіть калорії")

while True:
    line=input()

    if line=="":
        if sum>0:
            info.append(sum)
            sum=0

        if len(info)>0:
            next_line=input()
            if next_line=="":
                break
            else:
                sum+=int(next_line)
    else:
        try:
            sum+=int(line)
        except ValueError:
            print("Error")

max_sum=max(info)
print(f"\n{max_sum} ")
