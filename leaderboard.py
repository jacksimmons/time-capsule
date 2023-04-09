lb_done = False
yourscore = 52
while lb_done == False:
    x = 1
    yourname = input("Winner: Please enter your 'victory' name! (Must be no longer than 10 characters)\n~ ")
    if len(yourname) <= 10:
        if len(yourname) < 10:
            while x < 10:
                x = len(yourname)
                yourname = yourname + ' '
        elif len(yourname) == 10:
            file = open('leaderboard.txt','r')
            lb_1 = [file.read(11),int(file.read(3))]
            lb_2 = [file.read(11),int(file.read(3))]
            lb_3 = [file.read(11),int(file.read(3))]
            lb_4 = [file.read(11),int(file.read(3))]
            lb_5 = [file.read(11),int(file.read(3))]
            file.close()
            if yourscore > lb_1[1]:
                if yourscore > lb_2[1]:
                    if yourscore > lb_3[1]:
                        if yourscore > lb_4[1]:
                            if yourscore > lb_5[1]:
                                yourplace = 1
                            else:
                                yourplace = 2
                        else:
                            yourplace = 3
                    else:
                        yourplace = 4
                else:
                    yourplace = 5
            else:
                yourplace = 6
            if yourplace < 6:
                file = open('leaderboard.txt','w')
                if yourplace == 5:
                    file.write(yourname + '\n' + str(yourscore) + '\n' + lb_2[0] + str(lb_2[1]) + '\n' + lb_3[0] + str(lb_3[1]) + '\n' + lb_4[0] + str(lb_4[1]) + '\n' + lb_5[0] + str(lb_5[1]))
                    print("Nice job! You are 5th on the leaderboard for winning scores.")
                elif yourplace == 4:
                    file.write(lb_1[0] + str(lb_1[1]) + '\n' + yourname + '\n' + str(yourscore) + '\n' + lb_3[0] + str(lb_3[1]) + '\n' + lb_4[0] + str(lb_4[1]) + '\n' + lb_5[0] + str(lb_5[1]))
                    print("Amazing! You got 4th on the leaderboard for winning scores.")
                elif yourplace == 3:
                    file.write(lb_1[0] + str(lb_1[1]) + '\n' + lb_2[0] + str(lb_2[1]) + '\n' + yourname + '\n' + str(yourscore) + '\n' + lb_4[0] + str(lb_4[1]) + '\n' + lb_5[0] + str(lb_5[1]))
                    print("Incredible! You got 3rd on the leaderboard for winning scores. Bronze medal to you!")
                elif yourplace == 2:
                    file.write(lb_1[0] + str(lb_1[1]) + '\n' + lb_2[0] + str(lb_2[1]) + '\n' + lb_3[0] + str(lb_3[1]) + '\n' + yourname + '\n' + str(yourscore) + '\n' + lb_5[0] + str(lb_5[1]))
                    print("Wait a second... you just got 2nd on the leaderboard for winning scores! Unbelievable!")
                elif yourplace == 1:
                    file.write(lb_1[0] + str(lb_1[1]) + '\n' + lb_2[0] + str(lb_2[1]) + '\n' + lb_3[0] + str(lb_3[1]) + '\n' + lb_4[0] + str(lb_4[1]) + '\n' + yourname + '\n' + str(yourscore))
                    print("Congratulations! You got a new world record! Your score is placed 1st on the leaderboard for winning scores!")
                lb_done = True
            else:
                print("Sorry, but your score wasn't high enough to get on the leaderboard! Better luck next time...\nYour score: " + str(yourscore) + "\n5th place score: " + str(lb_1[1]))
                lb_done = True
    else:
        if len(yourname) > 10:
            print("This username is too long. Please enter a name that is between 3 and 10 characters long!")
        elif len(yourname) < 3:
            print("This username is too short. Please enter a name that is between 3 and 10 characters long!")
print('\nThe leaderboard for winning scores now are:\n5th: ' + lb_1[0] + '> ' + str(lb_1[1]) + '\n4th: ' + lb_2[0] + '> ' + str(lb_2[1]) + '\n3rd: ' + lb_3[0] + '> ' + str(lb_3[1]) + '\n2nd: ' + lb_4[0] + '> ' + str(lb_4[1]) + '\n1st: ' + lb_5[0] + '> ' + str(lb_5[1]))
