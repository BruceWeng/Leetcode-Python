# // function reverse(strs) {
# //   result = strs.split('').reverse().join('')
# //   return result
# // }
# //
# // var test1 = 'abcde'
# // console.log(reverse(test1))


def reverse(strs):
  return ''.join(list(strs)[4:0:-1])

print reverse('abcde')
