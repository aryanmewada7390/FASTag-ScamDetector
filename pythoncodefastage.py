# FASTag Scam Awareness & Detection Tool

# List of suspicious keywords
suspicious_keywords = [
    "free", "cashback", "offer", "urgent", "click now",
    "limited time", "win", "prize", "verify", "update",
    "bank", "fastag", "recharge now"
]

# List of suspicious domains
suspicious_domains = [
    "bit.ly", "tinyurl", "shorturl", "goo.gl"
]


def check_link():
    link = input("\nEnter the link: ").lower()

    risk_score = 0

    # Check for suspicious domains
    for domain in suspicious_domains:
        if domain in link:
            print(" Suspicious shortened URL detected!")
            risk_score += 2

    # Check for keywords
    for word in suspicious_keywords:
        if word in link:
            risk_score += 1

    # Result
    print("\n--- Result ---")
    if risk_score >= 3:
        print("High Risk: This link may be a SCAM!")
    elif risk_score == 2:
        print("Medium Risk: Be careful before using this link.")
    else:
        print("Low Risk: Link looks relatively safe.")


def analyze_message():
    message = input("\nPaste the message: ").lower()

    risk_score = 0
    found_words = []

    for word in suspicious_keywords:
        if word in message:
            risk_score += 1
            found_words.append(word)

    print("\n--- Analysis ---")
    if found_words:
        print("Suspicious words found:", ", ".join(found_words))
    else:
        print("No suspicious keywords detected.")

    if risk_score >= 3:
        print("High Risk: This message may be a SCAM!")
    elif risk_score == 2:
        print("Medium Risk: Be cautious.")
    else:
        print("Low Risk: Seems safe.")


def show_tips():
    print("\n--- Safety Tips ---")
    print("1. Never click on unknown recharge links.")
    print("2. Always use official apps/websites.")
    print("3. Avoid offers that sound too good to be true.")
    print("4. Do not share OTP or bank details.")
    print("5. Check URL carefully before payment.")
    print("6. Avoid shortened links (bit.ly, tinyurl).")
    print("7. Verify messages from official sources.")
    print("8. Use trusted payment platforms.")
    print("9. Don't panic if message says 'urgent'.")
    print("10. When in doubt, don't click!")


def main():
    while True:
        print("\n===== FASTag Scam Detector =====")
        print("1. Check a Link")
        print("2. Analyze a Message")
        print("3. Safety Tips")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            check_link()
        elif choice == "2":
            analyze_message()
        elif choice == "3":
            show_tips()
        elif choice == "4":
            print("Exiting... Stay safe!")
            break
        else:
            print("Invalid choice. Try again.")


# Run the program
if __name__ == "__main__":
    main()