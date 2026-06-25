package zerotrust.access

default access = "none"

# Weights (can be tuned experimentally)
user_weight = 0.4
device_weight = 0.4
app_weight = 0.2

# Compute aggregate trust
aggregate_trust = score {
    score :=
        (input.user.trust_score * user_weight) +
        (input.device.trust_score * device_weight) +
        ((1 - input.application.risk_score) * app_weight)
}

# Blacklisted users always denied
access = "none" {
    input.user.category == "blacklisted"
}

# Full access
access = "full" {
    input.user.category == "admin"
    aggregate_trust >= 0.75
}

# Limited access
access = "limited" {
    aggregate_trust >= 0.45
    aggregate_trust < 0.75
}
