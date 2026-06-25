Testcase 3 temporal decay

package zero_trust3_2.access

# Weighted trust calculation
user_weights = {
    "admin": 1.0,
    "guest": 0.5,
    "blacklisted": 0.0
}

device_weights = {
    "trusted": 1.0,
    "untrusted": 0.3
}

app_weights = {
    "allowed": 1.0,
    "blocked": 0.0
}

# Contextual trust algorithm
trust_score := score {
    user_weight := user_weights[input.user.category]
    device_weight := device_weights[input.device.category]
    app_weight := app_weights[input.application.type]
    
    # Weighted average
    score := (user_weight * 0.4) + (device_weight * 0.4) + (app_weight * 0.2)
}






package zero_trust3_2.temporal

# Session management with decay
sessions := {
    "session123": {
        "user": "admin",
        "device": "trusted",
        "start_time": 1672531200,
        "last_activity": 1672534800,
        "trust_score": 0.9
    }
}

# Temporal decay function
decayed_trust(session_id) = score {
    session := sessions[session_id]
    current_time := time.now_ns() / 1000000000  # Convert to seconds
    idle_time := current_time - session.last_activity
    
    # Exponential decay: trust = initial_trust * e^(-λ * idle_time)
    decay_rate := 0.0001  # λ = decay constant
    score := session.trust_score * math.exp(-decay_rate * idle_time)
}

# Dynamic access level
access_level := level {
    trust := decayed_trust(input.session_id)
    
    level := "full" {
        trust >= 0.75
    }
    
    level := "limited" {
        trust >= 0.45
        trust < 0.75
    }
    
    level := "none" {
        trust < 0.45
    }
}



Component	Purpose	Port	Access
Host System	Ubuntu 24.04 base with SDN support	-	Local
Open vSwitch	Network layer microsegmentation	6653	Local
OpenDaylight	SDN controller & policy administrator	8181	http://localhost:8181

Keycloak	Identity & device trust anchor	8080	http://localhost:8080

Open Policy Agent	Policy decision engine	8182	http://localhost:8182

Envoy Proxy	Application-level enforcement	10000	http://localhost:10000

Mininet	Network topology emulation	-	CLI
