from character import Character

class Manager():
    def __init__(self):
        self.characters = []

    def add_character(self, n, a, i, d):
        nuevo = Character(n, a, i, d)
        self.characters.append(nuevo)
        return True

    def delete_character(self, n):
        for i in self.characters:
            if i.name == n:
                tmp = i.getCharacter()
                self.characters.remove(tmp)
                return True
        return False

    def get_characters(self):
        json = []
        for k in self.characters:
            personaje = {
                'name': k.name,
                'anime': k.anime,
                'desc': k.desc,
                'image': k.image
            }
            json.append(personaje)
        return json

