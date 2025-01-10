def cakes(recipe, available):
    
    max_cakes = 10000000

    for key in recipe:
        if key in available:
            max_cakes = min(max_cakes, available[key] // recipe[key])
        
        else:
            return 0
        
    return max_cakes
