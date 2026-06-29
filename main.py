#Basketball Projekat

roster = {
    "15":{
        "Name of the Player": "Nikola Jokic",
        "Position": "Center",
        "PPG": 29.6,
        "Recent fouls": 4,
        "Injured": False,
        "Starter": True
    },

    "27":{
        "Name of the Player": "Jamal Murray",
        "Position": "Point Guard",
        "PPG": 21.4,
        "Recent fouls": 2,
        "Injured": True,
        "Starter": True
    },

    "0":{
        "Name of the Player": "Christian Braun",
        "Position": "Shooting Guard",
        "PPG": 15.4,
        "Recent fouls": 4,
        "Injured": False,
        "Starter": True
    },

    "32":{
        "Name of the Player": "Aron Gordon",
        "Position": "Power Forward",
        "PPG": 14.7,
        "Recent fouls": 3,
        "Injured": False,
        "Starter": True
    },

    "10":{
        "Name of the Player": "Tim Hardaway Jr.",
        "Position": "Shooting Guard",
        "PPG": 11.0,
        "Recent fouls": 5,
        "Injured": False,
        "Starter": True
    },

    "17":{
        "Name of the Player": "Jonas Valanciunas",
        "Position": "Center",
        "PPG": 10.4,
        "Recent fouls": 5,
        "Injured": False,
        "Starter": False
    },

    "3":{
        "Name of the Player": "Julian Strawther",
        "Position": "Shooting Guard",
        "PPG": 9.9,
        "Recent fouls": 1,
        "Injured": False,
        "Starter": False
    },

    "11":{
        "Name of the Player": "Bruce Brown",
        "Position": "Shooting Guard",
        "PPG": 8.3,
        "Recent fouls": 3,
        "Injured": False,
        "Starter": False
    },

    "5":{
        "Name of the Player": "Peyton Wtson",
        "Position": "Power Forward",
        "PPG": 8.1,
        "Recent fouls": 0,
        "Injured": False,
        "Starter": False
    },

    "22":{
        "Name of the Player": "Zeke Nnaji",
        "Position": "Center",
        "PPG": 3.6,
        "Recent fouls": 0,
        "Injured": False,
        "Starter": False
    },

    "24":{
        "Name of the Player": "Jalen Pickett",
        "Position": "Point Guard",
        "PPG": 3.2,
        "Recent fouls": 0,
        "Injured": False,
        "Starter": False
    },

}

karton = []
ukupno_poena = 0


print("=== IZVEŠTAJ ZA TRENERSKI TIM: ŽIVI SASTAV ===")
print(f"{'Dres':<6}| {'Ime igrača':<24}| {'Poz.':<15}| {'PPG':<6}| Status")
print("-------------------------------------------------------------------------")

for jersey, statistika in roster.items():
    if statistika['Injured']:
        status = "POVREDJEN"
    elif statistika['Recent fouls'] >= 6:
        status = "ISKLJUCEN 6F"
        karton.append(jersey)
    elif statistika['Recent fouls'] == 5:
        status = "OPASNOST 5F"
        karton.append(jersey)
    else:
        status = "DOSTUPAN"
    ukupno_poena += int(statistika['PPG'])

    if statistika['Starter']:
        print(f"#{jersey:<4}| "
              f"{statistika['Name of the Player']:<25}| "
              f"{statistika['Position']:<15}| "
              f"{statistika['PPG']:<6}| "
              f"{status}")
print("-------------------------------------------------------------------------")
print("\n")

print("=== IZVESTAJ ===")
print("-------------------------------------------------------------------------")

if len(karton) > 0:
    print("UPOZORENJE")
    print("TRENERU: Prilagodi rotaciju!")
    for player in karton:
        print(player)
else:
    print("Nema igraca u problemu sa faulovima.")
print("-------------------------------------------------------------------------")
prosek = ukupno_poena/len(roster)
final_res = round(prosek, 1)

print(f"Prosek poena cele ekipe: {final_res}")