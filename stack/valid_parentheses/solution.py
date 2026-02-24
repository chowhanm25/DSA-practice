class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determines whether the input string of brackets is valid.

        A string is valid if:
        1. Open brackets are closed by the same type.
        2. Open brackets are closed in correct order.
        3. Every closing bracket has a corresponding opening bracket.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        # Stack to store opening brackets
        stack = []

        # Mapping of closing bracket -> corresponding opening bracket
        closeToOpen = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        # Traverse each character in string
        for c in s:

            # If current character is a closing bracket
            if c in closeToOpen:

                # Check:
                # 1. Stack must not be empty
                # 2. Top of stack must match corresponding opening bracket
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()   # Valid match → remove opening bracket
                else:
                    return False  # Invalid case

            else:
                # If opening bracket → push into stack
                stack.append(c)

        # If stack is empty → all brackets matched correctly
        return not stack
