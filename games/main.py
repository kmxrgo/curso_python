'''
Archivo principal del juego Games
'''
from Athlete import Athlete
from Sport import Sport
from Team import Team
from Game import Game
import json

def main(archivo_torneo:str):
    '''
    Funcion principal del juego
    '''
    if archivo_torneo != "":
        with open(archivo_torneo, "r") as file:
            torneo = json.load(file)
    else:
        players_mexico = ['Chicharito', 'Piojo', 'Chucky', 'Tecatito', 'Gullit', 'Ochoa', 'Guardado', 'Herrera', 'Layun', 'Moreno', 'Araujo']
        players_espania = ['Casillas', 'Ramos', 'Pique', 'Alba', 'Iniesta', 'Silva', 'Isco', 'Busquets', 'Costa', 'Morata', 'Asensio']
        players_brasil = ['Neymar', 'Coutinho', 'Marcelo', 'Casemiro', 'Alisson', 'Jesus', 'Paulinho', 'Thiago', 'Silva', 'Firmino', 'Danilo']
        players_argetina = ['Messi', 'Aguero', 'Di Maria', 'Mascherano', 'Higuain', 'Dybala', 'Otamendi', 'Romero', 'Rojo', 'Banega', 'Fazio']
        lista_mexico = [Athlete(x) for x in players_mexico]
        lista_espania = [Athlete(x) for x in players_espania]
        lista_brasil = [Athlete(x) for x in players_brasil]
        lista_argetina = [Athlete(x) for x in players_argetina]
        soccer = Sport("Soccer", 11, "FIFA")
        mexico = Team("Mexico", soccer, lista_mexico)
        espania = Team("Espania", soccer, lista_espania)
        brasil = Team("Brasil", soccer, lista_brasil)
        argentina = Team("Argentina", soccer, lista_argetina)
        equipos = [mexico, espania, brasil, argentina]
        d = {}
        for local in equipos:
            for visitante in equipos:
                if local != visitante:
                    juego = Game(local, visitante)
                    d[juego.to_json()[A]['name']] = juego.to_json()
        torneo = list(d.values())
        # juego = Game(mexico, espania)
        # torneo = [juego.to_json()]
        archivo_torneo = "torneo.json"
        with open(archivo_torneo, "w", encoding='utf-8') as f:
            json.dump(torneo, f, ensure_ascii=False, indent=4)
        print(f"Se escribió el archivo {archivo_torneo} con un torneo de {len(torneo)} juego(s)")
    # Jugar todos los juegos del torneo
    for juego in torneo:
        A = Team(juego["A"]["name"], Sport(juego["A"]["sport"]["name"], juego["A"]["sport"]["players"], juego["A"]["sport"]["league"]), [Athlete(x["name"]) for x in juego["A"]["players"]])
        B = Team(juego["B"]["name"], Sport(juego["B"]["sport"]["name"], juego["B"]["sport"]["players"], juego["B"]["sport"]["league"]), [Athlete(x["name"]) for x in juego["B"]["players"]])
        game = Game(A, B)
        game.play()
        print(game)
        print("----------------")

if __name__ == "__main__":
    archivo_torneo = ""
    main(archivo_torneo)
