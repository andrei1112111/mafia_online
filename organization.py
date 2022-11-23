class Organizer:
    def __init__(self):
        self.clients = []

    def new_client(self) -> dict:
        """make new client id and return it"""
        k = str(len(self.clients))
        self.clients.append(k)
        return {
            "id": k
        }

    def situation(self) -> dict:
        """return game situation (technical side)"""
        return {
            "players_count": str(len(self.clients))
        }
