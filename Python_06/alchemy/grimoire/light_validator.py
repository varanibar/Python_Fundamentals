from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients = light_spell_allowed_ingredients()

    for allowed in allowed_ingredients:
        if allowed in ingredients.lower():
            return "VALID"
    else:
        return "INVALID"
