import json

print("Interface Status")
print("="*80)
print("{: <50} {: <21} {: <8} {: <1}".format("DN", "Description", "Speed", "MTU"))
print("-------------------------------------------------- --------------------  ------  ------")

with open("data.json", "r") as data_js:
    data_py= json.load(data_js)
    for object in data_py["imdata"]:
        dn = object["l1PhysIf"]["attributes"]["dn"]
        descr = object["l1PhysIf"]["attributes"]["descr"]
        speed = object["l1PhysIf"]["attributes"]["speed"]
        mtu = object["l1PhysIf"]["attributes"]["mtu"]
        print("{: <50} {: <21} {: <8} {: <1}".format(dn, descr, speed, mtu))

