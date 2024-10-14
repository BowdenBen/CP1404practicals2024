"""
Write a program to read wimbledon.csv, process the data and display processed information.
- the champions and how many times they have won.
- the countries of the champions in alphabetical order
By Benjamin Bowden
Estimate: 50 minutes
Actual:   minutes
"""

filename = "wimbledon.csv"

def process_file(filename):
    """Open the data file, extract and process information"""
    # Initialise dictionary and list needed
    champions = []
    champions_dict = {}
    champion_countries = set() # creates an empty set in Python
    with open(filename, "r", encoding="utf-8-sig") as file: # open file using utf 8 encoding
        next(file) # skip the first line of the file
        for line in file:
            data = line.strip().split(",") # strip removes leading and lagging space, split us comma as delimiter

            # Unpack the data into meaningful variables
            year, champion_country, champion, runner_up_country, runner_up, score = data

            # Append to the list of champions
            champions.append([year, champion_country, champion, runner_up_country, runner_up, score])

            # Update the champions dictionary (count the number of wins per champion)
            if champion in champions_dict:
                champions_dict[champion] += 1
            else:
                champions_dict[champion] = 1

            champion_countries.add(champion_country)

    return champions, champions_dict, champion_countries

def display_champions(champions_dict):
    """Display the champions and their win counts."""
    for champion, wins in sorted(champions_dict.items()):
        print(f"{champion} {wins}")


def display_countries(champion_countries):
    """Display the countries in alphabetical order."""
    sorted_countries = sorted(champion_countries)
    print(", ".join(sorted_countries))

def main():
    PRINT "Wimbledon Champions:"
    CALL display_champions(champions_dict)
    PRINT "These countries have won Wimbledon:"
    CALL display_countries(countries_set)

if __name__ == "__main__":
    main()