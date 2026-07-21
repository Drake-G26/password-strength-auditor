# Password Strength Auditor - by Drake Garcia
# Checks a password's length and character variety, then scores it 0-5

print("Password Auditor is alive!")

while True: 
    entry = input("Enter a password to audit (or 'quit'): ")

    if entry == "quit": 
        print("Goodbye!")
        break

    print("Length: ", len(entry))

    # Reset flags for each new password
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for char in entry: 
        if char.isupper():
            has_upper = True 
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        else: 
            has_symbol = True 
    # Award one point per strength factor, max score out of 5
    score = 0

    if len(entry) >= 8:
        score += 1 
    if has_upper: 
        score += 1
    if has_lower: 
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1

    print("Score: ", score, "out of 5")

    if score <= 2: 
        print("Verdict: WEAK")
    elif score <= 4: 
        print("Verdict: DECENT")
    else: 
        print("Verdict: STRONG")