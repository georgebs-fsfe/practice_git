def main():
    print("Quiz: name the famous Joan Armatrading song that opens with this lyric:")
    print("\"I'm right on target, my aim is straight\"")
    print("(Hint: the artist initials are J.A.)")
    answer = input("Enter the artist name: ").strip()

    if answer.lower() == "joan armatrading":
        print("Well done")
    else:
        print("Bad luck")


if __name__ == "__main__":
    main()
