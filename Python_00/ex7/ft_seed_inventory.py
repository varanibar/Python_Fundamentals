def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    def unit_converter(quantity, unit):
        if unit == "packets":
            return f"{quantity} packets available"
        if unit == "grams":
            return f"{quantity} grams total"
        if unit == "area":
            return f"covers {quantity} square meters"
        return "Unknown unit type"
    unit_converted = unit_converter(quantity, unit)
    print(f"{seed_type.capitalize()} seeds: {unit_converted}")
