import json
from datetime import date


print("\nWelcome to cli draft tool\n")


def newDraft():
    chutiyeCount = int(input("\nEnter number of chutiye playing: "))
    draftCount = int(input("\nEnter number of players ya'll drafting: "))

    data = {}
    chutiye = []

    for i in range(chutiyeCount):
        name = input("\nEnter name of chutiya: ")
        chutiye.append(name)
        data[name] = {}
        data[name]['draftCount'] = draftCount
        club = input(f"Enter club for {name}: ")
        data[name]['club'] = club
        data[name]['team'] = []

    roundRobin(data, chutiye)
    fileName = createFileName(data)

    with open(fileName, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
    with open(fileName, 'r', encoding='utf-8') as file:
        content = json.load(file)
        print('data from the file:')
        print(content)


def roundRobin(dict, list):
    flag = 1

    while True:
        if flag > 0:
            for name in list:
                if dict[name]['draftCount'] == 0:
                    flag = 0
                    break
                dict[name]['draftCount'] = dict[name]['draftCount'] - 1
                print(f"\nEnter player pick for {name}")
                pick = input()
                dict[name]['team'].append(pick)

        elif flag < 0:
            for name in reversed(list):
                if dict[name]['draftCount'] == 0:
                    flag = 0
                    break
                dict[name]['draftCount'] = dict[name]['draftCount'] - 1
                print(f"\nEnter player pick for {name}")
                pick = input()
                dict[name]['team'].append(pick)

        else:
            print("breaking out of the while loop")
            break

        flag = flag * -1


def createFileName(data):  # should return a string
    fileName = ""
    for name in data:
        fileName = fileName + name.capitalize() + '__'

    today = date.today()
    formatted_date_time = today.strftime("%Y-%m-%d")
    fileName = fileName + formatted_date_time + ".json"
    return fileName

def main():
    print("Options-")
    print("1: start a new draft")
    print("2: load previous draft")
    print("3: delete previous draft")

    choice = int(input("Enter what you wanna do: "))
    print(choice)
    if choice == 1:
        newDraft()


main()
