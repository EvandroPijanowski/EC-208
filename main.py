def convert(line):
    return int(line, 2)


def get_op(inst):
    return inst[:4], inst[4:8], inst[8:12], inst[12:]


def save(num, reg_3):
    aux = list(data)
    aux[convert(reg_3)] = str(num)
    dataFile.seek(0)
    dataFile.write(''.join(aux))


def add(num_1, num_2):
    return int(num_1) + int(num_2)


def sub(num_1, num_2):
    return int(num_1) - int(num_2)


def execute(op, num_1, num_2, reg_3):
    if op == '0000':
        save(add(num_1, num_2), reg_3)
    elif op == '0001':
        save(sub(num_1, num_2), reg_3)


def load(reg_1, reg_2):
    return data[reg_1], data[reg_2]


def get_inst(inst):
    op, reg_1, reg_2, reg_3 = get_op(inst)
    num_1, num_2 = load(convert(reg_1), convert(reg_2))
    execute(op, num_1, num_2, reg_3)


dataFile = open('data.txt', 'r+')
with open('instruction.txt') as instFile:
    for line in instFile.readlines():
        dataFile.seek(0)
        data = dataFile.readline()
        get_inst(line)
dataFile.close()
