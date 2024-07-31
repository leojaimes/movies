import csv
import random

# Crear encabezados
header = [
    "id",
    "full",
    "text",
    "favorites",
    "retweets",
    "mentions",
    "country",
    "followers",
]
data = [header]

# Listas de ejemplo para generar datos
full_texts = [
    "Running down the hill",
    "Celebrating today",
    "Reacting to the news",
    "Faking it by Atwell",
    "Welcoming back",
    "Contest winner",
    "Feeling grateful",
    "OnePlus 8 Giveaway",
    "Here it is",
    "Advertising during the year",
    "In love with the game",
    "The best product",
    "Can't believe it",
    "Buy this product",
    "Feeling bad",
    "Not feeling good",
    "Programming is a hot topic",
    "Thanks man",
    "There's nothing better than programming",
    "Feeling bored",
]


# Función para generar menciones
def random_mention():
    return "@user" + str(random.randint(1, 1000))


# Agregar 100 filas de datos con sentido
for i in range(1, 101):
    row = [
        183720 + i,
        random.choice(full_texts),
        "This is a sample tweet text number "
        + str(i)
        + " with more details and context.",
        random.randint(0, 500),
        random.randint(0, 500),
        random_mention(),
        random.choice(["USA", "UK", "Canada", "Germany", "France", "Spain"]),
        random.randint(100, 10000),
    ]
    data.append(row)

# Escribir datos en un archivo CSV
csv_file_path = "meaningful_output.csv"
with open(csv_file_path, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file created at: {csv_file_path}")
