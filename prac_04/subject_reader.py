"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"  # The name of the file containing subject data

def main():
    """Main function to load and display subject data."""
    data = load_data()  # Load the data from the file into a list
    print(data)  # Print the raw data list (existing functionality)
    display_subject_details(data)  # Call the function to display formatted subject details


def load_data():
    """
    Read data from the file formatted like: subject,lecturer,number of students.
    Returns a list of lists where each sublist contains subject, lecturer, and number of students.
    """
    input_file = open(FILENAME)  # Open the file for reading
    data = []  # Initialize an empty list to hold the processed data
    for line in input_file:  # Loop through each line in the file
        line = line.strip()  # Remove any leading/trailing whitespace, including newline characters
        parts = line.split(',')  # Split the line into parts using a comma as the delimiter
        parts[2] = int(parts[2])  # Convert the third part (number of students) from a string to an integer
        data.append(parts)  # Append the processed line (as a list) to the data list
    input_file.close()  # Close the file once all data has been processed
    return data  # Return the list of processed data


def display_subject_details(data):
    """
    Display subject details in a formatted manner.
    Accepts a list of lists (data) where each sublist contains subject, lecturer, and number of students.
    Outputs the details in the format: "subject is taught by lecturer and has number of students".
    """
    for subject in data:  # Loop through each list in the data
        # Unpack and format the subject, lecturer, and number of students into a human-readable string
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")


# Call the main function to execute the program
main()
