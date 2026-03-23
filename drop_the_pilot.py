def main():
    print("Quiz: name the famous Joan Armatrading song that opens with this lyric:")
    print("\"I'm right on target, my aim is straight\"")
    print("(Hint: the next line goes \"So you're in love, I say what of it\")")
    answer = input("Enter the song name: ").strip()

    if answer.lower() == "drop the pilot":
        print("Well done")
    else:
        print("Bad luck")


if __name__ == "__main__":
    main()
