import json

with open('sample-data.json', 'r') as file:
    data = json.load(file)

print("Interface Status")
print("---")
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("---")

for item in data['imdata']:
    dn = item['l1PhysIf']['attributes']['dn']
    description = item['l1PhysIf']['attributes'].get('descr', 'inherit')
    speed = item['l1PhysIf']['attributes'].get('speed', 'inherit')
    mtu = item['l1PhysIf']['attributes'].get('mtu', 'inherit')
    print("{:<50} {:<20} {:<8} {:<6}".format(dn, description, speed, mtu))