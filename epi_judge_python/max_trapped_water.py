from test_framework import generic_test


def get_max_trapped_water(heights):
    return my_solution(heights)


# Avg runtime 219 us; Median runtime 22 us
def my_solution(heights):
    max_area = 0
    left, right = 0, len(heights) - 1

    while left < right:
        min_height = min(heights[left], heights[right])
        width = right - left
        area = min_height * width
        max_area = max(area, max_area)

        if heights[left] <= heights[right]:
            left += 1
        else:
            right -= 1

    return max_area


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_trapped_water.py",
                                       "max_trapped_water.tsv",
                                       get_max_trapped_water))
