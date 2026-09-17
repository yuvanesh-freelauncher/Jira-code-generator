project_code = input("Enter project code: ")

bug_number = 1

while True:
    bug_description = input("\nEnter bug description: ")

    bug_code = project_code + "-" + str(bug_number)

    print("Generated Bug Code:", bug_code)
    print("Bug Description:", bug_description)

    bug_number = bug_number + 1

    choice = input("\nDo you want to add another bug? (yes/no): ")

    if choice.lower() == "no":
        break
