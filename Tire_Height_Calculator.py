# Tire Height Calculator
# New Header
def tire_height(width, height, rim):
    th = (((width/25.4) * height * 2) + rim)
    print(th)

tire_height(275, .40, 22)