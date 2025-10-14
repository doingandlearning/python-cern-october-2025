import math

def calculate_ph(hydrogen_ion_concentration, does_not_exist):
    """
    Calculates the ph from the hydrogen ion concentration
    :param hydrogen_ion_concentration: Will be a decimal
    :param does_not_exist: Does not exist
    :return: The ph which will be a float
    """
    ph = -math.log10(hydrogen_ion_concentration)
    return ph

calculate_ph()

print()