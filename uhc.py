import hypixel
API_KEYS = ['']
hypixel.setKeys(API_KEYS)

Username = input('Enter Username: ')
player = hypixel.Player(Username)
UHCStats = player.JSON['stats']['UHC']
UHCKills = UHCStats['kills']
UHCWins =  UHCStats['wins']
UHCScore = UHCStats['score']
UHCCoins = UHCStats['coins']
UHCDeaths = UHCStats['deaths']
UHCKills = str(UHCKills)
UHCWins = str(UHCWins)
UHCScore = str(UHCScore)
UHCCoins = str(UHCCoins)
UHCDeaths = str(UHCDeaths)
UHC_Stats = Username + "'s UHC Stats: \n" + 'Kills: ' + UHCKills + '\n' + 'Wins: ' + UHCWins + '\n' + 'Score: ' + UHCScore + '\n' + 'Coins: ' + UHCCoins + '\n' + 'Deaths: ' + UHCDeaths + '\n\n'
print(UHC_Stats)
file1 = 'uhcstats.txt'
with open(file1, 'a') as file_object:
    file_object.write(UHC_Stats)
"""file_object.write("bw wins: {}".format(BwStats['wins_bedwars']))"""
