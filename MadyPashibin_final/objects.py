#!/usr/bin/env python3

from dataclasses import dataclass

@dataclass
class Team:
    teamID:int = 0
    teamName:str = ""
    teamMascot:str = ""
    conference:str = ""
    wins:int = 0
    losses:int = 0
    headCoach:str = ""

    @property
    def teamInfo(self):
        return (f"{self.teamName} are known as the {self.teamMascot} "
                f"and are in the {self.conference} conference. Their "
                f"head coach is {self.headCoach}.")
    
@dataclass         
class Player:
    playerID:int = 0
    teamID: int = 0
    number:int = 0
    firstName:str = ""
    lastName:str = ""
    position:str = ""
    setsPlayed:int = 0
    matchesPlayed:int = 0
    hitKills:int = 0
    hitAttempts:int = 0
    hitErrors:int = 0
    assists:int = 0
    serveAces:int = 0
    serveErrors:int = 0
    digs:int = 0
    blocks:int = 0

    @property
    def fullName(self):
        return f"{self.firstName} {self.lastName}"

    @property
    def hittingAvg(self):
        try:
            avg = (self.hitKills - self.hitErrors) / self.hitAttempts
            return round(avg, 3)
        except ZeroDivisionError:
            return 0.0

    @property
    def assistsPerSet(self):
        try:
            avg = self.assists / self.setsPlayed
            return round(avg, 2)
        except ZeroDivisionError:
            return 0.0

    @property
    def digsPerSet(self):
        try:
            avg = self.digs / self.setsPlayed
            return round(avg, 2)
        except ZeroDivisionError:
            return 0.0

    @property
    def pointsPerSet(self):
        try:
            avg = (self.hitKills + self.serveAces + self.blocks) / self.setsPlayed
            return round(avg, 2)
        except ZeroDivisionError:
            return 0.0
            
def main():
    pass

# if started as the main module, call the main function
if __name__ == "__main__":
    main()
