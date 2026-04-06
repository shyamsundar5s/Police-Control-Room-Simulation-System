import random
import time

# -------------------------------
# Police Unit Class
# -------------------------------
class PoliceUnit:
    def __init__(self, unit_id, location):
        self.unit_id = unit_id
        self.location = location
        self.available = True

    def assign(self):
        self.available = False

    def release(self):
        self.available = True

# -------------------------------
# Incident Class
# -------------------------------
class Incident:
    def __init__(self, complaint, location):
        self.complaint = complaint
        self.location = location
        self.priority = self.classify_priority()
        self.status = "Pending"

    def classify_priority(self):
        keywords_high = ["murder", "gun", "kidnap", "terror"]
        keywords_medium = ["fight", "robbery", "accident"]
        
        for word in keywords_high:
            if word in self.complaint.lower():
                return "HIGH"
        
        for word in keywords_medium:
            if word in self.complaint.lower():
                return "MEDIUM"
        
        return "LOW"

# -------------------------------
# Dispatcher System
# -------------------------------
class Dispatcher:
    def __init__(self):
        self.units = []
        self.incidents = []

    def add_unit(self, unit):
        self.units.append(unit)

    def report_incident(self, incident):
        print(f"\n📞 New Incident Reported: {incident.complaint}")
        print(f"📍 Location: {incident.location}")
        print(f"⚠️ Priority: {incident.priority}")
        self.incidents.append(incident)
        self.dispatch_unit(incident)

    def dispatch_unit(self, incident):
        available_units = [u for u in self.units if u.available]

        if not available_units:
            print("❌ No units available! Waiting...")
            return

        unit = random.choice(available_units)
        unit.assign()
        incident.status = "Assigned"

        print(f"🚓 Unit {unit.unit_id} dispatched to {incident.location}")

        # Simulate response time
        time.sleep(2)

        incident.status = "Resolved"
        unit.release()

        print(f"✅ Incident resolved by Unit {unit.unit_id}")

    def show_status(self):
        print("\n📊 Incident Status Dashboard")
        for i, incident in enumerate(self.incidents, 1):
            print(f"{i}. {incident.complaint} | {incident.status} | {incident.priority}")

# -------------------------------
# Simulation
# -------------------------------
def simulate():
    dispatcher = Dispatcher()

    # Add police units
    locations = ["North Zone", "South Zone", "East Zone", "West Zone"]
    for i in range(5):
        dispatcher.add_unit(PoliceUnit(i+1, random.choice(locations)))

    # Sample incidents
    complaints = [
        ("Robbery in bank", "South Zone"),
        ("Car accident", "East Zone"),
        ("Kidnap case reported", "North Zone"),
        ("Noise complaint", "West Zone"),
        ("Gun firing incident", "South Zone")
    ]

    for comp, loc in complaints:
        incident = Incident(comp, loc)
        dispatcher.report_incident(incident)
        time.sleep(1)

    dispatcher.show_status()

# -------------------------------
# Run Program
# -------------------------------
if __name__ == "__main__":
    simulate()