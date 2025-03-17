import math

def are_antipodal(points):
    angles = sorted(math.atan2(y, x) for x, y in points)

    n = len(angles)
    for i in range(n):
        target = angles[i] + math.pi
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2
            if abs(angles[mid] - target) < 1e-9:
                return True
            elif angles[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
    return False

points = [(1, 0), (-1, 0), (0, 1), (0, -1)]
print(f'Are antipodal: {are_antipodal(points)}')