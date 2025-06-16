import uuid

random_uuid = uuid.uuid4()
print("Random UUID:", random_uuid)


namespace = uuid.NAMESPACE_DNS
name_uuid = uuid.uuid5(namespace, "example.com")
print("UUID using namespace:", name_uuid)
