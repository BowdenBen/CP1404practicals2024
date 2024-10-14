"""
Write a program to read wimbledon.csv, process the data and display processed information.
- the champions and how many times they have won.
- the countries of the champions in alphabetical order
By Benjamin Bowden
Estimate: 50 minutes
Actual:   minutes
"""

FUNCTION process_file(file):
    INIT empty list matches, dictionary champions_dict, set countries_set
    SKIP header line
    FOR each line in file:
        SPLIT line by commas
        ADD match data to matches
        INCREMENT champion's count in champions_dict
        ADD champion's country to countries_set
    RETURN matches, champions_dict, countries_set

FUNCTION display_champions(champions_dict):
    FOR each champion, wins in champions_dict:
        PRINT champion, wins

FUNCTION display_countries(countries_set):
    SORT countries_set
    PRINT ', '.join(countries_set)

FUNCTION main():
    OPEN file "wimbledon_data.csv" with encoding "utf-8-sig"
    champions_list, champions_dict, countries_set = process_file(file)
    PRINT "Wimbledon Champions:"
    CALL display_champions(champions_dict)
    PRINT "These countries have won Wimbledon:"
    CALL display_countries(countries_set)
    CLOSE file
