#!/usr/bin/python
import sys
import json
from random import randrange, randint
from datetime import timedelta, datetime


def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


if len(sys.argv) != 5:
    print('Bad arguments, use a format like this: ticket_gen -n 1000 -o activities.json')
    exit(128)

num_of_random_activities = int(sys.argv[2])

list_of_tickets = {
    "metadata": {
        "start_at": str(datetime.now()),
        "end_at": '',
        "activities_count": 0
    },
    "activities_data": []
}

d1 = datetime.strptime('1/1/2019 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('7/7/2020 4:50 AM', '%m/%d/%Y %I:%M %p')

status = ['Open', 'Closed', 'Resolved', 'Waiting for Customer',
          'Waiting for Third Party', 'Pending']

for i in range(num_of_random_activities):
    list_of_tickets['activities_data'].append({
        "performed_at": str(random_date(d1, d2)),
        "ticket_id": i,
        "performer_type": "user",
        "performer_id": i,
        "activity": {
            "shipping_address": "N/A",
            "shipment_date": "21 Apr, 2017",
            "category": "Phone",
            "contacted_customer": True,
            "issue_type": "Incident",
            "source": 3,
            "status": status[randint(0, 5)],
            "priority": 4,
            "group": "refund",
            "agent_id": 149018,
            "requester": 145423,
            "product": "mobile", }})

list_of_tickets['metadata']['end_at'] = str(datetime.now())
list_of_tickets['metadata']['activities_count'] = len(
    list_of_tickets['activities_data'])

json_tickets = json.dumps(list_of_tickets)
f = open(sys.argv[4], "w")
f.write(json_tickets)
f.close()
