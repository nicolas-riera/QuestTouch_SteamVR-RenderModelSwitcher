import os

from src.get_SteamVR_path import real_case_path, find_steam_path

def check_current_rendermodel(device):
    
    if device == "Quest 3":
        if os.path.exists(os.path.join(real_case_path(find_steam_path()), "steamapps", "common", "SteamVR", "resources", "rendermodels", "oculus_quest_plus_controller_left", "oculus_quest_plus_controller_left.obj")):
            return "Touch Plus"
        elif os.path.exists(os.path.join(real_case_path(find_steam_path()), "steamapps", "common", "SteamVR", "resources", "rendermodels", "oculus_quest_plus_controller_left", "oculus_quest_pro_controller_left.obj")):
            return "Touch Pro"
        else:
            return "Unknown"
    elif device == "Quest 2":
        if os.path.exists(os.path.join(real_case_path(find_steam_path()), "steamapps", "common", "SteamVR", "resources", "rendermodels", "oculus_quest2_controller_left", "oculus_quest2_controller_left.obj")):
            return "Touch Quest 2"
        elif os.path.exists(os.path.join(real_case_path(find_steam_path()), "steamapps", "common", "SteamVR", "resources", "rendermodels", "oculus_quest2_controller_left", "oculus_quest_pro_controller_left.obj")):
            return "Touch Pro"
        else:
            return "Unknown"
    elif device == "Wands":
        if os.path.exists(os.path.join(real_case_path(find_steam_path()), "steamapps", "common", "SteamVR", "resources", "rendermodels", "vr_controller_vive_1_5", "custom_sensor")):
            return "Vive Controllers 2.0"
        elif os.path.exists(os.path.join(real_case_path(find_steam_path()), "steamapps", "common", "SteamVR", "resources", "rendermodels", "vr_controller_vive_1_5", "onepointfive_texture.png")):
            return "Vive Controllers 1.0"
        else:
            return "Unknown"
