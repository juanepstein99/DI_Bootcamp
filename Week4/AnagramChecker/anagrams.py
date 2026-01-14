from anagram_checker import AnagramChecker

checker = AnagramChecker("word_list.txt")

while True:
    print("1) Enter a word")
    print("2) Exit")

    choice = input("Choose: ").strip()

    if choice == "2":
        print("Bye")
        break

    if choice != "1":
        print("Invalid option\n")
        continue

    user_word = input("Type a word: ").strip()

    if len(user_word.split()) != 1:
        print("Error: Only one word allowed\n")
        continue

    if not user_word.isalpha():
        print("Error: Only letters allowed\n")
        continue

    valid = checker.is_valid_word(user_word)

    print(f'\nYOUR WORD: "{user_word.upper()}"')

    if valid:
        print("This is a valid English word.")
        anagrams = checker.get_anagrams(user_word)

        if anagrams:
            print("Anagrams for your word:", ", ".join(anagrams))
        else:
            print("No anagrams found.")
    else:
        print("This is NOT a valid English word.")

    print()