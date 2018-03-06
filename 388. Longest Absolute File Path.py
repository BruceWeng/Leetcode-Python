"""
Suppose we abstract our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory
subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains
a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains
a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a
file within our file system. For example, in the second example above, the longest
absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not
including the double quotes).

Given a string representing the file system in the above format, return the length
of the longest absolute path to file in the abstracted file system. If there is no
file in the system, return 0.

Note:
The name of a file contains at least a . and an extension.
The name of a directory or sub-directory will not contain a ..
Time complexity required: O(n) where n is the size of the input string.

Notice that a/aa/aaa/file1.txt is not the longest file path, if there is another
path aaaaaaaaaaaaaaaaaaaaa/sth.png.
"""
"""
Algorithm: Stack
1. Let a stack stores the accumulated path length in the current level(not necessary be max)
2. Split input into list by '\n'
3. Let level = last index of '\t' + 1
4. Pop stack until stack size == level + 1, find parent (while level + 1 < len(stack))
5. Let length = stack[-1] + len(s) - level + 1 (remove '\t' add '/'')
6. Once we find the file(if '.' in name), update result = max(result, length - 1) <- not include '/'
7. return result

"""
"""
@param {string} input
@return {int}
"""
def lengthLongestPath(input):
    if len(input) == 0 or input == None:
        return 0

    result = 0
    stack = [0]
    for name in input.split('\n'):
        level = name.rfind('\t') + 1 # lastIndexOf('\t'), return -1 if not found

        while level + 1 < len(stack):
            stack.pop()

        length = stack[-1] + len(name) - level + 1 # remove '\t' add '/'
        stack.append(length)
        if '.' in name:
            result = max(result, length - 1) # find file, no '/' following

    return result


if __name__=="__main__":
    path = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    print(lengthLongestPath(path)) # 32
