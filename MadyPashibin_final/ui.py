#!/usr/bin/env python3

import db
from objects import Team, Player

# Team Class

def add_team():
    team_name = input("Team name: ").title()
    team_mascot = input("Mascot: ").title()
    conference = input("Conference: ").title()
    wins = int(input("Team wins: "))
    losses = int(input("Team losses: "))
    head_coach = input("Head Coach: ")

    team = Team(None, team_name, team_mascot, conference, wins, losses, head_coach)

    db.add_team(team)
    print(f"{team.teamName} was added.\n")

def remove_team():
    team_name = get_team_name()
    team = db.get_team_by_name(team_name)
    db.delete_team(team)
    if team:
        db.delete_team(team.teamID)
        print(f"{team_name} was deleted.\n")
    else:
        print("Team not found.")

def get_team_name():
    while True:
        team_name = input("Team: ")
        teams = db.get_teams()
        if any(team.teamName == team_name for team in teams):
            return team_name
        else:
            print("Team not found. Please try again.")
            display_teams() 

def display_teams():
    teams = db.get_teams()
    if not teams:
        print("There are currently no teams in the database.")
        return
    for team in teams:
        print(f"{'':1}{'Team Name':<30}{'Mascot':<15}{'Conference':<15}"
              f"{'Wins':<10}{'Losses':<10}{'Head Coach':<20}")
        print("-" * 80)
        print()
        for team in teams:
            print(f"{'':1}{team.teamName:<30}{team.teamMascot:<15}{team.conference:<15}"
          f"{team.wins:<10}{team.losses:<10}{team.headCoach:<20}")
    print()

def display_record():
    teams = db.get_team_records()
    if not teams:
        print("There are currently no teams in the database.")
        return
    else:
        print(f"{'':3}{'Team':25}{'Record':>6}")
        print("-" * 64)
        for team in teams:
            print(f"{team.teamName:30}{team.wins}-{team.losses:}")
    print()

def display_team_information(team_name, db):
    # Get the selected team
    team = db.get_team_by_name(team_name)
    if not team:
        print("No team found with that name: {team_name}")
        return
    else:
        print(f"{team.teamInfo}.")
    print()

# Player Class 

def add_player():
    team_name = get_team_name()
    team = db.get_team_by_name(team_name)
    if not team:
        print("Team not found.")
        return
    
    first_name = input("First name: ").title()
    last_name = input("Last name: ").title()
    number = get_player_number()
    position = get_player_position()
    sets_played = get_sets_played(matches_played)
    matches_played = get_matches_played()
    hit_kills = get_hit_kills(hit_attempts)
    hit_errors = get_hit_errors(hit_attempts)
    hit_attempts = get_hit_attempts()
    assists = get_assists()
    serve_aces = get_serve_aces()
    serve_errors = get_serve_errors()
    digs = get_digs()
    blocks = get_blocks()

    player = Player(None, team.teamID, number, first_name, last_name, position, sets_played, 
                    matches_played, hit_kills, hit_errors, hit_attempts,
                    assists, serve_aces, serve_errors, digs, blocks)
    
    db.add_player(player)
    print(f"{player.fullName} was added.\n")

# Handle inputs for player information for error handling

def get_player_position():
    while True:
        position = input("Position: ").upper()
        if position in POSITIONS:
            return position
        else:
            print("Invalid position. Please try again.")
            display_positions()

def get_sets_played(matches_played):
    while True:
        try:
            sets_played = int(input("Sets played: "))
        except ValueError:
            print("Invalid number. Please try again.")
            continue

        if sets_played < 0 or sets_played > matches_played:        
            print(f"Invalid entry. Must be from 0 to {matches_played}.")
        else:
            return sets_played

def get_matches_played():
    while True:
        try:
            matches_played = int(input("Matches played: "))
        except ValueError:
            print("Invalid number. Please try again.")
            continue

        if matches_played < 0 or matches_played > 100:    
            print("Invalid entry. Must be from 0 to 100.")
        else:
            return matches_played

def get_hit_kills(hit_attempts):
    while True:
        try:
            hit_kills = int(input("Number of kills: "))
        except ValueError:
            print("Invalid number. Please try again.")
            continue

        if hit_kills < 0 or hit_kills > hit_attempts:        
            print(f"Invalid entry. Must be from 0 to {hit_attempts}.")
        else:
            return hit_kills

def get_hit_errors(hit_attempts):
    while True:
        try:
            hit_errors = int(input("Number of hitting errors: "))
        except ValueError:
            print("Invalid number. Please try again.")
            continue

        if hit_errors < 0 or hit_errors > hit_attempts:        
            print(f"Invalid entry. Must be from 0 to {hit_attempts}.")
        else:
            return hit_errors

def get_hit_attempts():
    while True:
        try:
            hit_attempts = int(input("Number of hitting attempts: "))
        except ValueError:
            print("Invalid number. Please try again.")
            continue

        if hit_attempts < 0 or hit_attempts > 10000:        
            print(f"Invalid entry. Must be from 0 to 10,000.")
        else:
            return hit_attempts

def get_assists():
    while True:
        try:
            assists = int(input("Number of assists: "))
        except ValueError:
            print("Invalid number. Please try again.")
            continue

        if assists < 0 or assists > 10000:        
            print(f"Invalid entry. Must be from 0 to 10,000.")
        else:
            return assists

def get_serve_aces():
    while True:
        try:
            serve_aces = int(input("Number of serving aces: "))
        except ValueError:
            print("Invalid number. Please try again.")
            continue

        if serve_aces < 0 or serve_aces > 1000:        
            print(f"Invalid entry. Must be from 0 to 1,000.")
        else:
            return serve_aces

def get_serve_errors():
    while True:
        try:
            serve_errors = int(input("Number of serving errors: "))
        except ValueError:
            print("Invalid number. Please try again.")
            continue

        if serve_errors < 0 or serve_errors > 1000:        
            print(f"Invalid entry. Must be from 0 to 1,000.")
        else:
            return serve_errors

def get_digs():
    while True:
        try:
            digs = int(input("Number of digs: "))
        except ValueError:
            print("Invalid number. Please try again.")
            continue

        if digs < 0 or digs > 10000:        
            print(f"Invalid entry. Must be from 0 to 10,000.")
        else:
            return digs

def get_blocks():
    while True:
        try:
            blocks = int(input("Number of blocks: "))
        except ValueError:
            print("Invalid number. Please try again.")
            continue

        if blocks < 0 or blocks > 1000:        
            print(f"Invalid entry. Must be from 0 to 1,000.")
        else:
            return blocks

def get_player_number(players, prompt):
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("Invalid number. Please try again.")
            continue

        if number < 1 or number > 100:
            print("Invalid player number. Please try again.")
        else:
            return number

def remove_player():
    last_name = input("Enter the last name of the player to remove: ")
    players = [p for p in db.get_players() if p.lastName == last_name]
    if not players:
        print("No players found.")
        return
    else:
        db.delete_player(players[last_name].playerID)
        print(f"{player.fullName} was deleted.\n")

def edit_player_stats():
    last_name = input("Enter the last name of the player to edit: ")
    players = [p for p in get_players() if p.lastName == last_name]
    if not players:
        print("No players found.")
        return

    player = players[last_name]
    print(f"You selected {player.fullName} to edit.")
    
    player.setsPlayed = get_sets_played(player.matchesPlayed)
    player.matchesPlayed = get_matches_played()
    player.hitKills = get_hit_kills(player.hitAttempts)
    player.hitErrors = get_hit_errors(player.hitAttempts)
    player.hitAttempts = get_hit_attempts()
    player.assists = get_assists()
    player.serveAces = get_serve_aces()
    player.serveErrors = get_serve_errors()
    player.digs = get_digs()
    player.blocks = get_blocks()
    
    db.update_player_stats(player)
    print(f"{player.fullName} was updated.\n")

def display_stats():
    players = db.get_players()
    if not players:
        print("There are currently no players in the database.")
        return
 
    print("D = Digs, B = Blocks,K = Kills, HE = Hitting Errors, HA = Hitting Attempts, SE = Serving Errors\n\n")
    print(f"{'Player':20}{'Pos':>3}{'K':>6}{'HE':>6}"
          f"{'HA':>6}{'Hitting Avg':>15}{'Aces':>8}"
          f"{'SE':>6}{'D':>8}{'D/S':>6}{'B':>6}"
          f"{'B/S':>6}{'Points/Set':>12}")
    print("-" * 80)
        
    for player in players:
        print(f"{player.fullName:20}{player.position:6}{player.hitKills:3}"
              f"{player.hitErrors:6}{player.hitAttempts:6}{player.hittingAvg:10}"
              f"{player.serveAces:12}{player.serveErrors:6}{player.digs:8}"
              f"{player.digsPerSet:8}{player.blocks:6}{player.assistsPerSet:6}"
              f"{player.pointsPerSet:10}")
    print()

def display_all_players():
    players = db.get_players()
    if not players:
        print("There are currently no players in the database.")
        return

    print(f"{'Number':<20}{'Player':<30}{'Position':<10}{'Points Per Set':<15}")
    print("-" * 80)
    
    for player in players:
        print(f"{player.number:<20}{player.fullName:<30}{player.position:<10}{player.pointsPerSet:<10}")

    print()

# Roster functionality

def display_team_roster():
    team_name = input("Enter the team name: ")
    team = db.get_team_by_name(team_name)
    if not team:
        print("Team not found.")
        return
    
    roster = db.get_team_roster(team.teamID)
    print(f"                     Roster for {team.teamName}:")
    print(f"{'':3}{'Number':<6}{'Player':<30}{'Position':<10}{'Matches Played':>14}"
          f"{'Sets Played':>14}{'Points Per Set':>15}")
    print("-" * 80)
    
    for player in roster:
        print(f"{player.number:<3}{player.fullName():<30}{player.position:<10}"
              f"{player.matchesPlayed:>14}{player.setsPlayed:>14}{player.pointsPerSet:>15}")
        
    print() 

# User Interface

POSITIONS = ("L", "S", "OH", "MH", "RH")

def display_separator():
    print("=" * 64)

def display_title():
    print("                   Division III Women's Volleyball")

def display_main_menu():
    print("MENU OPTIONS")
    print("A – Team Information")
    print("B – Player Information")
    print("C - Exit Program")
    print()

def display_team_menu():
    print("TEAM MENU OPTIONS")
    print("1 – Display teams")
    print("2 - Display team information")
    print("3 – Display team roster")
    print("4 - Display overall record")
    print("5 - Add team")
    print("6 - Remove team")
    print("7 - Back to main menu")
    print("8 - Exit program")
    print()

def display_player_menu():
    print("PLAYER MENU OPTIONS")
    print("1 – Display team roster")
    print("2 – Display all players")
    print("3 - Display positions")
    print("4 - Display player stats")
    print("5 – Add player to team")
    print("6 – Remove player from team")
    print("7 – Edit player stats")
    print("8 - Back to main menu")
    print("9 - Exit program")
    print()

def display_positions():
    print("POSITIONS")
    print(", ".join(POSITIONS))
    print("L: Libero, S: Setter, OH: Outside Hitter, MH: Middle Hitter, RH: Rightside Hitter")

def main():

    # Connect to database
    db.connect()
    teams = db.get_teams()
    players = db.get_players()         
    
    while True:
        
        # Display main menu
        display_separator()
        display_title()
        display_separator()
        
        display_main_menu()
        try:
            main_option = input("Menu option: ").upper()
        except ValueError:
            main_option = "INVALID"

        if main_option == "A":
            operate_team_menu()
        elif main_option == "B":
            operate_player_menu()
        elif main_option == "C":
            print("Goodbye!")
            break
        else:
            print("Invalid menu option. Please try again.\n")

    # Close the database
    db.close()

# Team Menu

def operate_team_menu():

    while True:
        display_separator()
        display_team_menu()
        
        team_option = int(input("Team menu option: "))
        
        if team_option == 1:
            display_teams(teams)
        elif team_option == 2:
            team_name = input("Enter team name: ")
            display_team_information(team_name, db)
        elif team_option == 3:
            display_team_roster()
        elif team_option == 4:
            display_record()
        elif team_option == 5:
            add_team()
        elif team_option == 6:
            remove_team()
        elif team_option == 7:
            break
        elif team_option == 8:
            exit_program()
        else:
            print("Not a valid option. Please try again.\n")
            display_team_menu()
            
 # Player Menu

def operate_player_menu():

     while True:

        display_separator()
        display_player_menu()
        
        player_option = int(input("Player menu option: "))

        if player_option == 1:
            display_team_roster()
        elif player_option == 2:
            display_all_players()  
        elif player_option == 3:
            display_positions()
        elif player_option == 4:
            display_stats()
        elif player_option == 5:
            add_player()
        elif player_option == 6:
            remove_player()
        elif player_option == 7:
            edit_player_stats()
        elif player_option == 8:
            break
        elif player_option == 9:
            exit_program()
        else:
            print("Not a valid option. Please try again.\n")
            display_player_menu()

# Exit Program

def exit_program():
    db.close()
    print("Goodbye and go Blugolds!")
    exit()

if __name__ == "__main__":
    main()
