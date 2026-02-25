from pyscript import document

players = [
    "1) Escudero",
    "2) Estrada",
    "3) Tolentino",
    "4) Pimentel",
    "5) Binay",
    "6) Cayetano",
    "7) Dela Rosa",
    "8) Ejercito",
    "9) Gatchalian",
    "10) Go",
    "11) Hontiveros",
    "12) Ko",
    "13) Legarda",
    "14) Marcos",
    "15) Padilla",
    "16) Poe",
    "17) Revilla",
    "18) Tulfo",
    "19) Villanueva",
    "20) Villar"
]

def show_players(event):
    output = document.getElementById("player-list")
    output.innerHTML = "<br>".join(players)
