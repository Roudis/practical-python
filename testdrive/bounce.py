height = 100
bounce = height * 3/5
bounces = 1

while bounces <= 10 :
    print(bounces, bounce * height )
    bounces = bounces + 1
    height = height * 3/5

print('Number of bounces', bounces)

