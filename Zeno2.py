if __name__ == "__main__":
    # f1 = open("test.txt", 'r')
    f1 = open("trace_201708/prep1.csv", 'r')

    loop = 0
    dic1 = {}
    while True:
        loop +=1
        if loop % 100000 == 0:  #대략 129만 줄
            print(loop)

        line = f1.readline()
        if not line: break
        comp = line.split(",")
        # timestamp1, timestamp2, job, task, machine, avgcpu, avgmem

        if comp[3] in dic1:
            dic1[comp[3]] += 1
        else:
            dic1[comp[3]] = 1
    f1.close()
    count = 0
    dic2 = {}
    for key, value in dic1.items():
        if value >= 50:
            dic2[key] = value
            count += 1
    print("initial count complete: " + str(count))

    f1 = open("trace_201708/prep1.csv", 'r')
    f2 = open("trace_201708/prep2.csv", 'w')
    loop = 0
    count = 0
    while True:
        loop += 1
        if loop % 100000 == 0:  # 대략 129만 줄
            print(loop)

        line = f1.readline()
        if not line: break
        comp = line.split(",")
        # timestamp1, timestamp2, job, task, machine, avgcpu, avgmem
        if comp[3] in dic2:
            time = int(comp[1]) - int(comp[0])
            newline = str(time) + ',' + comp[3] + ',' + comp[4] + ',' + comp[5] + ',' + comp[6]
            f2.write(newline)
            # time, task, machine, avgcpu, avgmem
        else:
            count += 1
    f1.close()
    f2.close()
    print("filtering complete, deleted lines: " + str(count))