Generated from data_views.py on 2021-09-17 13:22:42.251452

# peeringdb_server.data_views

This holds JSON views for various data sets

Mostly these are needed for filling form-selects for editable
mode in UX

# Functions
---

## asns
`def asns(request)`

Returns a JSON response with a list of asns that the user's
organizations own, to use for selecting asn in netixlan
creation

---
## countries
`def countries(request)`

Returns all valid countries and their country codes

---
## countries_w_blank
`def countries_w_blank(request)`

Returns all valid countries and their country codes with a blank field

---
## facilities
`def facilities(request)`

Returns all valid facilities with id and name

---
## my_organizations
`def my_organizations(request)`

Returns a JSON response with a list of organization names and ids
that the requesting user is a member of

---
## organizations
`def organizations(request)`

Returns a JSON response with a list of organization names and ids
This is currently only used by the org-merge-tool which is only
available to site administrators.

---
## sponsorships
`def sponsorships(request)`

Returns all sponsorships

---