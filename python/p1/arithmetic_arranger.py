def arithmetic_arranger(data_list, *solutions):
    
    operator = []                                                                       
    longest = []                                           #len of the longest number from operation
    left_digits = []
    right_digits = []
    results = []  
    #the lenght condition
    if len(data_list) > 5:
        return "Error: Too many problems."

    #the operators condition
    for operation in data_list:
        if "+" in operation:
            operator.append("+")
        elif "-" in operation:
            operator.append("-")
        else:
            return "Error: Operator must be '+' or '-'."
        
        #max of four digits in width condintion
        first_number = operation.find(' ') - 1
        left_number = operation[:first_number + 1]
        right_number = operation[first_number + 4:]
        if len(left_number) > 4 or len(right_number) > 4:
            return "Error: Numbers cannot be more than four digits."
        left_digits.append(left_number)
        right_digits.append(right_number)

        #the only digits condition
        for char in operation:
            dig_op = "1234567890-+ "
            if char not in dig_op:
                return "Error: Numbers must only contain digits."

        if len(left_number) > len(right_number):                     #used during printing the output
            longest.append(len(left_number))
        else:
            longest.append(len(right_number))


        if operator[-1] == "+":                                      #used during printing the output              
            results.append(str(int(left_number) + int(right_number)))
        else:
            results.append(str(int(left_number) - int(right_number)))


    #printing the output
    first_line = ''
    second_line = ''
    third_line = ''
    fourth_line = ''
    for numb in range(len(data_list)):
        first_line += '  ' + (longest[numb] - len(left_digits[numb])) * ' ' +  left_digits[numb] + '    '
        second_line += operator[numb] + ' ' + (longest[numb] - len(right_digits[numb])) * ' ' + right_digits[numb] + '    '
        third_line += '--' + '-' * longest[numb] + '    '
        if '+' == operator[numb]:
            fourth_line += ((longest[numb] + 2) - len(results[numb])) * ' ' + str(results[numb]) + '    '
        else:
            if int(results[numb]) > 0:
                fourth_line += '  '  + ((longest[numb] - len(results[numb])))* ' ' + str(results[numb]) + '    '
            else:
                fourth_line += ' '  + ((longest[numb] - len(results[numb])))* ' ' + str(results[numb]) + '    '

    if True in solutions:
        return first_line + '\n' + second_line + '\n' + third_line + '\n' + fourth_line
    else:
        return first_line + '\n' + second_line + '\n' + third_line





