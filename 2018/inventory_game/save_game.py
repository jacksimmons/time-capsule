import pickle

def save(obj):
    #ref: https://stackoverflow.com/questions/13906623/using-pickle-dump-typeerror-must-be-str-not-bytes
    with open("save.pkl", "wb") as file:
        pickle.dump(obj, file)

def load() -> object:
    with open("save.pkl", "rb") as file:
        return pickle.load(file)