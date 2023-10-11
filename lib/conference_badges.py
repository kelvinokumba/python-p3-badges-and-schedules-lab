def badge_maker(name=""):
    return f"Hello, my name is {name}"
badge_maker()

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]


def assign_rooms(names):
    rooms = range(1, len(names) + 1)
    names = []

    for i, speaker in enumerate(names):
        names = f"Hello, {speaker}! You'll be assigned to room {rooms[i]}."
        names.append(names)

    return names

def printer(names):
   # Get badge messages
    badges = batch_badge_creator(names)
    for badge in badges:
        print(badge)

    # Get room assignment messages
    room_assignments = assign_rooms(names)
    for assignment in room_assignments:
        print(assignment)
