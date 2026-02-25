from pyscript import document

players = [
    "Escudero",
    "Estrada",
    "Tolentino",
    "Pimentel",
    "Binay",
    "Cayetano",
    "Dela Rosa",
    "Ejercito",
    "Gatchalian",
    "Go",
    "Hontiveros",
    "Ko",
    "Legarda",
    "Marcos",
    "Padilla",
    "Poe",
    "Revilla",
    "Tulfo",
    "Villanueva",
    "Villar"
]

def show_players(event):
    output = document.getElementById("player-list")
    
    output.innerHTML = "" 
    
    for i in range(len(players)):
        output.innerHTML += f"{i+1}) {players[i]}<br>"
