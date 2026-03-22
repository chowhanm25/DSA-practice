def minEatingSpeed(piles, h):
    left, right = 1, max(piles)
    result = right

    while left <= right:
        k = (left + right) // 2
        
        total_hours = 0
        for pile in piles:
            total_hours += (pile + k - 1) // k

        if total_hours <= h:
            result = k
            right = k - 1
        else:
            left = k + 1

    return result

# Example usage
if __name__ == "__main__":
    print(minEatingSpeed([3,6,7,11], 8))        # Output: 4
    print(minEatingSpeed([30,11,23,4,20], 5))   # Output: 30
    print(minEatingSpeed([30,11,23,4,20], 6))   # Output: 23
