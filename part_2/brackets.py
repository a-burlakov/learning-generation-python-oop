def brackets():

    brackets = input()
    brackets_count = {"(": 1, ")": -1}
    count = 0

    for bracket in brackets:
        count += brackets_count[bracket]
        if count < 0:
            print("False")
            return

    if count != 0:
        print("False")
        return

    print("True")


brackets()
