import wikipedia

def main():
    print("Welcome to the Wikipedia Search Engine.")
    title = input("Please enter a title or search phrase.\n>>>  ")
    while title != "":
        page = wikipedia.page(title, auto_suggest=False)
        print(f"\n{page.title}\n")
        print(page.url)
        print(f"\n{page.summary[:1000]}...")
        title = input("Please enter a title or search phrase.\n>>>  ")
    print("Thank you for using this program.")

if __name__ == "__main__":
    main()
