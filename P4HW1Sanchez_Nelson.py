# Nelson Sanchez
# 3/23/2026
# P4WH1
# Collects user imput grades, removes lowest score, averages scores and assigns a letter grade.

#Pseudocode

# 1.Prompt the user to enter how many scores they want to input.
# 2.Initialize an empty list to store valid scores.
# 3.Initialize a counter to track the number of scores entered.
# 4.While the count of valid scores is less than the number requested:
#   a. Prompt user to enter a score with the current score number.
#   b. Check if the entered score is an integer between 0 and 100.
#       - If invalid, print an error message and ask for that score again.
#       - If valid, add the score to the list and increment the count.
# 5.Find the lowest score in the list.
# 6.Remove the lowest score from the list.
# 7.Calculate the average of the remaining scores.
# 8.Determine the letter grade based on the average:
#   - A: 90 and above
#   - B: 80 to 89.99
#   - C: 70 to 79.99
#   - D: 60 to 69.99
#   - F: below 60
# 9.Print the lowest score, the modified list, the average, and the letter grade.



# Letter Grades
def get_letter_grade(avg_score):
    if avg_score >= 90:
        return "A"
    elif avg_score >= 80:
        return "B"
    elif avg_score >= 70:
        return "C"
    elif avg_score >= 60:
        return "D"
    else:
        return "F"

def main():
    # Step 1: Ask how many scores to enter
    while True:
        try:
            total_scores = int(input("How many scores do you want to enter? "))
            if total_scores <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    scores = []
    score_index = 1

    # Step 4: Collect scores with validation
    while len(scores) < total_scores:
        try:
            score = float(input(f"Enter score #{score_index}: "))
            if 0 <= score <= 100:
                scores.append(score)
                score_index += 1
            else:
                print("\nINVALID Score entered!!!!")
                print("Score should be between 0 and 100")
                # Prompt to re-enter the same score number again
        except ValueError:
            print("\nInvalid input! Please enter a numeric score.")
            # Prompt to re-enter the same score number again

    # Step 5 & 6: Remove lowest score
    lowest_score = min(scores)
    scores.remove(lowest_score)

    # Step 7: Calculate average of modified list
    average_score = sum(scores) / len(scores)

    # Step 8: Determine letter grade
    grade = get_letter_grade(average_score)

    # Step 9: Display results
    print("\n-------------Results-------------")
    print(f"Lowest Score   : {lowest_score}")
    print(f"Modified List  : {scores}")
    print(f"Scores Average : {average_score:.2f}")
    print(f"Grade          : {grade}")
    print("--------------------------------")

if __name__ == "__main__":
    main()