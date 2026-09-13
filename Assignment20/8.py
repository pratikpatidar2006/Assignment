while True:

    print("\n===== Smart Text Processing System =====")
    print("1. Reverse Complete String")
    print("2. Reverse Every Word")
    print("3. Reverse Word Order")
    print("4. Exit")

    ch = int(input("Enter Choice: "))

    # -------------------- Choice 1 --------------------
    if ch == 1:

        s = input("Enter String: ")

        # Remove extra spaces
        words = s.split()
        s = ""
        for i in range(len(words)):
            s += words[i]
            if i != len(words)-1:
                s += " "

        letters = ""

        # Store only alphabets
        for c in s:
            if c.isalpha():
                letters += c

        # Reverse manually
        rev = ""
        i = len(letters)-1
        while i >= 0:
            rev += letters[i]
            i -= 1

        ans = ""
        j = 0

        # Keep special characters fixed
        for c in s:
            if c == '@' or c == '#' or c == '$' or c == '%':
                ans += c
            else:
                ans += rev[j]
                j += 1

        print("Output:", ans)

    # -------------------- Choice 2 --------------------
    elif ch == 2:

        s = input("Enter String: ")

        words = s.split()

        for w in words:

            digit = False

            for c in w:
                if c.isdigit():
                    digit = True
                    break

            if digit:
                print(w, end=" ")
            else:
                rev = ""
                i = len(w)-1

                while i >= 0:
                    rev += w[i]
                    i -= 1

                # First letter uppercase
                first = rev[0].upper()
                print(first + rev[1:], end=" ")

        print()

    # -------------------- Choice 3 --------------------
    elif ch == 3:

        s = input("Enter String: ")

        words = s.split()

        unique = []

        # Remove duplicates (keep first occurrence)
        for w in words:
            found = False

            for x in unique:
                if w.lower() == x.lower():
                    found = True
                    break

            if not found:
                unique.append(w)

        # Print reverse order manually
        i = len(unique)-1

        while i >= 0:
            print(unique[i], end=" ")
            i -= 1

        print()

    # -------------------- Choice 4 --------------------
    elif ch == 4:
        print("Program Closed Successfully")
        break

    else:
        print("Invalid Choice")