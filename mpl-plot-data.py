import matplotlib.pyplot as plt

person = ["Christian", "Jayvee", "Edriane", "Khian", "Avian"]
intake = [6, 7, 5, 4, 8]

plt.title("Amount of water intake (person) in cups")
plt.xlabel("Person")
plt.ylabel("Cups of Water")
plt.bar(person, intake)
# plt.grid(True)
plt.show()