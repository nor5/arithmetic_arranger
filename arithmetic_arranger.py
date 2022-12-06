import re


def arithmetic_arranger(problems, calcul=False):
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    #Situations that will return an error

    if len(problems) <= 5:

        for pp in problems:
            p = ''.join(pp.split())
            ##    regexp = "([0-9]{1,4})([-\+])([0-9]{1,4}$)"
            regexp = "(\d{1,4})([-\+])(\d{1,4}$)"
            match = re.match(regexp, p)

            if match is None:
                
                falseOperation = "(\d{1,4})(.)(\d{1,4}$)"
                match1 = re.match(falseOperation, p)
                onlydigit = "(\w{1,4})(.)(\w{1,4}$)"
                match2 = re.match(onlydigit, p)
                maxdigit = "(\d+)([-\+])(\d+)"
                match3 = re.match(maxdigit, p)
                #2 appropriate operators
                if match1:
                    arranged_problems = "Error: Operator must be '+' or '-'."
                    return arranged_problems
                #3 only contain digits
                elif match2:
                    arranged_problems = "Error: Numbers must only contain digits."
                    return arranged_problems
                #4 max of four digits in width
                elif match3:
                    arranged_problems = "Error: Numbers cannot be more than four digits."
                    return arranged_problems
                
            else:

                if len(match[1]) <= len(match[3]):
                    space = (len(match[3]) - len(match[1]))
                    operand1 = 2 * " " + space * " " + match[1]
                    operand2 = match[3]
                    inderscor = (len(match[3]) + 2) * "-"
                else:
                    space = len(match[1]) - len(match[3])
                    inderscor = (len(match[1]) + 2) * "-"
                    operand1 = 2 * " " + match[1]
                    operand2 = space * " " + match[3]

                operator = match[2] + " "
                
                result = str(eval(match[1] + match[2] + match[3]))
                spaceResult = len(inderscor) - len(result)
               
                if problems.index(pp) == (len(problems)-1):
                  
                  line1 = line1 + operand1 
                  line2 = line2 + operator + operand2 
                  line3 = line3 + inderscor 
                  line4 = line4 + spaceResult*" "+ result 
                else:
                  
                  line1 = line1 + operand1 + 4 * " "
                  line2 = line2 + operator + operand2 + 4 * " "
                  line3 = line3 + inderscor + 4 * " "
                  line4 = line4 + spaceResult*" "+ result + 4 * " "
                
                

                  
                
              

        #return arranged_problems
        if calcul:

            arranged_problems = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
            return arranged_problems
        else:
            arranged_problems = line1 + "\n" + line2 + "\n" + line3
            return arranged_problems
        
    else:
        #1 too many problems
        arranged_problems = "Error: Too many problems."
        return arranged_problems
