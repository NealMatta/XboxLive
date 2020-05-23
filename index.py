# pylint: skip-file
import requests
from secret import headers


def grabXuid():
    print("Grabbing my XUID")
    response = requests.get(
        "https://xapi.us/v2/accountxuid", headers=headers)
    if response.status_code == 200:
        cleanResponse = response.json()
        return(cleanResponse["xuid"])
    else:
        print("Error: Could not get XUID from XAPI")
        quit()


def grabAllFriends(xuid):
    print("Grabbing all friends")
    URL = "https://xapi.us/v2/{}/friends".format(xuid)
    response = requests.get(URL, headers=headers)

    allFriends = []

    if response.status_code == 200:
        cleanResponse = response.json()
        for user in cleanResponse:
            allFriends.append(user['Gamertag'])
        return allFriends
    else:
        print("Error: Could not get Friends from XAPI")
        quit()


def generateFriendsXuid(friends):
    print("Generating the friends XUID")
    friendXuidDict = {}

    for friend in friends:
        URL = "https://xapi.us/v2/xuid/{}".format(friend)
        response = requests.get(URL, headers=headers)

        if response.status_code == 200:
            friendXuid = response.json()
            friendXuidDict[friend] = friendXuid
        else:
            print("Error: Could not get Friends from XAPI")
            quit()

    return friendXuidDict


def getStatus(friends, friendXuidDict):
    print("Getting Statuses of Friends")
    friendStatusDict = {}

    for friend in friends:
        URL = "https://xapi.us/v2/{}/presence".format(friendXuidDict[friend])
        response = requests.get(URL, headers=headers)
        if response.status_code == 200:
            cleanResponse = response.json()
            if cleanResponse['state'] == 'Online':
                friendStatusDict[friend] = cleanResponse['state']
        else:
            print("Error: Could not get XUID from XAPI")
            quit()

    return friendStatusDict


if __name__ == '__main__':
    xuid = grabXuid()
    friends = grabAllFriends(xuid)
    friendXuidDict = generateFriendsXuid(friends)
    allStatuses = getStatus(friends, friendXuidDict)

    print(allStatuses)
