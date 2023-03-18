import os

def fill_config():
    print("*ворчливо* Вообще то и сами могли зайти отредактировать \n")

    print("Введите ваше расширение равов, моё например .NEF")
    print("Если расширений несколько, введите через пробел")
    raw_format = input().split(" ")
    raw_format_configStr = "расширение равов = " + " ".join(raw_format) #генератор строк для нескольких равов

    print("Введите путь к папке со всеми фотографиями")
    photos_folder_configStr = "папка со всеми фотографиями = " + input()

    print("Введите путь к папке с отобранными джипегами")
    otborki_configStr = "папка с отборками = " + input()

    print("Введите путь к папке куда кидать равы")
    raw_folder_configStr = "папка куда закинуть = " + input()

    
    with open("config.txt", "w") as file: #собсна запись в файл
        file.write("\n".join([raw_format_configStr, photos_folder_configStr, otborki_configStr, raw_folder_configStr]))
        


def check_config(): #если конфига нет - создаёт, спрашивает заполнить ли при всех удобных случаях | это сделанно что бы после чека уже использовать его или ручками вводить всё
    config_default = "расширение равов = <> <>" + "\n" + "папка со всеми фотографиями = <>" + "\n" + "папка с отборками = <>" + "\n" + "папка куда закинуть = <>"
    current_dir = os.getcwd()
    configUsage = False

    configExists = False
    for file in os.listdir(current_dir): #проверка есть ли уже конфиг файл в папке с прогой
        filename = os.fsdecode(file)
        if filename == "config.txt":
            configExists = True
            break

    if(not configExists): #создаём дефолт конфиг при отстутствии оного
        with open("config.txt", "w") as f:
            f.write(config_default)
        print("Конфиг не обнаружен, но был создан. Хотите заполнить его для дальнейшего упрощения работы? (да/нет)")
        if input() == "да":
            fill_config()
            configUsage = True
    else:
        with open("config.txt", "r") as file: #проверка на пустоту
            configContent = file.read()
        if(configContent == config_default):
            print("Конфиг обнаружен, но он пуст. Хотите заполнить его для дальнейшего упрощения работы? (да/нет)")
            if input() == "да":
                fill_config()
                configUsage = True
        else:
            print("Конфиг обнаружен. Используем? (да/нет)") #проверка на использование
            if input() == "да":
                configUsage = True

    return configUsage 


def readConfig():
    with open("config.txt", "r") as file: #считываем данные с конфига
        configContent = file.read().split("\n")

    photos_folder = configContent[1] #впадлу в одну строку реализовывать | тут мы уже реально достаём всё из конфига
    photos_folder = photos_folder[photos_folder.find("=") + 2:]
    otborki_folder = configContent[2]
    otborki_folder = otborki_folder[otborki_folder.find("=") + 2:]
    raw_folder = configContent[3]
    raw_folder = raw_folder[raw_folder.find("=") + 2:]
    rawTypes = configContent[0]
    rawTypes = rawTypes[rawTypes.find("=") + 2:].split(" ")

    return(rawTypes, photos_folder, otborki_folder, raw_folder)