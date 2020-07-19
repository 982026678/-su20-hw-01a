# su20-hw-01a


# display title
print()
print("Test Scores Program")
print("You will be prompted to Enter 3 test scores below.")
print()
print("====================")

# get scores from the user and sum the total
##total_score = 0
##total_score += int(input("Enter Test Score: "))
##total_score += int(input("Enter Test Score: "))
##total_score += int(input("Enter Test Score: "))

score_01 = int(input("Enter Test Score: "))
score_02 = int(input("Enter Test Score: "))
score_03 = int(input("Enter Test Score: "))
total_score = score_01+score_02+score_03

# calculate average score
average_score = round(total_score / 3)

# format and display the result
print("====================")
print(f'Your Scores:\t {score_01} {score_02} {score_03}')
print(f'Total Score:\t {total_score}')
print(f'Average Score:\t {average_score}')
print()
print('End of Program.')
