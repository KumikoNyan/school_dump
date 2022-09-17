# Simple coin change program

user_input = int(input("Centavos: "))
print("5-peso coin/s: " + str(user_input // 500))
user_input = user_input % 500
print("1-peso coin/s: " + str(user_input // 100))
user_input = user_input % 100
print("25-centavo coin/s: " + str(user_input // 25))
user_input = user_input % 25
print("10-centavo coin/s: " + str(user_input // 10))
user_input = user_input % 10
print("5-centavo coin/s: " + str(user_input // 5))
user_input = user_input % 5
print("1-centavo coin/s: " + str(user_input // 1))
user_input = user_input % 1