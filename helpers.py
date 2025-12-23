from typing import List

def check_bun_names(buns, expected_bun_names: List[str]) -> bool:
    return len(buns) == len(expected_bun_names) and all(
        bun.get_name() == expected_name for bun, expected_name in zip(buns, expected_bun_names)
    )

def check_ingredient_names(ingredients, expected_ingredient_names: List[str]) -> bool:
    return len(ingredients) == len(expected_ingredient_names) and all(
        ingredient.get_name() == expected_name for ingredient, expected_name in zip(ingredients, expected_ingredient_names)
    )