

if __name__ == "__main__":
    # f1 = open("test.txt", 'r')
    f1 = open("trace_201708/prep3.csv", 'r')
    f2 = open("trace_201708/prep4.csv", 'w')

    loop = 0
    cnt = 0
    while True:
        loop += 1
        if loop % 100000 == 0:  # 대략 113만 줄
            print(loop)

        line = f1.readline()
        if not line: break
        comp = line.split(",")
        if comp[0] == '3':
#print(line)
            cnt+=1
            newline = "1,"
        else:
            newline = "0,"
        newline += comp[4] + "," + comp[5]
        f2.write(newline)
    print(cnt)
    f1.close()
    f2.close()
'''
    avg_time = [0]*7
    tag_count = [0] * 7
    loop = 0
    dic1 = {}
    while True:
        loop +=1
        if loop % 100000 == 0:  #대략 113만 줄
            print(loop)

        line = f1.readline()
        if not line: break
        comp = line.split(",")
        tag = int(comp[0])
        time = int(comp[1])
        avg_time[tag] += time
        tag_count[tag] += 1
    for i in range(7):
        avg_time[i] = avg_time[i] / tag_count[i]

    print(avg_time)
    avg_time.sort()
    print(avg_time)

    f1.close()
'''
