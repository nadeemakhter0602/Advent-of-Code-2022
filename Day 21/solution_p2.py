import time


def parse(line):
    line = line.split(': ')
    monkey = line[0]
    if str.isnumeric(line[1]):
        return monkey, int(line[1])
    else:
        return monkey, line[1].split(' ')


def form_equation(monkey, graph, equation):
    curr = graph[monkey]
    if monkey == 'humn':
        return 'x'
    elif isinstance(curr, (int, float)):
        return graph[monkey]
    return '(' + str(form_equation(curr[0], graph, equation)) + curr[1] + str(form_equation(curr[2], graph, equation)) + ')'


with open('input.txt') as f:
    start = time.time()
    graph = dict()
    lines = f.read().split('\n')
    graph = dict()
    for line in lines:
        monkey, job = parse(line)
        graph[monkey] = job
    graph['root'] = [graph['root'][0], '-', graph['root'][2]]
    equation = form_equation('root', graph, str())
    complex_num = eval(equation.replace('x', '1j'))
    print('The number you yell is :', int(-complex_num.real / complex_num.imag))
    print('Time taken :', time.time() - start)
