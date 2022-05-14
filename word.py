from random import choice
from os import listdir

def get_files():
    files = []
    for file in listdir("themes"):
        files.append(file[:-4])
    return files

files = get_files()

def get_words(name):
    if name in files:
        try:
            file = open(f"themes/{name}.csv")
            content = file.read()
            return content.split(',')
        except FileNotFoundError:
            print("File doesn't exist")
    return None


def pick_random_word(theme):
    words = get_words(theme)
    if not words:
        print("Coudn't get a word.")
        return None
    return choice(words)

def valid_theme(theme):
    return theme in files

def display_themes():
    themes = ", ".join(files)
    print(f"Themes: {themes}.")