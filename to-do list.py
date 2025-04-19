entries = []

while True:
    print("To-Do List")
    input_response = input("Please type 'Add' to add a task; 'Delete' to remove a task; 'Show List' to view current list; 'Exit' to exit program: ")
    
    if input_response == "Add" or input_response == "add" :

        subject = input("Enter a subject for task: ")
        body = input("Enter a description for the task: ")

        if subject and body:
            entry = {'Subject': subject, 'Description': body}
            entries.append(entry)
            print(f"Subject: {entry['Subject']}\nDescription: {entry['Description']}.")
        else:
            print("Inputs cannot be empty.")

    elif input_response == "Delete" or input_response == "delete":
        if not entries:
            print("No entries to delete.")
        else:
            # Show all entries with numbers
            print("All entries:")
            for i, entry in enumerate(entries, 1):
                print(f"{i}. Subject: {entry['Subject']}\nDescription: {entry['Description']}.")

            # Get index to delete
            try:
                index = int(input("Enter the number of the entry to delete: "))
                # Convert to 0 based index
                if 1 <= index <= len(entries):
                    removed_entry = entries.pop(index-1) # Remove and get the entry
                    print(f"Deleted entry:\nSubject: {removed_entry['Subject']}\nDescription {removed_entry['Description']}.")
                else:
                    print(f"Invalid number. Please enter a number between 1 and {len(entries)}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    elif input_response == "Show List" or input_response == "show list":
        if entries:
            print("All entries:")
            for i, entry in enumerate(entries, 1):
                print(f"{i}. Subject: {entry['Subject']}\nDescription: {entry['Description']}")
        else:
            print("No entries to display.")

    elif input_response == "Exit" or input_response == "exit":
        while True:
            input_quit = input("Are you sure you want to quit application (Y/N)?: ")
            if input_quit == 'Y' or input_quit == 'y':
                print("Program ended.")
                exit()
            elif input_quit == 'N' or 'n':
                break # Return to main loop
            else:
                print("Invalid command.")

    else:
        print("Not a valid input.")

    

