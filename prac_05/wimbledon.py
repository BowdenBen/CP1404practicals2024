"""
Write a program to read wimbledon.csv, process the data and display processed information.
- the champions and how many times they have won.
- the countries of the champions in alphabetical order
By Benjamin Bowden
Estimate: 50 minutes
Actual:   minutes
"""

filename = "wimbledon.csv"

def read_file(filename):
    """Read the file and return the data as a list of lists."""
    champions_data = []  # List of lists to store the data
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)  # Skip the header
        for line in in_file:
            champions_data.append(line.strip().split(","))  # Split each line into a list of fields
    return champions_data


def count_champion_wins(champions_data):
    """Create and return a dictionary with champions and their win counts."""
    champion_wins = {}  # Dictionary to store champion names and their win counts
    for champion in champions_data:
        champion_name = champion[2]  # Champion's name is in the 3rd column (index 2)
        if champion_name in champion_wins:
            champion_wins[champion_name] += 1
        else:
            champion_wins[champion_name] = 1
    return champion_wins


def get_countries(champions_data):
    """Create and return a sorted list of unique countries of champions."""
    countries = set()  # Set to store unique countries
    for champion in champions_data:
        countries.add(champion[1])  # Champion's country is in the 2nd column (index 1)
    return sorted(countries)  # Return the sorted list of countries


def main():
    """Main function to drive the program."""
    champions_data = read_file(filename)
    champion_wins = count_champion_wins(champions_data)
    countries = get_countries(champions_data)

    # Display champions and their win counts
    print("Champions and their number of wins:")
    for champion, wins in champion_wins.items():
        print(f"{champion:18} {wins}")

    # Display countries that have won Wimbledon
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


if __name__ == "__main__":
    main()