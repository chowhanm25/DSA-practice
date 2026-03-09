class FreqStack(object):

    def __init__(self):
        # value -> frequency
        self.freq = {}

        # frequency -> stack of values
        self.group = {}

        # current maximum frequency
        self.maxFreq = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """

        # Increase frequency of value
        self.freq[val] = self.freq.get(val, 0) + 1
        f = self.freq[val]

        # Update maximum frequency
        if f > self.maxFreq:
            self.maxFreq = f

        # Create stack for this frequency if it doesn't exist
        if f not in self.group:
            self.group[f] = []

        # Push value into corresponding frequency stack
        self.group[f].append(val)

    def pop(self):
        """
        :rtype: int
        """

        # Pop the most frequent element
        val = self.group[self.maxFreq].pop()

        # Decrease its frequency
        self.freq[val] -= 1

        # If no more elements at this frequency, reduce maxFreq
        if not self.group[self.maxFreq]:
            self.maxFreq -= 1

        return val
