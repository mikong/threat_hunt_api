# Threat Hunt API

## API

```
/api/tenants
/api/technologies
/api/assets
/api/hunts
```

## Database Schema

```
tenants
  - id: uuid
  - name: varchar

technologies
  - id: uuid
  - name: varchar
  - versions: json

assets
  - id: uuid
  - mac_address: varchar
  - host: varchar
  - timestamp: numeric
  - tenant_id: uuid
  - running_tech: json

hunts
  - id: uuid
  - name: varchar
  - description: text
  - tenant_id: uuid
  - asset_ids: uuid[]
```

## Project Setup

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install Flask==2.3.3
pip install "connexion[swagger-ui]==2.14.2"
```
