import uuid

uuid1 = uuid.uuid4()
uuid2 = uuid.uuid4()

print("UUID1:", uuid1)
print("UUID2:", uuid2)

if uuid1 == uuid2:
    print("UUIDs are equal")
else:
    print("UUIDs are different")
