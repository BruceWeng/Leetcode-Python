# Solution 1:
def generateNextNumber(startNumber):
    current = {"number": startNumber}
    def tempFunction():
        current["number"] += 1
        return current["number"]
    return tempFunction

getNextNumber = generateNextNumber(10)
for i in range(10):
    print (getNextNumber())

# Solution 2:
def generateNextNumber(startNumber):
    current = startNumber
    def tempFunction():
        nonlocal current
        current += 1
        return current
    return tempFunction

getNextNumber = generateNextNumber(10)
for i in range(10):
    print (getNextNumber())

 # JavaScript Version
# function generateNextNumber(startNumber) {
#     let current = startNumber
#     function tempFunction() {
#         current += 1
#         return current
#     }
#     return tempFunction
# }
#
# getNextNumber = generateNextNumber(10)
# for (let i = 0; i < 10; i++) {
#     console.log(getNextNumber())
# }
