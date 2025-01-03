import wikipedia
from wikipedia import PageError, DisambiguationError


def main():
    print("Welcome to the Wikipedia Search Engine.")
    title = input("Please enter a title or search phrase.\n>>>  ")
    while title != "":
        try:
            page = wikipedia.page(title, auto_suggest=False)
            print(f"\n{page.title}\n")
            print(page.url)
            print(f"\n{page.summary[:1000]}...")
        except PageError:
            # Handle page not found error
            print(f"\nPage id \"{title}\" does not match any pages. Try another id!")
        except DisambiguationError as e:
            print(f"\nPage ID \"{title}\" does not match any pages. Try one of the following pages:\n")
            print(e.options)
        title = input("Please enter a title or search phrase.\n>>>  ")
    print("Thank you for using this program.")

if __name__ == "__main__":
    main()
