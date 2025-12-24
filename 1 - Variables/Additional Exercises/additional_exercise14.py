#16-01-2012
#additional exercise 14
#sample solution

def quote_formatter():
    print("Quote Formatter")
    print("This program displays a given quote in different formats")
    quote = input("Enter a quote: ")
    print("Original quote: ", quote)
    print("Uppercase: ", quote.upper())
    print("Lowercase: ", quote.lower())
    # Erstes Wort groß schreiben
    print("Capitalize: ", quote.capitalize())
    # Titelweise schreiben (erstes Wort jedes Wortes groß)
    print("Title case: ", quote.title())
    # Ersetzen eines Wortes
    replace_word = input("Enter a word to replace in the quote: ")
    replace_with = input("Enter the word to replace it with: ")
    # Ersetzen des Wortes und Ausgabe
    if replace_word in quote:
        print("Original quote (after replacement): ", quote.replace(replace_word, replace_with))
    else:
        print(f"The word '{replace_word}' wasn't found in the quote.")
# Funktionsaufruf
quote_formatter()


