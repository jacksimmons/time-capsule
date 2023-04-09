# This file does all of the behind the scenes BMG manipulation
# Encodes the config file into BMG, then replaces the BMG in all Scene/UI files
# Updates the distribution with LE-CODE

# Limitations:
# CT-CODE (not LE-CODE yet)
# Automatic course adding
# TPL manipulation

import os
import sys
from PIL import Image

# INITIALISATION
def create_files():
    f = open("Common.txt", "w")
    f.close()
    f = open("tracks.bmg.txt", "w")
    f.close()

# BMG FRANKENSTEINING
def config_to_tracks():
    os.system("wctct bmg --le-code --long config.txt >tracks.bmg.txt")

def get_tracks():
    f = open("tracks.bmg.txt", "r")
    lines = f.readlines() # 6600 - 714b, but 7000 - 7041 need replacing
    # (7000-7041 = line 77 - 142 after first 5 lines have been removed)
    f.close()
    return lines

def get_restored_track_names():
    f = open("defaults/restore_track_names.txt", "r")
    lines = f.readlines()
    f.close()
    return lines

def restore_track_names():
    tracks = get_tracks()[5:]
    restored_track_names = get_restored_track_names()

    for i, x in enumerate(tracks):
        if 76 <= i <= 141:
            # Lines 77 - 142 (7000-7041BMG)
            tracks[i] = restored_track_names[i - 76] # 0 <= i - 76 <= 65
        if i == 141:
            tracks[i] += "\n"

    f = open("tracks.bmg.txt", "w")
    f.writelines(tracks)
    f.close()

def get_common():
    f = open("defaults/Common.txt", "r")
    lines = f.readlines()
    f.close()

    f = open("Common.txt", "w")
    f.writelines(lines)
    f.close()
    return lines

def patch_ui_common():
    tracks = get_tracks()[76:] # Restore the tracks BEFORE this procedure
    common = get_common()[:254]

    for track in tracks:
        common.append(track)

    f = open("Common.txt", "w")
    f.writelines(common)
    f.close()

    os.system("wszst patch --le-menu ./files/Scene/UI/*_U.szs --patch-bmg replace=Common.txt -o")

def patch_ui_tpl():
    # Export images into /img
    os.system("wimgt decode ./ct_icons.tpl -d img/ --number")
    
    images = list()
    height = 0
    width = 128

    sorted_files = sorted(os.listdir(os.path.join(os.getcwd(), "img")))
    for file in sorted_files:
        im = Image.open(os.path.join(os.getcwd(), "img", file))
        images.append(im)
        height += im.height
    
    combined = Image.new('RGB', (width, height))
    i = 0
    for im in images:
        combined.paste(im, (0, im.height * i))
        i += 1

    print(os.path.join(os.getcwd(), "image.png"))
    combined.save(os.path.join(os.getcwd(), "image.png"))

# COURSE COMMON EXTRACTING (long)
def course_extract_common():
    os.system("wszst xcommon ./files/Race/Course/*.szs -qiod ./files/Race/Common")

# LE-CODE TAMPERING
def update_distribution():
    os.system("wlect dis config.txt ./defaults/lpar.txt lecode=./files/rel/lecode-@.bin -o")

def patch_main_dol():
    os.system("wstrt patch sys/main.dol --clean-dol --add-lecode")

# FINALISATION
def remove_files():
    os.remove("Common.txt")
    os.remove("tracks.bmg.txt")
    print(os.getcwd())
    for file in os.listdir(os.path.join(os.getcwd(), "img")):
        print(file)

# MAIN
def main(extract_common, keep_files, overwrite_tpl):
    os.chdir(r"C:\Users\sack-\Documents\Dolphin ISOs\Mario Kart Wii\DATA")

    create_files()
    
    config_to_tracks()
    restore_track_names()
    patch_ui_common()

    if overwrite_tpl:
        patch_ui_tpl()

    update_distribution()
    patch_main_dol()

    if extract_common:
        course_extract_common()

    if not keep_files:
        remove_files()

if __name__ == "__main__":
    extract_common = False
    keep_files = False
    overwrite_tpl = False
    if len(sys.argv) > 1:
        # First arg is always the file
        if "-e" in sys.argv:
            extract_common = True
        if "-k" in sys.argv:
            keep_files = True
        if "-t" in sys.argv:
            overwrite_tpl = True
    main(extract_common, keep_files, overwrite_tpl)
