"""Classes for melon orders."""


class AbstractMelonOrder():
    """An abstract base class"""
    # passing  common arguments between Domestic and International sub classes

    def __init__(self, species, qty, order_type, tax):

        self.species = species
        self.qty = qty
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        
        if self.species == "Christmas melons":
            total = total * 1.5 
        
        if self.order_type == "International" and self.qty < 10:
            total = total + 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class GovernmentMelonOrder(AbstractMelonOrder):
    """Government Melon Information"""
    # Gorvnment will not pay tax 
    
    def __init__(self, species, qty):
        super().__init__(species, qty, "Government", 0.0)

    passed_inspection = False

    def mark_inspection(self):   
        self.passed_inspection = True



class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    # we are inhereting 
    def __init__(self, species, qty):

        # we are inherting __init__ from Abstract class
        super().__init__(species, qty, "Domestic", 0.08)




class InternationalMelonOrder(AbstractMelonOrder):

    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty, "Interntional", 0.17) 
        self.country_code = country_code   

  

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
