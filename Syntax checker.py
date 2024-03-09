import language_tool_python

# creating the tool
my_tool = language_tool_python.LanguageTool('en-US')


# given text
# my_text = 'A quick broun fox jumpps over a a little lazy dog.'

# correction
# correct_text = my_tool.correct(my_text)

# printing some texts
# print("Original Text:", my_text)
# print("Text after correction:", correct_text)


def checkSentence(string):
    length = len(string)
    if string[0] < 'A' or string[0] > 'Z':
        return False
    if string[length - 1] != '.':
        return False
    prev_state = 0
    curr_state = 0
    index = 1
    while (string[index]):
        if string[index] >= 'A' and string[index] <= 'Z':
            curr_state = 0
        elif string[index] == ' ':
            curr_state = 1
        elif string[index] >= 'a' and string[index] <= 'z':
            curr_state = 2
        elif string[index] == '.':
            curr_state = 3
        if prev_state == curr_state and curr_state != 2:
            return False
        if prev_state == 2 and curr_state == 0:
            return False
        if curr_state == 3 and prev_state != 1:
            return True
        index += 1
        prev_state = curr_state
    return False


while 1:
    string = input("Enter a sentence: ")
    corrected_text = my_tool.correct(string)
    print("Original string: " + string)
    print("Checking syntax :")
    if checkSentence(string):
        print("\"" + string + "\" syntax is CORRECT")
    else:
        print("\"" + string + "\" syntax is INCORRECT")
    print("\nCorrected string with spelling and grammar mistake: " + corrected_text)

