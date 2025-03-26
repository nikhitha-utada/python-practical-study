# Mini Project: Story Generator Using Function

# Objective:
# Create an interactive story generator where users input choices, and the program generates a unique short story based on those choices.

# How It Works:
# The user selects a character (e.g., Detective, Scientist, or Explorer).
# The user selects a location (e.g., Forest, Space, or Ancient Ruins).
# The program generates a random event that happens in the story.
# Based on these inputs, a custom story is displayed.

# Functions to Implement:
# choose_character() → Lets the user pick a character.
# choose_location() → Lets the user pick a setting.
# generate_event() → Randomly selects an event (e.g., "finds a secret map" or "meets an alien").
# create_story(character, location, event) → Generates a short story using the inputs.
# start_story_generator() → Controls the flow of the program.

import random

# Function to choose a character
def choose_character():
    characters = ["Detective", "Scientist", "Explorer"]
    print("Choose a character:")
    for i, char in enumerate(characters, 1):
        print(f"{i}. {char}")
    
    choice = int(input("Enter your choice (1-3): "))
    return characters[choice - 1] if 1 <= choice <= 3 else "Unknown"

# Function to choose a location
def choose_location():
    locations = ["Forest", "Space", "Ancient Ruins"]
    print("\nChoose a location:")
    for i, loc in enumerate(locations, 1):
        print(f"{i}. {loc}")
    
    choice = int(input("Enter your choice (1-3): "))
    return locations[choice - 1] if 1 <= choice <= 3 else "Unknown"

# Function to generate a random event
def generate_event():
    events = [
        "finds a hidden treasure",
        "gets trapped in a mysterious cave",
        "discovers an ancient artifact",
        "meets a talking animal",
        "encounters a secret society",
        "finds a hidden portal to another dimension"
    ]
    return random.choice(events)

# Function to create the story
def create_story(character, location, event):
    story = f"\nYour story:\n{character} went on an adventure to the {location}. " \
            f"While exploring, they suddenly {event}! What happens next is a mystery...\n"
    return story

# Main function to start the story generator
def start_story_generator():
    print("Welcome to the Interactive Story Generator!\n")
    
    character = choose_character()
    location = choose_location()
    event = generate_event()

    story = create_story(character, location, event)
    print(story)

# Run the story generator
start_story_generator()

    