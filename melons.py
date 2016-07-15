"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """Parent class, to help with repetitive code"""
    #include all the parameters that will be used by the subclasses
    def __init__(self, species, qty, order_type, tax, country_code=None):
        """Initialize melon order class attributes"""
        #Define all the attributes needed
        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price."""

        base_price = 5
        if self.species == 'Christmas Melon':
            base_price = base_price * 1.5

        total = ((1 + self.tax) * self.qty * base_price)
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True



class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        #Include all arguments in exact order, if default values enter directly
        super (DomesticMelonOrder, self). __init__(species, qty, "domestic", 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""
        super(InternationalMelonOrder, self).__init__(species, qty, "international", 0.17, country_code)

    def get_total(self):
        """Calculate total price"""

        base_price = 5
        if self.species == 'Christmas Melon':
            base_price = base_price * 1.5

        flat_fee = 0
        if self.qty < 10:
            flat_fee = 3

        total = ((1 + self.tax) * self.qty * base_price) + flat_fee
        return total

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """for government orders and security inspection"""

    def __init__(self, species, qty):

        super(GovernmentMelonOrder, self).__init__(species, qty, "domestic", 0)
        self.passed_inspection = False

    def mark_passed(self):
        self.passed_inspection = True
