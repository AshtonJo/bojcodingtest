angles = [int(input()) for _ in range(3)]
angle1, angle2, angle3 = angles

if angle1 == 60 and angle2 == 60 and angle3 == 60:
  print("Equilateral")
elif angle1 + angle2 + angle3 == 180 and (angle1 == angle2 or angle1 == angle3 or angle2 == angle3):
  print("Isosceles")
elif angle1 + angle2 + angle3 == 180 and (angle1 != angle2 or angle1 != angle3 or angle2 != angle3):
  print("Scalene")
elif angle1 + angle2 + angle3 != 180:
  print("Error")