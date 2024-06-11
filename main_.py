def main():
    print("Welcome to the Essay Grading System!")
    while True:
        essay = input("Enter your essay (or type 'exit' to quit): ")
        if essay.lower() == 'exit':
            break
        else:
            predicted_grade = predict_grade0(essay)
            predicted_grade = predict_grade1(essay)
            predicted_grade = predict_grade2(essay)


main()
