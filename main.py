import os
from colorama import init, Fore, Style
from configTools import check_config, fill_config, readConfig

init(convert = True) #это тут что бы цвета нормально в консоли работали

configUsage = check_config() #решаем использовать ли конфиг
if(configUsage == False): 
    print(Fore.LIGHTBLUE_EX + "Введите ваше расширение равов, моё например .NEF" + Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "Если расширений несколько, введите через пробел" + Style.RESET_ALL)
    rawTypes = input().split(" ")
    print(" ".join(rawTypes) + Fore.GREEN + " - расширения равоф" + Style.RESET_ALL)

    print(Fore.LIGHTBLUE_EX + "Введите путь к папке со всеми фотографиями" + Style.RESET_ALL) 
    photos_folder = input()
    print(photos_folder + Fore.GREEN + " - папка со всеми" + Style.RESET_ALL) #папка со всеми
    print()

    print(Fore.LIGHTBLUE_EX + "Введите путь к папке с отобранными жипегами" + Style.RESET_ALL)
    otborki_folder = input()
    print(otborki_folder + Fore.GREEN + " - папка с отборками" + Style.RESET_ALL) #папка с отборками
    print()

    print(Fore.LIGHTBLUE_EX +  "Введите путь к папке куда закинуть равы" + Style.RESET_ALL)
    raw_folder = input() 
    print(raw_folder + Fore.GREEN +" - папка с равами" + Style.RESET_ALL) #папка с равами
    print()
    print()

else:
    config = readConfig()
    rawTypes = config[0]
    photos_folder = config[1]
    otborki_folder = config[2]
    raw_folder = config[3]

photos_dir = os.fsencode(photos_folder)
otborki_dir = os.fsencode(otborki_folder)
#обозначил рабочие директории
otborki_names = []

for file in os.listdir(otborki_dir): #добавляем имена файлов которые нужно перекинуть в папку с равами
    filename = os.fsdecode(file)
    if (filename.endswith(".JPG") or filename.endswith(".jpg")):
        otborki_names.append(filename[:-4])

for file in os.listdir(photos_dir): #определяем рав/не рав и собсна копируем
    filename = os.fsdecode(file)
    isRaw = False
    if(filename[-4:] in rawTypes):#проверка на равы v2
        isRaw = True

    if (filename[:-4] in otborki_names) and (isRaw):
        filePath =  photos_folder + "\\" + filename #собираем путь к файлу
        os.system("copy " + filePath + " " + raw_folder)
        print("copy " + filePath + " " + raw_folder)
