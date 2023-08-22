voted = {}


def check_voter(tom):
    if voted.get(tom):
        print("kick them out!")
    else:
        voted[tom] = True
        print("let them vote!")