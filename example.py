# example usage of the interface
import interface
import common

# first set the variables for logging into your webdkp app
common.url = "https://webdkp.com/dkp/Aegwynn/Dark+Alliance"  # URL for your webdkp page, change to yours
common.username = ""  # your username here
common.password = ""  # your password here
common.clan = "SomeClan"  # example clan, change to yours
common.server = "SomeServer"  # example server, change to yours
common.table_ids = {  # example DKP tables, change to yours
    "DKP": 1,  
    "AKP": 2
}

# login and sync the player data
interface.login()
interface.sync_players()

# do stuff with the DKP
print(interface.force_dkp("Player1", 700, "DKP"))
print(interface.award_dkp(["Player1", "Player2"], "Some Raid", 350, "AKP"))
print(interface.award_item("Player1", "Some Drop", 400, "AKP"))