"""
This is the people module and supports all the ReST actions for the
PEOPLE collection
"""

# System modules
from datetime import datetime

# 3rd party modules
from flask import make_response, abort

import json, requests
#response = requests.get("https://jsonplaceholder.typicode.com/todos")
#todos = json.loads(response.text)
headers = {"Authorization": "Bearer dba483aa545ab0c2a48c245184af573ce681f185cd949c3d3ab18f36bd8a21815f41bf5bb8490a16a9bc3261cc0db1a906f46ffa2bd56f78ecc35f57e9294c5a","Content-Type":"application/json"}
response = requests.get("https://hackicims.com/api/v1/companies/57/jobs", headers=headers)
jobs = json.loads(response.text)



def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API
PEOPLE = {
    "Farrell": {
        "fname": "Data Scientist",
        "lname": "1",
        "timestamp": get_timestamp(),
    },
    "Brockman": {
        "fname": "Architect",
        "lname": "2",
        "timestamp": get_timestamp(),
    },
    "Easter": {
        "fname": "UX Designer",
        "lname": "3",
        "timestamp": get_timestamp(),
    },
}
    
from functools import reduce  # forward compatibility for Python 3
import operator

def getFromDict(dataDict, mapList):
    return reduce(operator.getitem, mapList, dataDict)

def setInDict(dataDict, mapList, value):
    getFromDict(dataDict, mapList[:-1])[mapList[-1]] = value
    

def read_all():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        json string of list of people
    """
    # Create the list of people from our data
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]


def read_one(lname):
    """
    This function responds to a request for /api/people/{lname}
    with one matching person from people

    :param lname:   last name of person to find
    :return:        person matching last name
    """
    # Does the person exist in people?
    if lname in PEOPLE:
        person = PEOPLE.get(lname)

    # otherwise, nope, not found
    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )

    return person


def create(person):
    """
    This function creates a new person in the people structure
    based on the passed in person data

    :param person:  person to create in people structure
    :return:        201 on success, 406 on person exists
    """
    lname = person.get("lname", None)
    fname = person.get("fname", None)

    # Does the person exist already?
    if lname not in PEOPLE and lname is not None:
        PEOPLE[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp(),
        }
        return PEOPLE[lname], 201

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Peron with last name {lname} already exists".format(lname=lname),
        )


def update(lname, person):
    """
    This function updates an existing person in the people structure

    :param lname:   last name of person to update in the people structure
    :param person:  person to update
    :return:        updated person structure
    """
    # Does the person exist in people?
    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person.get("fname")
        PEOPLE[lname]["timestamp"] = get_timestamp()

        return PEOPLE[lname]

    # otherwise, nope, that's an error
    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )


def delete(lname):
    """
    This function deletes a person from the people structure

    :param lname:   last name of person to delete
    :return:        200 on successful delete, 404 if not found
    """
    # Does the person to delete exist?
    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response(
            "{lname} successfully deleted".format(lname=lname), 200
        )

    # Otherwise, nope, person to delete not found
    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )

jobCount = len(jobs)
for i in range(0, jobCount):
    print(jobs[i] )
    id = getFromDict(jobs[i], ['id'])
    title = getFromDict(jobs[i], ['title'])
    print(id, title)
    lname = str(id)
    fname = title
    person = {}
    person = {"lname": lname,
              "fname": fname}
    create(person)
#   print(jobs[i].'id')
#    jobs[id]
#    PEOPLE[lname] = {
#            "lname": lname,
#            "fname": fname,
#           "timestamp": get_timestamp(),
#       }
            
