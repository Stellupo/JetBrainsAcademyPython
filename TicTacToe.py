while True:
    answer = input('Enter cells: ')
    possibility = {"0","X","_"}
    set_answer = set(answer)
    if set_answer == possibility:
        if (len(answer)) == 9:
            continue
        else:
            print("---------")
            print("| "+answer[0]+" "+answer[1]+" "+answer[2]+" |")
            print("| "+answer[3]+" "+answer[4]+" "+answer[5]+" |")
            print("| "+answer[6]+" "+answer[7]+" "+answer[8]+" |")
            print("---------")
    else:
        continue