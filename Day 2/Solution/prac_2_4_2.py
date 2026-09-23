hp = int(input("Enter the HP: "))
defence = int(input("Enter the Defence: "))
attack = int(input("Enter the Attack: "))
speed = int(input("Enter the Speed: "))
accuracy = int(input("Enter the Accuracy: "))

if (hp > 1000 and defence > 500) or attack < 500:
    print("This is a defence monster")
elif attack > 1000 and speed > 250 and accuracy == 0:
    print("This is a cleave monster")
elif hp < 500 or accuracy > 50 or attack < 1000:
    print("This is a glass cannon monster")
else:
    print("This is a normal monster")