Generated from api_key_views.py on 2021-09-17 13:22:42.251452

# peeringdb_server.api_key_views

Views for organization api key management

# Functions
---

## add_user_key
`def add_user_key(request, **kwargs)`

Create a new User API key

Requires a name and a readonly boolean.

---
## load_all_key_permissions
`def load_all_key_permissions(org)`

Returns dict of all users with all their permissions for
the given org

---
## remove_user_key
`def remove_user_key(request, **kwargs)`

Revoke user api key

---
## save_key_permissions
`def save_key_permissions(org, key, perms)`

Save key permissions for the specified org and key

perms should be a dict of permissioning ids and permission levels

---