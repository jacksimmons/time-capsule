from defaults import default_input

class Inventory():
    def __init__(self, items: list=[]):
        self.items = items

    def get_items(self):
        items = ""
        for item in self.items:
            items += "\t" + item.name + "\n"
        return items[:-1] # Remove the last newline
    
    def add_item(self, item):
        self.items.append(item)
    
    def use_item(self, item, stats: dict):
        print(stats["name"] + " used a " + item.name + "!")
        default_input()
        index = self.items.index(item)
        stats = item.use(stats)
        self.items.pop(index)
        return stats
    
class Item():
    def __init__(self, name):
        self.name = name

class AdditiveItem(Item):
    def __init__(self, name, mapping: dict):
        super().__init__(name)
        self.add_map = mapping
    
    def use(self, stats: dict):
        for key in stats.keys():
            if (key in self.add_map):
                stats[key] += self.add_map[key]
                if (key == "hp"):
                    print("Restored " + str(self.add_map["hp"]) + " HP.")
                else:
                    print("Added " + str(self.add_map[key]) + key.upper())
        
        if (stats["hp"] >= stats["max_hp"]):
            print("Fully restored HP!")
            stats["hp"] = stats["max_hp"]
        return stats

class MultiplicativeItem(Item):
    def __init__(self, name, mapping: dict):
        super().__init__(name)
        self.mult_map = mapping
    
    def use(self, stats: dict):
        for key in stats.keys():
            stats[key] *= self.mult_map[key]
            print("Added a " + str(self.mult_map[key]) + "x modifier to " + key.upper() + ".")
        
        if (stats["hp"] >= stats["max_hp"]):
            print("Fully restored HP!")
            stats["hp"] = stats["max_hp"]
        return stats

class PenguinBar(AdditiveItem):
    def __init__(self):
        super().__init__("PenguinBar", {"hp": 5})

class YazooMilk(AdditiveItem):
    def __init__(self):
        super().__init__("YazooMilk", {"hp": 10})
