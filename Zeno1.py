

if __name__ == "__main__":
    # f1 = open("test.txt", 'r')
    f1 = open("trace_201708/batch_instance.csv", 'r')
    f2 = open("trace_201708/prep1.csv", 'w')

    loop = 0
    dic1 = {}
    while True:
        loop +=1
        if loop % 100000 == 0:  #대략 1600만 줄
            print(loop)

        line = f1.readline()
        if not line: break
        comp = line.split(",")
        if comp[0] == '0' or comp[1] == '0' or comp[2] == "" or comp[3] == "" or comp[9] == "" or comp[11] == "\n":
            continue

        newline = comp[0] + "," + comp[1] + "," + comp[2] + "," + comp[3] + "," + comp[4] + "," + comp[9] + "," + comp[11]
        f2.write(newline)

    f1.close()
    f2.close()
