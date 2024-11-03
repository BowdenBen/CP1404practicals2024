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


def display_projects(projects):
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [p for p in projects if p.is_complete()]
    incomplete.sort()
    complete.sort()
    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")
    print("Completed projects:")
    for project in complete:
        print(f"  {project}")

def filter_projects_by_date(projects):
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = [p for p in projects if p.start_date > date]
    filtered_projects.sort(key=lambda p: p.start_date)
    for project in filtered_projects:
        print(f"  {project}")

def add_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date_str = input("Start date (dd/mm/yyyy): ")
    start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    project = Project(name, start_date, priority, cost, completion)
    projects.append(project)

def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    project = projects[choice]
    print(project)
    completion = input("New completion percentage: ")
    if completion:
        project.update_completion(int(completion))
    priority = input("New priority: ")
    if priority:
        project.update_priority(int(priority))


#
# Call main function to run program
