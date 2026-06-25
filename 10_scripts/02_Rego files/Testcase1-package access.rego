package access.control

# ----------------------------------
# Default decision: deny everything
# ----------------------------------
default decision = "Rejected"

# ----------------------------------
# Hard denies (highest priority)
# ----------------------------------

# Blacklisted users are always denied
decision = "Rejected" {
    input.user.role == "blacklisted"
}

# Blocked applications are always denied
decision = "Rejected" {
    input.application.status == "blocked"
}

# Untrusted devices on remote networks are denied
decision = "Rejected" {
    input.device.trust == "untrusted"
    input.network.location == "remote"
}

# ----------------------------------
# Allow rules
# ----------------------------------

# Admin access: trusted device, any network, allowed app
decision = "Granted" {
    input.user.role == "admin"
    input.application.status == "allowed"
    input.device.trust == "trusted"
}

# Guest access: local network only, trusted device, allowed app
decision = "Granted" {
    input.user.role == "guest"
    input.application.status == "allowed"
    input.network.location == "local"
    input.device.trust == "trusted"
}

# ----------------------------------
# Optional: explicit fallback reject
# (clarity for audits/logs)
# ----------------------------------
decision = "Rejected" {
    not decision == "Granted"
}
