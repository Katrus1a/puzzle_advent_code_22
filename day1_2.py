info=[]
current_sum=0
print("Введіть калорії")

while True:
    line=input()

    if line=="":
        if current_sum>0:
            info.append(current_sum)
            current_sum=0

        if len(info)>0:
            next_line=input()
            if next_line=="":
                break
            else:
                current_sum+=int(next_line)
    else:
        try:
            current_sum+=int(line)
        except ValueError:
            print("Error")

if not info:
    print("No")
else:
    top_three_calories=sorted(info, reverse=True)[:3]
    three_sum=sum(top_three_calories)
    print(f"\nСума: {three_sum}")
