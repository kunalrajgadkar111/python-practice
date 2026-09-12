text = "  Python Programming is Amazing  "

print("Original:", text)

print("Upper:", text.upper())
print("Lower:", text.lower())
print("Title:", text.title())
print("Capitalized:", text.strip().capitalize())

clean_text = text.strip()
print("Stripped:", clean_text)

print("Replace:", clean_text.replace("Amazing", "Powerful"))

print("Starts with Python:", clean_text.startswith("Python"))
print("Ends with Amazing:", clean_text.endswith("Amazing"))

print("Count of 'm':", clean_text.lower().count("m"))

words = clean_text.split()
print("Words:", words)

joined_text = "-".join(words)
print("Joined:", joined_text)