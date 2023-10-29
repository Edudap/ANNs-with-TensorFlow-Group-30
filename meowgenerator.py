def meow_generator():
    count = 1
    while True:
     yield " ".join(["Meow"]*count)
     count *= 2

Meows = meow_generator()
print(next(Meows))
print(next(Meows))
print(next(Meows))
print(next(Meows))