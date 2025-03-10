import random
num_points = 100000
points_inside_circle = 0 # 初始化点在圆内的数量
for _ in range(num_points):
    x = random.random()
    y = random.random()
    if x ** 2 + y ** 2 <= 1:
        points_inside_circle += 1

pi_estimate = 4 * points_inside_circle / num_points
print(f"Estimated value of pi after {num_points} throws: {pi_estimate}")