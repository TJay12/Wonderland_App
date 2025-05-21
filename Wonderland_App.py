# pyinstaller --onefile Wonderland_App.py
import logging
import traceback
import datetime

# <--- Logging --->
logging.basicConfig(
    filename="logging.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

#----------------------------------------------------   <---Functions--->
# <--- Function to take/store and validate score values
#      as well as calculate average score --->
def input_results(learner_name):
    while True:
        # Make sure the entered value is a number
        try:
            math_score = int(input(f"Enter {learner_name}'s Math Score: "))
            if  math_score < 0 or math_score > 100:
                print("Make sure score is in range (0 - 100)")
                logging.warning("Entered number out of score range")
                continue
            eng_score = int(input(f"Enter {learner_name}'s English Score: "))
            if eng_score < 0 or eng_score > 100:
                print("Make sure score is in range (0 - 100)")
                logging.warning("Entered number out of score range")
                continue
            sci_score = int(input(f"Enter {learner_name}'s Science Score: "))
            if sci_score < 0 or sci_score > 100:
                print("Make sure score is in range (0 - 100)")
                logging.warning("Entered number out of score range")
                continue
            break
        # If not number entered, don't crash
        except:
            print("Please enter a numerical value (0 - 100)")
            logging.warning(f"Non numerical values entered in scores")

    # All scores stored in a list
    scores = [math_score, eng_score, sci_score]
    logging.info(f"{learner_name}s scores input successfully: {scores}")

    # Calculate Average of scores
    avg_score = int((math_score + eng_score + sci_score) / 3)
    logging.info(f"Average score for {learner_name} calculated: {avg_score}")
    # return the values scores and average
    return scores, avg_score

# <--- Function to calculate grade from score --->
def calculate_grade(score):
    if score > 90:
        grade = "A"
    elif score > 80:
        grade = "B"
    elif score > 70:
        grade = "C"
    elif score > 60:
        grade = "D"
    else:
        grade = "F"
    logging.info(f"Grade calculated: {grade} from score: {score}")
    # Return the value grade
    return grade

# <--- Main Function to run Program --->
def main():
    while True:
        learner_name = input("Enter Learners Name: ").lower().capitalize()
        # Get scores and average from input_results() function
        learner_scores, learner_avg_score = input_results(learner_name)
        # create blank list to store grades in
        grades = []
        # For each of the values in learner_scores,
        for value in learner_scores:
            score = int(value)
            # calculate grade with calculate_grade() function,
            grading = calculate_grade(score)
            # store grade in grades list
            grades.append(grading)
        # Print the results
        print(f"{learner_name.capitalize()}'s Results:")
        print(f"Maths:   {learner_scores[0]} \t Grade: {grades[0]}")
        print(f"English: {learner_scores[1]} \t Grade: {grades[1]}")
        print(f"Science: {learner_scores[2]} \t Grade: {grades[2]}")
        print(f"Average Score: {learner_avg_score}")
        logging.info(f"{learner_name}s Scores Grades and Average successfully printed")
        # Check if the user want's to add another entry
        while True:
            cont = input("Do you have another entry (y/n): ").lower()
            if cont == "n":
                # End the program
                print("Thank you for using this app")
                logging.info("User input app termination")
                break
            elif cont == "y":
                logging.info("User input running again")
                break
            else:
                print("Invalid Option")
                logging.warning(f"{cont} Invalid Option")
        if cont == "n":
            break

#-------------------------------------------------   <--- Run Program --->
if __name__ == "__main__":
    try:
        main()
# <--- Error Logging --->
    except Exception as e:
        error_message = f"An error occurred: \n{traceback.format_exc()}"
        logging.error(error_message)
        input("An error occurred. Check logging.txt for details."
              "\nPress Enter to exit...")
