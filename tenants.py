from uuid import uuid4
from flask import abort, make_response

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

def show(id):
    if id not in TENANTS:
        abort(404, "Tenant not found")
    
    return TENANTS[id]

def update(id, tenant):
    if id not in TENANTS:
        abort(404, "Tenant not found")
    
    name = tenant.get("name")

    if name is None or name == "":
        abort(406, "Name is missing")

    TENANTS[id]["name"] = name
    return TENANTS[id]

def delete(id):
    if id not in TENANTS:
        abort(404, "Tenant not found")
    
    del TENANTS[id]
    return make_response("Tenant successfully deleted", 200)
