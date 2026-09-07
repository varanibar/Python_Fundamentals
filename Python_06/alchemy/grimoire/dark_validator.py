from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients = dark_spell_allowed_ingredients()

    for allowed in allowed_ingredients:
        if allowed in ingredients.lower():
            return "VALID"
    else:
        return "INVALID"
