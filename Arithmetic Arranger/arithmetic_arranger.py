#import packages
import numpy as np
import itertools
import operator

# define the arithmetic_arranger function, that take a list of strings that are arithmetic problems as the first argument, and an optinal second argument that mention if the answers will be displayed
def arithmetic_arranger(problems, status=False):

  print(problems, '\n')
  # define only the operators that will be used
  allowed_operators={
    "+": operator.add,
    "-": operator.sub}

  # define empty lists that will contain the different lines of the conversion, if the problems are properly formed
  prob_first_line, prob_second_line, prob_result, prob_daschs, final_solution = [], [], [], [], []

  # raise error message if more then five problems supplied to the function
  if len(problems) > 5 :
    return print("Error: Too many problems.")
    
  # continue if less then five problems supplied  
  else:

    # each problem is arranged horizentally
    for problem in problems:

      # split each problem to first operand (number) "list_problems[0]", operator "list_problems[1]" and second operand "list_problems[2]"
      list_problems = problem.split()
      
      # raise an error message if the operator passed on the problem is not addition or subtraction
      if list_problems[1] not in ['-', '+'] :
        return print("Error: Operator must be '+' or '-'")

      # raise an error message if the operands contain other then digits
      elif not (list_problems[0].isdigit() and list_problems[2].isdigit()):
        return print("Error: Numbers must only contain digits.")

      # raise an error message if at least one of the operands contain more then four digits
      elif (len(list_problems[0])>4 or len(list_problems[2])>4):
        return print("Error: Numbers cannot be more than four digits.")

      # continue to arrange the problem verticaly because  it was supplied on the right format
      else: 

        # calculate the entire length of the problem to get the position of each character (digit, operator, signal, dashe) 
        position_operand = np.max([len(list_problems[0]), len(list_problems[2])])

        # define the empty first and second row (first and second operand) of the vertical arithmetic problem
        first_line, second_line = [], []
        
        # numbers should be right-aligned
        first_line.append(list_problems[0].rjust(position_operand))
        second_line.append(list_problems[2].rjust(position_operand))
        # adding four spaces (4*' ') between eauch problem
        # each problem should have dashes at the bottom that have the same length as the problem
        prob_daschs.append('-'*(position_operand + 2) + 4*' ')

        # append the digits of the first operand to the end of the first row of the vertival arrangment
        prob_first_line.append('  '+ "".join(first_line) + 4*' ')

        # append the digits of the second operand to the end of the second row of the vertival arrangment
        # a single space between the operator and the longest of the two operands, the operator on the same line as the second operand
        prob_second_line.append(list_problems[1] + ' '+ "".join(second_line) + 4*' ')

        # if the second optionaly argument is set to "true", the function will return the answers of every problem
        if status == True:
          result = str(allowed_operators[list_problems[1]](int(list_problems[0]),int(list_problems[2])))

          # if the answer of the problem is negative, the first character of the solution will be a minus "-" and not a digit
          if not result[0].isdigit():
            result = result[0] + ' ' + result[1:]

          else: 
            result = ' ' * ((position_operand+2)-len(result)) + result
           
          prob_result.append(result+ 4*' ')
          
    # add the problem vertically arranged, to the list of correctly supplied problems, as a string   
    final_solution.append("".join(prob_first_line)+"\n"+"".join(prob_second_line)+"\n"+"".join(prob_daschs)+"\n"+"".join(prob_result))

    # return the entire list of arithmetic problems, arranged vertically and sidi-by-side
    return final_solution[0]  

        
  
  




