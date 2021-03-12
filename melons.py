"""Classes for melon orders."""

#Abastract- init with species, qty, shipped, order- type tax = tax
# def get shipped 

#in our subclass, then we can say tax = 0.08
#order-type- dom/int

class AbstractMelonOrder():
    """An abstract base class"""

    def __init__(self, species, qty, order_type, tax):

        self.species = species
        self.qty = qty
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True



class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    
    
    
    def __init__(self, species, qty):
        super().__init__(species, qty, "Domestic", 0.08)

        #self.order_type = "domestic"
        #self.tax = 0.08



    #     """Initialize melon order attributes."""


    #     self.species = species
    #     self.qty = qty
    #     self.shipped = False
    #     self.order_type = "domestic"
    #     self.tax = 0.08

    # def get_total(self):
    #     """Calculate price, including tax."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price

    #     return total

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""

    #     self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder):

    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty, "Interntional", 0.17) 
        self.country_code = country_code   

        #self.order_type = "international"
        #self.tax = 0.17
        # self.species = species
        # self.qty = qty
        # self.shipped = False
        # self.order_type = "international"
        # self.tax = 0.17

    # def get_total(self):
    #     """Calculate price, including tax."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price

    #     return total

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""

    #     self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
