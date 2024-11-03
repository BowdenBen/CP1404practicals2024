"""
Time to completion EST: 1 hour
Actual Time to Completion:
"""

# 1. Import Project class and datetime module
#
# 2. Define load_projects function with parameter filename:
#     Open filename in read mode
#     Skip the header line
#     Initialize empty list for projects
#     For each line in file:
#         Split line into name, start_date, priority, cost, and completion
#         Parse start_date using datetime to convert to date object
#         Create Project object with parsed data
#         Append Project object to projects list
#     Return projects list
#
# 3. Define save_projects function with parameters filename and projects:
#     Open filename in write mode
#     Write header line
#     For each project in projects:
#         Write project data in formatted string to file
#
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
# 8. Define main function:
#     Load projects from "projects.txt" by calling load_projects
#     Print welcome message with number of loaded projects
#
#     While True:
#         Print menu options
#         Get user choice
#
#         If choice is 'L' (Load projects):
#             Prompt user for filename
#             Call load_projects with filename and update projects list
#
#         If choice is 'S' (Save projects):
#             Prompt user for filename
#             Call save_projects with filename and current projects list
#
#         If choice is 'D' (Display projects):
#             Call display_projects with current projects list
#
#         If choice is 'F' (Filter projects by date):
#             Call filter_projects_by_date with current projects list
#
#         If choice is 'A' (Add new project):
#             Call add_project with current projects list
#
#         If choice is 'U' (Update project):
#             Call update_project with current projects list
#
#         If choice is 'Q' (Quit):
#             Prompt user to save to "projects.txt" if desired
#             Break loop to quit program
#
#         If choice is invalid:
#             Print error message for invalid input
#
# Call main function to run program
