import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtCore import QCoreApplication
import urllib.request
import json
import csv

def SummonAzure(cntEligible,
                gender,
                partyAffiliation,
                householdHead,
                householdRank,
                mailOrder,
                income,
                compOwner,
                homeOwner,
                cnt,
                educationLevel,
                dontPhone):
    if gender[0] is "M":
        gender = 'M'
    else:
        gender = 'F'

    if partyAffiliation[0] is 'D':
        partyAffiliation = 'D'
    elif partyAffiliation[0] is 'R':
        partyAffiliation = 'R'
    else:
        partyAffiliation = 'U'
    print('Party affiliation is: '+partyAffiliation)

    if householdHead[0] is 'H':
        householdHead = 'H'
    else:
        householdHead = 'M'
    print('householdHead is: '+householdHead)

    if householdRank[0] is '1':
        householdRank = '1'
    print('Household rank is: ' + householdRank)

    if mailOrder[0:2] is 'I o':
        mailOrder = '1'
    else:
        mailOrder = '0'
    print('mailOrder is : ' + mailOrder)

    if income[0:4] is 'Under':
        income = 'A'
    elif income[0:4] is '$15,0':
        income = 'B'
    elif income[0:4] is '$25,0':
        income = 'C'
    elif income[0:4] is '$35,0':
        income = 'D'
    elif income[0:4] is '$50,0':
        income = 'E'
    elif income[0:4] is '$75,0':
        income = 'F'
    elif income[0:4] is '$100,':
        income = 'G'
    elif income[0:4] is '$125,':
        income = 'H'
    elif income[0:4] is '$150,':
        income = 'I'
    elif income[0:4] is '$175,':
        income = 'J'
    elif income[0:4] is '$200,':
        income = 'K'
    else:
        income = 'L'
    print('Income is: '+income)

    if compOwner[0:3] is 'I  o':
        compOwner = 1
    else:
        compOwner = 0
    print('compOwner is: '+str(compOwner))

    if homeOwner[0] is 'R':
        homeOwner = 'A'
    elif homeOwner[0:9] is 'Probable R':
        homeOwner = 'B'
    elif homeOwner[0:9] is 'Probable H':
        homeOwner = 'C'
    else:
        homeOwner = 'D'
    print('homeOwner is: '+homeOwner)

    if educationLevel[0] is '6':
        educationLevel = 'F'
    elif educationLevel[0] is '1':
        educationLevel = 'A'
    elif educationLevel[0] is '2':
        educationLevel = 'B'
    elif educationLevel[0] is '3':
        educationLevel = 'C'
    elif educationLevel[0] is '4':
        educationLevel = 'D'
    elif educationLevel[0] is '5':
        educationLevel = 'E'
    else:
        educationLevel = 'G'
    print('educationLevel is: ' + educationLevel)

    if dontPhone[0:5] is "I'm on":
        dontPhone = 'Y'
    elif dontPhone[0:5] is "I'm no":
        dontPhone = 'N'
    else:
        dontPhone = 'U'
    print('dontPhone is: '+dontPhone)
    print()

    data = {"Inputs": {"input1":[{'id': "1",'gender': "M",'partyAffiliation': "U",'partyMix': "noneR",'householdHead': "M",'householdRank': "3+",'income': "D",'homeOwner': "A",'mailOrder': "1",'compOwner': "0",'educationLevel': "B",'donateReligion': "0",'donatePolitics': "0",'donateArts': "0",'donateAnimals': "0",'donateChild': "0",'donateHealth': "1",'donatePoverty': "0",'donateEnvironment': "0",'fec_01_02': "0",'fec_99_00': "0",'fec_97_98': "0",'fec_95_96': "0",'fec_93_94': "0",'fec_03_04': "0",'fec_05_06': "0",'dontPhone': "N",'ageD': "9420",'cnt': "0",'gen90': "0",'pri90': "0",'oth90': "0",'gen91': "0",'pri91': "0",'oth91': "0",'gen92': "0",'ppp92': "0",'oth92': "0",'gen93': "0",'pri93': "0",'oth93': "0",'gen94': "0",'pri94': "0",'oth94': "0",'gen95': "0",'pri95': "0",'oth95': "0",'gen96': "0",'ppp96': "0",'oth96': "0",'gen97': "0",'pri97': "0",'oth97': "0",'gen98': "0",'pri98': "0",'oth98': "0",'gen99': "0",'pri99': "0",'oth99': "0",'gen00': "0",'ppp00': "0",'oth00': "0",'gen01': "0",'pri01': "0",'oth01': "0",'gen02': "0",'pri02': "0",'oth02': "0",'pri03': "0",'gen03': "0",'oth03': "0",'ppp04': "0",'oth04': "0",'gen04': "0",'cntEligible': "0",'percentAttended': "0",'ageY': "25.7715036112935",'pProb': "0.357449277351257",'pNodes': "12",'ageC': "(19.2,36.7]",'incC': "35k-75k",'eduC': "primary",'pSegs': "10",}],},"GlobalParameters":  {}}

    data["Inputs"]["input1"][0]["cntEligible"]      = cntEligible
    data["Inputs"]["input1"][0]["gender"]           = gender
    data["Inputs"]["input1"][0]["partyAffiliation"] = partyAffiliation
    data["Inputs"]["input1"][0]["householdHead"]    = householdHead
    data["Inputs"]["input1"][0]["householdRank"]    = householdRank
    data["Inputs"]["input1"][0]["mailOrder"]        = mailOrder
    data["Inputs"]["input1"][0]["income"]           = income
    data["Inputs"]["input1"][0]["compOwner"]        = compOwner
    data["Inputs"]["input1"][0]["homeOwner"]        = homeOwner
    data["Inputs"]["input1"][0]["cnt"]              = cnt
    data["Inputs"]["input1"][0]["educationLevel"]   = educationLevel
    data["Inputs"]["input1"][0]["dontPhone"]        = dontPhone

    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/63d46014c41343d4876bcf4f4e0b04f5/services/585e83670fb24ed08163f11026dd9b7f/execute?api-version=2.0&format=swagger'
    api_key = 'YVcsMr/dZv02JnKDFx4MD7n9R3h0/rXfGI5PmquL6joBBl/FYcUs7fFpXbg02OYnlK2VHdQxV+pfXVKAUu0UsA==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        result = result.decode('utf-8')
        result = result.split(':')
        result = result[83]
        finalresult = ''
        for i in range(0,len(result)-1):
            if result[i].isdigit() or result[i] is '.':
                finalresult += result[i]
        finalresult = float(finalresult)
        finalresult = finalresult*100
        finalresult = round(finalresult,2)
        return(finalresult)
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(json.loads(error.read().decode("utf8", 'ignore')))
