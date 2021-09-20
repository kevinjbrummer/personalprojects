def arithmetic_arranger(problems, display=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    else:
        problem_list = []
        for i in range(len(problems)):
            check = check_error(problems[i])
            if check[0] == True:
                return check[1]
            else:
                problem_list.append(check[1])
        output = [[], [], []]
        for i in range(len(problem_list)):
            opr1 = problem_list[i][0]
            oprand = problem_list[i][1]
            opr2 = problem_list[i][2]
            output[1].append(oprand + " ")
            max_length = 0
            if len(opr1) == len(opr2):
                max_length = len(opr1) + 2
                output[0].append("  " + opr1)
                output[1].append(opr2)
                for j in range(len(opr1) + 2):
                    output[2].append("-")
            elif len(opr2) > len(opr1):
                max_length = len(opr2) + 2
                output[1].append(opr2)
                for j in range(len(opr2) + 2):
                    output[2].append("-")
                for j in range(len(opr2) - len(opr1) + 2):
                    output[0].append(" ")
                output[0].append(opr1)
            else:
                max_length = len(opr1) + 2
                output[0].append("  " + opr1)
                for j in range(len(opr1) + 2):
                    output[2].append("-")
                for j in range(len(opr1) - len(opr2)):
                    output[1].append(" ")
                output[1].append(opr2)

            if i != (len(problem_list) - 1):
                for j in range(3):
                    output[j].append("    ")
            if display == True:
                output.append([])
                solution = solve(problem_list[i])
                temp = ""
                for j in range(max_length - len(solution)):
                    temp = temp + " "
                output[3].append(temp + solution)
                if i != (len(problem_list) - 1):
                    output[3].append("    ")

        temp = ""
        for i in output[0]:
            temp = temp + i
        temp = temp + "\n"
        for i in output[1]:
            temp = temp + i
        temp = temp + "\n"
        for i in output[2]:
            temp = temp + i
        if display == True:
            temp = temp + "\n"
            for i in output[3]:
                temp = temp + i
        return temp


def check_error(problem):
    temp1 = ""
    temp2 = ""
    temp3 = ""
    space = 1
    counter = 1
    for i in problem:
        if i == " ":
            space = space + 1
            counter = 1
        else:
            if space == 1:
                if i not in "1234567890":
                    return [True, "Error: Numbers must only contain digits."]
                elif counter > 4:
                    return [
                        True, "Error: Numbers cannot be more than four digits."
                    ]
                else:
                    temp1 = temp1 + i
                    counter = counter + 1
            elif space == 2:
                if i not in "+-":
                    return [True, "Error: Operator must be '+' or '-'."]
                else:
                    temp2 = temp2 + i
            else:
                if i not in "1234567890":
                    return [True, "Error: Numbers must only contain digits."]
                elif counter > 4:
                    return [
                        True, "Error: Numbers cannot be more than four digits."
                    ]
                else:
                    temp3 = temp3 + i
                    counter = counter + 1
    return [False, [temp1, temp2, temp3]]


def solve(equation):
    opr1 = int(equation[0])
    opr2 = int(equation[2])
    oprand = equation[1]
    if oprand == "+":
        return str(opr1 + opr2)
    else:
        return str(opr1 - opr2)
