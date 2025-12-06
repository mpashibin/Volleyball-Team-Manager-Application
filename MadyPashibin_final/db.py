#!/usr/bin/env python3

import sqlite3
from contextlib import closing
from objects import Team, Player

# Database functionalities

conn = None

def connect():
    global conn
    if not conn:
        DB_FILE = "volleyball_db.sqlite"
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row

def close():
    if conn:
        conn.close()

# Team Class

def make_team(row):
    return Team(row["teamID"], row["teamName"], row["teamMascot"], row["conference"], 
                row["wins"], row["losses"], row["headCoach"])


def get_teams():    
    query = '''SELECT teamID, teamName, teamMascot, conference,
                      wins, losses, headCoach
               FROM Team ORDER BY teamName'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

    teams = []
    for row in results:
        team = make_team(row)
        teams.append(team)
    return teams

def get_team_by_name(team_name):
    query = '''SELECT teamID, teamName, teamMascot, conference,
                      wins, losses, headCoach
               FROM Team
               WHERE teamName = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (team_name,))
        row = c.fetchone()
        if row:
            team = make_team(row)
            return team
        else:
            return None

def add_team(team):
    query = '''INSERT INTO Team (teamName, teamMascot, conference, wins, losses, headCoach) 
             VALUES (?, ?, ?, ?, ?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(query, (team.teamName, team.teamMascot, team.conference,
                          team.wins, team.losses, team.headCoach))
        conn.commit()

def delete_team(team):
    query = '''DELETE FROM Team WHERE teamID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (team.teamID,))
        conn.commit()

def get_team_records():
    query = '''SELECT teamName, wins, losses
               FROM Team
               ORDER BY wins DESC'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        rows = c.fetchall()
        return rows

def get_team_roster(team_id):
    query = '''SELECT playerID, teamID, number, firstName, lastName, position, 
                      setsPlayed, matchesPlayed, hitKills, hitAttempts, hitErrors, assists, 
                      serveAces, serveErrors, digs, blocks
               FROM Player WHERE teamID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (team_id,))
        results = c.fetchall()

    players = []
    for row in results:
        player = make_player(row)
        players.append(player)
    return players
        
# Player Class

def make_player(row):
    return Player(row["playerID"], row["teamID"], row["number"], row["firstName"], 
                  row["lastName"], row["position"], row["setsPlayed"], row["matchesPlayed"], 
                  row["hitKills"], row["hitAttempts"], row["hitErrors"], row["assists"], 
                  row["serveAces"], row["serveErrors"], row["digs"], row["blocks"])

def get_players():    
    query = '''SELECT playerID, teamID, number, firstName, lastName,
                      position, setsPlayed, matchesPlayed, hitKills,
                      hitAttempts, hitErrors, assists, serveAces,
                      serveErrors, digs, blocks
               FROM Player ORDER BY number'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

    players = []
    for row in results:
        player = make_player(row)
        players.append(player)
    return players

def add_player(player):
    query = '''INSERT INTO Player (teamID, number, firstName, lastName,
                                 position, setsPlayed, matchesPlayed, hitKills,
                                 hitAttempts, hitErrors, assists, serveAces,
                                 serveErrors, digs, blocks) 
             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(query, (player.teamID, player.number, player.firstName,
                        player.lastName, player.position, player.setsPlayed,
                        player.matchesPlayed, player.hitKills, player.hitAttempts,
                        player.hitErrors, player.assists, player.serveAces,
                        player.serveErrors, player.digs, player.blocks))
        conn.commit()

def delete_player(player):
    query = '''DELETE FROM Player WHERE playerID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (player.playerID,))
        conn.commit()    

def update_player_stats(player):
    query = '''UPDATE Player
             SET setsPlayed = ?,
                 matchesPlayed = ?,
                 hitKills = ?,
                 hitAttempts = ?,
                 hitErrors = ?,
                 assists = ?,
                 serveAces = ?,
                 serveErrors = ?,
                 digs = ?,
                 blocks = ?
             WHERE playerID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (player.setsPlayed, player.matchesPlayed, player.hitKills,
                          player.hitAttempts, player.hitErrors, player.assists,
                          player.serveAces, player.serveErrors, player.digs,
                          player.blocks, player.playerID))
        conn.commit()

# Main

def main():
    pass

if __name__ == "__main__":
    main()
