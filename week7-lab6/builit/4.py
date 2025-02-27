from time import sleep

num = int(input("Write the number: "))
sec = int(input("Write the milliseconds: "))

sleep(sec/1000)

print(f"Square root of {num} after {sec} miliseconds is {num**0.5}")