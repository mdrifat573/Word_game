# Name:  Md Rifat Hasan
# Student Number:  10736531

import random

# Create lists of 100 6-letter, 7-letter and 8-letter words that are similar enough to work well for this game.
easy_words = ['AETHER', 'ANSWER', 'AROUND', 'BADDER', 'BALDER', 'BANDED', 'BANKER', 'BANTER', 'BARBER', 'BASHED', 'BASHER', 'BATHED', 'BATHER', 'BATTER', 'BEAKER', 'BEANED', 'BEATER', 'BEAVER', 'BEDDER', 'BEFORE', 'BEHIND', 'BENDER', 'BETTER', 'BOLDER', 'BOLTER', 'BOMBER', 'BORDER', 'BOTHER', 'BOTTLE', 'BOWLER', 'BRACER', 'BRIDGE', 'BROKEN', 'BUMPER', 'BUSIER', 'BUTTON', 'CANDLE', 'CHARGE', 'CIRCLE', 'CLOSED', 'CORNER', 'CREATE', 'CREDIT', 'DANGER', 'DEADER', 'DEAFER', 'DEARER', 'DELVER', 'DEMAND', 'DENSER', 'DESIGN', 'DETECT', 'DEVICE', 'DEXTER', 'DOUBLE', 'DRIVER', 'ENERGY', 'ENGINE', 'ESCAPE', 'EVADER', 'EXPERT', 'FATHER', 'FENDER', 'GARDEN', 'GATHER', 'HEARER', 'HEIFER', 'HERDER', 'JESTER', 'JUDDER', 'KIDDER', 'LEADER', 'LEAPER', 'LEASER', 'LEVIED', 'LEVIER', 'LEVIES', 'MADDER', 'MEANER', 'MENDER', 'MINDER', 'NEATER', 'NEEDED', 'NESTED', 'PESTER', 'PEWTER', 'PONDER', 'REALER', 'REAVER', 'RENDER', 'SEEDER', 'SETTER', 'TEMPER', 'TENDER', 'TENNER', 'VENDER', 'WEDDER', 'WEEDED', 'WELDER', 'YONDER']
medium_words = ['ACTIONS', 'ANOTHER', 'ARRIVAL', 'BALANCE', 'BANDAGE', 'BANKERS', 'BANTERS', 'BARBERS', 'BARRING', 'BATTERS', 'BEACONS', 'BEATERS', 'BEATING', 'BEAVERS', 'BETTERS', 'BLAMING', 'BLUSTER', 'BOMBERS', 'BONKERS', 'BORDERS', 'BOTHERS', 'BOWLERS', 'BRACERS', 'BRIDGES', 'BROKERS', 'BURPING', 'BUTTONS', 'CANDLES', 'CHARGED', 'CHARGER', 'CIRCLED', 'CLOSERS', 'CLOSURE', 'CONNING', 'CREATED', 'CREATOR', 'CREDITS', 'DANGERS', 'DECADES', 'DEFENDS', 'DELIVER', 'DEMANDS', 'DENIERS', 'DEPUTES', 'DESIGNS', 'DETECTS', 'DEVICES', 'DISCORD', 'DRIVERS', 'DROVERS', 'DUSTERS', 'ELOPING', 'EXPERTS', 'FARMERS', 'FATHERS', 'GARDENS', 'GATHERS', 'HEARERS', 'HEIFERS', 'HERDERS', 'JESTERS', 'JUDDERS', 'KIDDERS', 'LEADERS', 'LEAPERS', 'LEASERS', 'LOOKERS', 'MARKERS', 'MEANDER', 'MENDERS', 'MILKERS', 'MINDERS', 'NESTERS', 'NETHERS', 'PESTERS', 'PEWTERS', 'PLANERS', 'PLANETS', 'POCKETS', 'PONDERS', 'READERS', 'REAVERS', 'RENDERS', 'RENTERS', 'RINGING', 'SEEDERS', 'SEEDING', 'SETTERS', 'SETTING', 'TANKERS', 'TARGETS', 'TENDERS', 'TENNERS', 'VENDERS', 'WEEDERS', 'WELDERS', 'WELDING', 'WINDOWS', 'WORKERS', 'WRITERS']
hard_words = ['ABRIDGED', 'ABSOLVED', 'ABSORBED', 'ACCEPTED', 'ACQUIRED', 'ADMITTED', 'ADVANCED', 'ADVERTED', 'AFFECTED', 'ALLOTTED', 'ANALYZED', 'ANIMATED', 'ANNULLED', 'APPROVED', 'ARRANGED', 'ASSIGNED', 'ASSUMING', 'ATTACHED', 'ATTEMPTS', 'ATTRACTS', 'AVERTING', 'BALANCED', 'BANTERED', 'BOTHERED', 'BUILDING', 'BUTTONED', 'CANDIDLY', 'CARRIAGE', 'CHARGING', 'COMBINED', 'CONCLAVE', 'CONCLUDE', 'CONSIDER', 'CONTAINS', 'CONTENTS', 'CONTROLS', 'CREATION', 'CREATIVE', 'CREDITED', 'CREDITOR', 'DECIDING', 'DECLINED', 'DECREASE', 'DEEPENED', 'DESIGNED', 'DETECTED', 'DETECTOR', 'DETESTED', 'DETRACTS', 'DISABLED', 'DISCOVER', 'EFFECTED', 'EMERGING', 'ENRICHED', 'ENROLLED', 'ERUPTING', 'EXCITING', 'EXCLUDES', 'EXECUTED', 'EXPANDED', 'EXPANDER', 'EXPELLED', 'EXPLORED', 'EXPLORER', 'EXTENDED', 'FINALISE', 'FINISHED', 'FINISHER', 'FLUSHING', 'HAPPENED', 'HEARINGS', 'HELPINGS', 'IDENTITY', 'IMAGINED', 'IMPROVED', 'INCLUDED', 'INCREASE', 'INFORMED', 'INVITING', 'INVOLVED', 'LEARNING', 'LEAVINGS', 'LOADINGS', 'LOCATING', 'PLACATED', 'RECEIVED', 'RELATION', 'RENDERED', 'REPORTED', 'REPORTER', 'RESEARCH', 'RESOLVED', 'RETRACTS', 'SHAVINGS', 'SIMPLIFY', 'SIMULATE', 'STEALING', 'STEELING', 'UNSOLVED', 'VALIDATE']

def compare_words(word1, word2):
    """Return the number of letters that match in the same position."""
    matching_letters = 0

    for position in range(len(word1)):
        if word1[position] == word2[position]:
            matching_letters += 1

    return matching_letters


print("Welcome to Password Guesser Deluxe!")
print("By Md Rifat Hasan (10736531)")
print()

# valid difficulty.
while True:
    print("Select a difficulty: [E]asy, [M]edium, [H]ard.")
    difficulty = input("> ").strip().upper()

    if difficulty in ("E", "M", "H"):
        break

    print("Invalid choice! Enter E, M or H.")
    print()

# Set up the game based on dificulty
if difficulty == "E":
    source_list = easy_words
    word_count = 7
    guesses_remaining = 5
    difficulty_name = "Easy"
elif difficulty == "M":
    source_list = medium_words
    word_count = 8
    guesses_remaining = 4
    difficulty_name = "Medium"
else:
    source_list = hard_words
    word_count = 9
    guesses_remaining = 4
    difficulty_name = "Hard"

word_list = random.sample(source_list, word_count)
password = random.choice(word_list)
starting_guesses = guesses_remaining

print(f"{difficulty_name} difficulty selected!")
print()
print(f"You have {guesses_remaining} guesses remaining to identify the password out of {word_count} words.")
print(f"It has {len(password)}-letter words.")
input("Press Enter to begin!")

Win = False

while guesses_remaining > 0 and not Win:
    print()
    print("The password is one of these words:")
    for number, word in enumerate(word_list, start=1):
        print(f"{number}) {word}")

    print()
    print(f"Guesses remaining: {guesses_remaining}")

    # Asking the user about the number.
    while True:
        choice_text = input(f"Guess (enter 1-{len(word_list)}): ").strip()

        if choice_text.isdigit():
            choice_number = int(choice_text)
            if 1 <= choice_number <= len(word_list):
                break

        print("Invalid choice! Enter one of the numbers shown.")

    selected_word = word_list.pop(choice_number - 1)
    guesses_remaining -= 1
    print()
    print(selected_word)

    if selected_word == password:
        print("Password correct.")
        Win = True
    else:
        matching_letters = compare_words(selected_word, password)
        print("Password incorrect.")
        print(f"{matching_letters}/{len(password)} correct.")

print()
if Win:
    if guesses_remaining == starting_guesses - 1:
        print("Lucky guess!")
    print("You win!")
else:
    print("You lose!")
    print(f"The password was {password}.")
