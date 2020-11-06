# This code is written in Python version 3.8.5 with GCC version 9.3.0 on Ubuntu 20.04.1 LTS.
# Additionally, the environment was set up using Pip 20.2.4 with virtual environment version 20.0.35

# The assumption here is that the lower case names are the same as upper case names.
# For example, 'Peter' and 'peter' and 'peTer' are treated same. The ones that comes before are favoured.
# (For example, given the lists--['Peter', 'peter'] and ['peTer']--'Peter' is favoured since it is in the first list and
# is before 'peter'.)

class Solution:
    def mergeList(studentListA: [str], studentListB: [str]) -> [str]:
        mergedList = []
        namesChecked = set()
        for name in (studentListA+studentListB):
            if not name.lower() in namesChecked:
                mergedList.append(name)
                namesChecked.add(name.lower())
        return list(mergedList)

class HelperFunctions:
    def areListsSame(answer: [str], correctAnswer: [str]) -> bool:
        return sorted(answer) == sorted(correctAnswer)

if __name__ == "__main__":
    testAndAnswers = []

    testAndAnswers.append([[['Allison', 'Brian', 'Peter'], ['Jason', 'Peter', 'Sara']], ['Allison', 'Brian', 'Peter', 'Jason', 'Sara']])
    testAndAnswers.append([[['Allison', 'brian', 'peTer'], ['jason', 'Peter', 'sara']], ['Allison', 'brian', 'peTer', 'jason', 'sara']])
    testAndAnswers.append([[['Allison', 'allison', 'Allison'], []], ['Allison']])
    testAndAnswers.append([[[], ['peter', 'Peter', 'Jason']], ['peter', 'Jason']])
    testAndAnswers.append([[['a Park'], ['b Park']], ['a Park', 'b Park']])

    for testAndAnswer in testAndAnswers:
        try:
            assert(HelperFunctions.areListsSame(Solution.mergeList(testAndAnswer[0][0], testAndAnswer[0][1]), testAndAnswer[1]))
        except AssertionError:
            print('Failed the test case. The answer should be\n')
            print(testAndAnswer[1])
            print()
            print('But was \n')
            print(Solution.mergeList(testAndAnswer[0][0], testAndAnswer[0][1]))
            exit()
    
    print('All Done without Errors')
    