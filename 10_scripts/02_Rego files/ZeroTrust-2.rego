package zerotrust.access

# Default decision
default access = "none"

########################
# DENY RULES (highest priority)
########################

# Blacklisted users are always denied
access = "none" {
    input.user.category == "blacklisted"
}

# Blocked applications are always denied
access = "none" {
    input.application.type == "blocked"
}

########################
# FULL ACCESS
########################

# Admin on trusted device accessing allowed app
access = "full" {
    input.user.category == "admin"
    input.device.trust == "trusted"
    input.application.type == "allowed"
}

########################
# LIMITED ACCESS
########################

# Admin on untrusted device accessing allowed app
access = "limited" {
    input.user.category == "admin"
    input.device.trust == "untrusted"
    input.application.type == "allowed"
}

# Guest on trusted device accessing allowed app
access = "limited" {
    input.user.category == "guest"
    input.device.trust == "trusted"
    input.application.type == "allowed"
}

########################
# EXPLICIT NO ACCESS (defense-in-depth)
########################

# Guest on untrusted device
access = "none" {
    input.user.category == "guest"
    input.device.trust == "untrusted"
}

JSON
{
  "user": {
    "id": "user123",
    "category": "admin"
  },
  "device": {
    "id": "deviceA",
    "trust": "trusted"
  },
  "application": {
    "name": "finance-dashboard",
    "type": "allowed"
  }
}


