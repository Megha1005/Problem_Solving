# Hackerrank problem
def featuredProduct(products):
    sorted_words=(sorted(products,reverse=True))
    print(sorted_words)
    max_count = max(sorted_words,key=sorted_words.count)    
    return max_count


featuredProduct(['redShirt','greenPants','redShirt','orangeShoes','blackPants','blackPants'])
# Expected outcome = 'redShirt'

featuredProduct(['yellowShirt','redHat','blackShirt','bluePants','redHat','pinkHat','blackShirt','yellowShirt','greenPants','greenPants'])
# Expected outcome = 'yelowShirt'

featuredProduct(['greenShirt','bluePants','redShirt','blackShoes','redPants','redPants','whiteShirt','redShirt'])
# Expected outcome = 'redShirt'

featuredProduct(['a'])
# Expected outcome = 'a'

