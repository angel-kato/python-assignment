# Ask user for their name
name = input("Enter your name: ")

# Ask what they achieved
achievement = input("What did you achieve? ")

# Create congratulations message using string concatenation
message = "Congratulations " + name + "! 🎉 " + \
          "You have successfully achieved " + achievement + "."

# Convert message to uppercase
print(message.upper())

# Print length of the message
print("Message length:", len(message))
