import PySimpleGUI as sg
import hypixel
import json

API_KEYS = []
hypixel.setKeys(API_KEYS)

layout = [[sg.Text('bedwars stats')],
          [sg.Text('username: '), (sg.InputText())],
          [sg.Button('ok'), sg.Button('cancel')]]

window = sg.Window('uwu', layout).Finalize()

while True:
    event, values = window.read()
    if event in (None, 'cancel'):
        break
    username = str(values[0])
    player = hypixel.Player(username)
    Blitz = player.JSON['stats']['HungerGames']
    BlitzKills = str(Blitz['kills'])
    BlitzWinsSolo = str(Blitz['wins'])
    BlitzWinsTeam = str(Blitz['wins_teams'])
    BlitzCoins = str(Blitz['coins'])
    BlitzChests = str(Blitz['chests_opened'])
    BlitzTaunt = str(Blitz['chosen_taunt'])
    blitz = 'blitz kills: ' + BlitzKills + '\nblitz wins solo: ' + BlitzWinsSolo + '\nblitz wins teams: ' + BlitzWinsTeam + '\nblitz coins: ' + BlitzCoins + '\nblitz chests: ' + BlitzChests + '\nblitz taunt: ' + BlitzTaunt
    print(blitz)

