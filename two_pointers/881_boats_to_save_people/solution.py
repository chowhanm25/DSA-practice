class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        i, j = 0, len(people) - 1
        boats = 0

        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1  # pair lightest with heaviest
            j -= 1      # heaviest person goes on boat
            boats += 1  # count this boat

        return boats

