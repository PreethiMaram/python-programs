# Athlete Class
class Athlete:
    def __init__(self, athlete_id, name, sport, gpa):
        self.athlete_id = athlete_id
        self.name = name
        self.sport = sport
        self.gpa = gpa          #grade point average
        self.scholarships = []       # List to store awarded scholarships
    
    def add_scholarship(self, scholarship):
        self.scholarships.append(scholarship)
    
    def __repr__(self):
        return f"(Athlete(ID: {self.athlete_id}, Name: {self.name}, Sport: {self.sport}, GPA: {self.gpa})"

# Scholarship Class
class Scholarship:
    def __init__(self, scholarship_id, name, amount, criteria):
        self.scholarship_id = scholarship_id
        self.name = name
        self.amount = amount
        self.criteria = criteria  # Link to Criteria object
    
    def __repr__(self):
        return f"Scholarship(ID: {self.scholarship_id}, Name: {self.name}, Amount: {self.amount}, Criteria: {self.criteria})"

# Criteria Class
class Criteria:
    def __init__(self, criteria_id, min_gpa, sport):
        self.criteria_id = criteria_id
        self.min_gpa = min_gpa
        self.sport = sport
    
    def is_eligible(self, athlete):
        return athlete.gpa >= self.min_gpa and athlete.sport == self.sport
    
    def __repr__(self):
        return f"Criteria(ID: {self.criteria_id}, Min GPA: {self.min_gpa}, Sport: {self.sport})"

# Data storage dictionaries
athletes = {}
scholarships = {}
criteria_list = {}

# Create/Update Athlete
def create_update_athlete(athlete_id, name, sport, gpa):
    athletes[athlete_id] = Athlete(athlete_id, name, sport, gpa)
    return athletes[athlete_id]

# Create/Update Scholarship
def create_update_scholarship(scholarship_id, name, amount, criteria_id):
    if criteria_id in criteria_list:
        scholarships[scholarship_id] = Scholarship(scholarship_id, name, amount, criteria_list[criteria_id])
    else:
        print(f"Criteria {criteria_id} not found.")
    return scholarships.get(scholarship_id)

# Create/Update Criteria
def create_update_criteria(criteria_id, min_gpa, sport):
    criteria_list[criteria_id] = Criteria(criteria_id, min_gpa, sport)
    return criteria_list[criteria_id]

# Manage Scholarships for Athlete
def manage_athlete_scholarships(athlete_id, scholarship_id):
    athlete = athletes.get(athlete_id)
    scholarship = scholarships.get(scholarship_id)
    
    if athlete and scholarship:
        if scholarship.criteria.is_eligible(athlete): #calls scholarship class
            athlete.add_scholarship(scholarship)
            print(f"Scholarship {scholarship.name} awarded to {athlete.name}.")
        else:
            print(f"{athlete.name} is not eligible for {scholarship.name}.")
    else:
        print("Invalid athlete or scholarship ID.")

# Track/Update Scholarship Criteria
def track_scholarship_criteria(criteria_id):
    return criteria_list.get(criteria_id, "Criteria not found.")

# Test the Program with 4 Sports

# Step 1: Create criteria for 4 different sports
create_update_criteria(1, 3.5, "Football")
create_update_criteria(2, 3.0, "Tennis")
create_update_criteria(3, 2.8, "Cricket")
create_update_criteria(4, 3.2, "Swimming")
create_update_criteria(5, 3.3, "Swimming")

# Step 2: Create athletes for each sport
create_update_athlete(1, "Athlete 1", "Football", 3.6)
create_update_athlete(2, "Athlete 2", "Tennis", 3.1)
create_update_athlete(3, "Athlete 3", "Cricket", 2.7)  # Not eligible for Cricket
create_update_athlete(4, "Athlete 4", "Swimming", 3.0)
create_update_athlete(5, "Sarah", "Swimming", 3.3)


#Step 3: Create scholarships for each sport based on criteria
create_update_scholarship(1, "Football Scholarship", 1500, 1)
create_update_scholarship(2, "Tennis Scholarship", 1200, 2)
create_update_scholarship(3, "Cricket Scholarship", 1000, 3)
create_update_scholarship(4, "Swimming Scholarship", 1300, 4)
create_update_scholarship(5, "Swimming Scholarship", 1300, 5)

# Step 4: Assign scholarships to athletes based on eligibility
manage_athlete_scholarships(1, 1)  # Football athlete eligible
manage_athlete_scholarships(2, 2)  # Tennis athlete eligible
manage_athlete_scholarships(3, 3)  # Cricket athlete not eligible
manage_athlete_scholarships(4, 4)  # Swimming athlete eligible
manage_athlete_scholarships(5, 5)

#unittest

# Track/Update Scholarship Criteria 
def track_scholarship_criteria(criteria_id):
    return criteria_list.get(criteria_id, "Criteria not found.")

# Test Cases: Create and Assign Scholarships (without specific names or sports)
# Step 1: Create criteria (criteria_id, min_gpa, sport)
create_update_criteria(1, 3.0, "Sport A")

# Step 2: Create an athlete (athlete_id, name, sport, gpa)
create_update_athlete(1, "Athlete 1", "Sport A", 3.5)

# Step 3: Create a scholarship linked to the criteria (scholarship_id, name, amount, criteria_id)
create_update_scholarship(1, "Scholarship A", 1000, 1)

# Step 4: Assign scholarship to athlete (athlete_id, scholarship_id)
manage_athlete_scholarships(1, 1)
