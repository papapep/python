def problem2_8(temp_list):
    max,min,acc=-1000,1000,0
    for temp in range(len(temp_list)):
        if float(temp_list[temp]) > max:
            max = float(temp_list[temp])
        if float(temp_list[temp]) < min:
            min = float(temp_list[temp])
        acc = acc + float(temp_list[temp])
    print("Average:",acc/len(temp_list))
    print("High:",max)
    print("Low:",min)