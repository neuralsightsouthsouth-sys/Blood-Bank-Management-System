class Donor:
    def __init__(self, donor_id, name, blood_type, volume_ml):
        self.donor_id = donor_id
        self.name = name
        self.blood_type = blood_type
        self.volume_ml = volume_ml

    def display_info(self):
        """Prints a summary of the donor."""
        print(f"Donor {self.name} ({self.blood_type}): {self.volume_ml}ml donated.")

    def get_volume(self):
        """Returns the donation volume."""
        return self.volume_ml

class BloodBank:
    def __init__(self, name):
        self.name = name
        self.donors = []

    def add_donor(self, donor):
        """Adds a Donor object to the bank's registry."""
        self.donors.append(donor)
        print(f"Added record for {donor.name} to {self.name}.")

    def get_total_donors(self):
        """Returns the total number of registered donors."""
        return len(self.donors)