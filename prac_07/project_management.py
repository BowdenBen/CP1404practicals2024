"""
Time to completion EST: 1 hour
Actual Time to Completion:
"""

import datetime
import csv
from project import Project


def main():
    projects = load_projects("projects.txt")
    print(f"Loaded {len(projects)} projects from projects.txt")

    while True:
        print(
            "\n- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit")
        choice = input(">>> ").lower()

        if choice == 'l':
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Filename: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            if input("Would you like to save to projects.txt? (y/n): ").lower() == 'y':
                save_projects("projects.txt", projects)
            break
        else:
            print("Invalid option")


def load_projects(filename):
    projects = []
    with open(filename, 'r') as file:
        next(file)  # Skip the header line
        for line in file:
            name, start_date, priority, cost, completion = line.strip().split('\t')
            start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
            project = Project(name, start_date, int(priority), float(cost), int(completion))
            projects.append(project)
    return projects

def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost\tCompletion\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost}\t{project.completion}\n")


# 4. Define display_projects function with parameter projects:
#     Initialize empty list for incomplete_projects and complete_projects
#     For each project in projects:
#         If project is complete, add to complete_projects list
#         Else, add to incomplete_projects list
#     Sort incomplete_projects and complete_projects by priority
#     Print incomplete projects
#     Print complete projects
#
# 5. Define filter_projects_by_date function with parameter projects:
#     Prompt user for date input
#     Convert date input to date object
#     Initialize empty list for filtered_projects
#     For each project in projects:
#         If project start_date is after input date, add to filtered_projects list
#     Sort filtered_projects by start_date
#     Print each project in filtered_projects
#
# 6. Define add_project function with parameter projects:
#     Prompt user for project details: name, start_date, priority, cost, completion
#     Convert start_date to date object, priority to integer, cost to float, completion to integer
#     Create Project object with user inputs
#     Append Project object to projects list
#
# 7. Define update_project function with parameter projects:
#     Display each project with an index
#     Prompt user to select project index
#     Get selected project from projects list
#     Prompt for new completion percentage and new priority
#     If new completion is entered, update project completion
#     If new priority is entered, update project priority
#

#
# Call main function to run program
