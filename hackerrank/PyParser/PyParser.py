'''
We have defined our own markup language, HRML. In HRML, each element consists of a starting and ending tag, and there are attibutes associated with each tag. Only starting tags van have attributes. We can call an attribute by referencing the tag, followed by the '~' symbol and the name of the attribute. The tags may also be nested.

The opening tags follow the format:
<tag-name attribute1-name = "value1" attibute2-name = 'value2' ...>
The closing tags follow the format:
< /tag-name >

For example:
<tag1 value = "HelloWorld">
<tag2 name = "Name1">
</tag2>
</tag1>

The attibutes are referenced as:
tag1~value
tag1.tag2~name
You are given the source code in HRML format consisting of N lines. You have to answer Q queries. Each query askes you to print the value of the attribute specified. Print "Not Found!" if there isn't any such attibute.

Input Format
The first line consists of two space separated integers, N and Q. The next N lines of the HML source code and each line consists of either an opening tag with zero or more attibutes or a closing tag. Then the next Q lines contains the queriies. Each query consists of string that references an attribute in the HRML source code.

Sample Input:
4 3
<tag1 value = "HelloWord" time = "0800">
<tag2 name = "Name1">
</tag2>
<tag3 name = "Tom">
<tag4>
</tag4>
</tag3>
</tag1>
tag1.tag2~name
tag1~name
tag1~value

Sample Output:
Name1
Not Found!
HelloWorld

'''

class TagTree():
    def __init__(self, tagName):
        self.name = tagName
        self.attrs = {}
        self.children = []
        self.parent = None
        self.level = 0

def main():
    data = map(int, raw_input().split(' '))
    tagLines = data[0]
    actions = data[1]
    level = 0
    tags = []
    tag = Tag()
    curr = tag

    for i in range(tagLines):
        string = raw_input()
        if string[1] == '/':
            level -= 1
            curr = curr.parent
        else:
            level += 1
            tag = string[1:-1].split(' ')
            tag[3] = tag[3][1:-1]
            tags.append(tag)
            tag.append(level)

            for ele in tags:
                curr = Tag(ele[0])
                tag.children.append(curr)
                curr.attrs[ele[1]] = ele[3]
                curr.level = ele[4]

    print tags

if __name__ == '__main__':
    main()
