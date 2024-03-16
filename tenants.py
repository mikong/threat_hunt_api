from uuid import uuid4
from flask import abort

TENANT_NAMES = [
    "Cisco Systems, Inc.",
    "The Cigna Group",
    "AT&T Inc.",
    "Microsoft Corporation"
]

TENANTS = {}
for name in TENANT_NAMES:
    id = str(uuid4())
    TENANTS[id] = {
        "id": id,
        "name": name
    }

def index():
    return list(TENANTS.values())

def create(tenant):
    name = tenant.get("name")

    if name is None or name == "":
        abort(406, "Name is missing")

    id = str(uuid4())
    TENANTS[id] = {
        "id": id,
        "name": name
    }
    return TENANTS[id], 201
