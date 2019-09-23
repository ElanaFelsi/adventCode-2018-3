def parameters(line):
    param = line.split()
    left, top = param[2].split(',')
    top = top.replace(':', "")
    wide, tall = param[3].split('x')
    left, top, wide, tall = int(left), int(top), int(wide), int(tall)
    id = param[0]
    return left, top, wide, tall, id


def overlapped(_path):
    d = {}
    with open(_path, 'r') as f:
        for line in f:
            left, top, wide, tall, id = parameters(line)
            for x in range(wide):
                for y in range(tall):
                    if (left + x, top + y) in d.keys():
                        d[(left + x, top + y)] += 1
                    else:
                        d[(left + x, top + y)] = 1

    count = 0
    for val in d.values():
        if val >= 2:
            count += 1
    print(count)

    with open(_path, 'r') as f:
        for line in f:
            left, top, wide, tall, id = parameters(line)
            flag = True
            for x in range(wide):
                for y in range(tall):
                    if d[(left + x, top + y)] > 1:
                        flag = False
            if flag:
                print(id)