from decimal import Decimal

LENGTH_UNITS = {
    # Imperial
    "inch": {"factor": Decimal("0.0254")},
    "feet": {"factor": Decimal("0.3048")},
    "yard": {"factor": Decimal("0.9144")},
    "mile": {"factor": Decimal("1609.344")},

    # Metric (cringe)
    "terameter": {"factor": Decimal("1e12")},
    "gigameter": {"factor": Decimal("1e9")},
    "megameter": {"factor": Decimal("1e6")},
    "kilometer": {"factor": Decimal("1000")},
    "hectometer": {"factor": Decimal("100")},
    "decameter": {"factor": Decimal("10")},
    "meter": {"factor": Decimal("1")},
    "decimeter": {"factor": Decimal("0.1")},
    "centimeter": {"factor": Decimal("0.01")},
    "millimeter": {"factor": Decimal("0.001")},
    "micrometer": {"factor": Decimal("1e-6")},
    "nanometer": {"factor": Decimal("1e-9")},
    "picometer": {"factor": Decimal("1e-12")},
    "femtometer": {"factor": Decimal("1e-15")},
    "attometer": {"factor": Decimal("1e-18")},

    # jokes *tee hee*
    "lightyear": {"factor": Decimal("9460700000000000")},
    "freedom_unit": {"factor": 1776},
}


def convert_distance_bruh(value, source, computed):
    print(value, source, computed)

    unit_of_measure = Decimal(value) * LENGTH_UNITS[source]["factor"]
    result = unit_of_measure / LENGTH_UNITS[computed]["factor"]

    return result


TEMPERATURE_UNITS = {

    "kelvin": {
        "to_kelvin": lambda k: Decimal(k),
        "from_kelvin": lambda k: Decimal(k),
    },
    "celsius": {
        "to_kelvin": lambda c: Decimal(c) + Decimal("273.15"),
        "from_kelvin": lambda k: Decimal(k) - Decimal("273.15"),
    },
    "fahrenheit": {
        "to_kelvin": lambda f: (Decimal(f) - Decimal("32")) * Decimal("5") / Decimal("9") + Decimal("273.15"),
        "from_kelvin": lambda k: (Decimal(k) - Decimal("273.15")) * Decimal("9") / Decimal("5") + Decimal("32"),
    },
    "rankine": {
        "to_kelvin": lambda r: Decimal(r) * Decimal("5") / Decimal("9"),
        "from_kelvin": lambda k: Decimal(k) * Decimal("9") / Decimal("5"),
    },
}

def convert_temperature_bruh(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    k = TEMPERATURE_UNITS[from_unit]["to_kelvin"](value)

    return TEMPERATURE_UNITS[to_unit]["from_kelvin"](k)


VOLUME_UNITS = {
    # Imperial
    "teaspoon": {"factor": Decimal("0.00492892")},
    "tablespoon": {"factor": Decimal("0.0147868")},
    "fluid_ounce": {"factor": Decimal("0.0295735")},
    "cup": {"factor": Decimal("0.24")},
    "pint": {"factor": Decimal("0.473176")},
    "quart": {"factor": Decimal("0.946353")},
    "gallon": {"factor": Decimal("3.78541")},
    "barrel": {"factor": Decimal("119.240471")},

    # Metric
    "milliliter": {"factor": Decimal("0.001")},
    "centiliter": {"factor": Decimal("0.01")},
    "deciliter": {"factor": Decimal("0.1")},
    "liter": {"factor": Decimal("1")},
    "decaliter": {"factor": Decimal("10")},
    "hectoliter": {"factor": Decimal("100")},
    "kiloliter": {"factor": Decimal("1000")},
}


def convert_volume_bruh(value, from_unit, to_unit):

    value = Decimal(str(value))
    liters = value * VOLUME_UNITS[from_unit]["factor"]
    result = liters / VOLUME_UNITS[to_unit]["factor"]

    return result


