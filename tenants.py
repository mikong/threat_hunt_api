from uuid import uuid4

TENANTS = {
    "Cisco": {
        "id": str(uuid4()),
        "name": "Cisco Systems, Inc."
    },
    "Cigna": {
        "id": str(uuid4()),
        "name": "The Cigna Group"
    },
    "ATT": {
        "id": str(uuid4()),
        "name": "AT&T Inc."
    },
    "Microsoft": {
        "id": str(uuid4()),
        "name": "Microsoft Corporation"
    }
}

def index():
    return list(TENANTS.values())
