def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    max_area = 0
    left, right = 0, len(height) - 1
    while (left < right):
        left_val, right_val = height[left], height[right]
        area = min(left_val,right_val) * (right - left)
        max_area = max(max_area, area)
        if left_val < right_val:
            left += 1
        else:
            right -= 1
    return max_area



if __name__ == "__main__":
    tests = [[1,8,6,2,5,4,8,3,7],
             [1,1]]
    for test in tests:
        print(maxArea(test))

