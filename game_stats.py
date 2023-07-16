class GameStats():
    def __init__(self,setti):
        self.setti = setti
        self.reset_stats()
        self.active_status = True
    def reset_stats(self):
        self.ships_left = self.setti.ship_limit 