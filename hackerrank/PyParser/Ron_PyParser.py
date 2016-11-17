test = "8 3\n<tag1 value = 'HelloWord' time = '0800'>\n<tag2 name = 'Name1'>\n</tag2>\n<tag3 name = 'Tom'>\n<tag4>\n</tag4>\n</tag3>\n</tag1>\ntag1.tag2~name\ntag1~name\ntag1~value"

# Sample Output:
# Name1
# Not Found!
# HelloWorld


# print(test)


def is_close(input):
    return input[0:2] == '</'

# print(is_close("<tag1 value = 'HelloWord' time = '0800'>"))
# print(is_close("</tag4>"))

def break_up(input):
    work = input[1:len(input)-1]
    work = work.split(' ')

    result = {}
    result['tag_name'] = work[0]
    result['attr'] = {}

    i = 1

    while i < len(work):
        result['attr'][work[i]] = work[i + 2][1:len(work[i+2])-1]
        i += 3


    return result

# print(break_up("<tag1 value = 'HelloWord' time = '0800'>"))

def break_up_command(input):
    work = input.split('.')
    temp = work[-1].split('~')
    work.pop()
    work.append(temp[0])
    work.append(temp[1])
    result = {}
    result['tag_path'] = work[:-1]
    result['attr_query'] = work[-1]
    return result

# print(break_up_command('tagr.tag10.tag1.tag2~name'))



def parser(input):
    work = input.split('\n')
    first_line = work[0]
    first_line = first_line.split(' ')

    lines_of_hml = first_line[0]

    hml_code = work[1:int(lines_of_hml)]

    # print(hml_code)

    stack = []
    result = {}
    stack.append(result)

    for i in xrange(0, len(hml_code)):
        line = hml_code[i]
        # open case
        if is_close(line) == False:
            reference = stack[-1]
            broken_line = break_up(line)
            reference[broken_line['tag_name']] = {}
            reference[broken_line['tag_name']]['attr'] = broken_line['attr']
            reference[broken_line['tag_name']]['nested'] = {}
            stack.append(reference[broken_line['tag_name']]['nested'])

        # close case
        else:
            stack.pop()

    commands = work[1+int(lines_of_hml):]

    # print(commands)

    for i in xrange(0, len(commands)):
        command = commands[i]
        broken_command = break_up_command(command)
        curr = result
        for j in xrange(0, len(broken_command['tag_path'])):
            uni_tag = broken_command['tag_path'][j]
            curr = curr[uni_tag]
            if j < len(broken_command['tag_path']) - 1:
                curr = curr['nested']

        attr = broken_command['attr_query']

        if attr in curr['attr']:
            print(curr['attr'][attr])
        else:
            print('Not found!')



parser(test)
