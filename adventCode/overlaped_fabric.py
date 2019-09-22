def open_file(_path):
    dict = {}
    dict = dict.fromkeys(dict, 0)
    with open(_path, 'r') as f:
        for line in f:
            param = line.split()
            left, top = param[2].split(',')
            top = top.replace(':', "")
            wide, tall = param[3].split('x')
            left, top, wide, tall = int(left), int(top), int(wide), int(tall)
            for x in range(wide):
                for y in range(tall):
                    dict[(left+x, top+y)] += 1

print(dict)






