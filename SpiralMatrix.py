def matrix_define(n, some_String):
    matrix=[]
    for i in range (n):
        matrix.append([0]*n)
    top_row = 0
    bot_row=n-1
    left_col = 0
    right_col=n-1
    
    counter = 0
    char_list = list(some_String)

    direction = 0

    while (top_row <= bot_row and left_col <= right_col):
        if direction == 0:
            for i in range (left_col, right_col+1):

                if counter == len(char_list):
                    counter=0
                    matrix[top_row][i] = char_list[counter]
                    counter += 1
                else:
                    matrix[top_row][i] = char_list[counter]
                    counter += 1

            top_row += 1
            direction = 1


        elif direction == 1:
            for i in range(top_row, bot_row+1):

                if counter == len(char_list):
                    counter=0
                    matrix[i][right_col] = char_list[counter]
                    counter += 1
                else:
                    matrix[i][right_col] = char_list[counter]
                    counter += 1

            right_col -= 1
            direction = 2


        elif direction == 2:
            for i in range (right_col, left_col-1, -1):

                    if counter == len(char_list):
                        counter = 0
                        matrix[bot_row][i] = char_list[counter]
                        counter += 1
                    else:
                        matrix[bot_row][i] = char_list[counter]
                        counter += 1

            bot_row -= 1
            direction = 3



        elif direction == 3:
            for i in range (bot_row, top_row-1, -1):

                    if counter == len(char_list):
                        counter = 0
                        matrix[i][left_col] = char_list[counter]
                        counter += 1
                    else:
                        matrix[i][left_col] = char_list[counter]
                        counter += 1
            left_col+=1
            direction = 0


    matrix_List=[]
    while len(matrix_List)<counter:
        for i in some_String:
            matrix_List.append(i)




    for i in range(n):
        print(matrix[i])





matrix_define(10, "SoftUni")