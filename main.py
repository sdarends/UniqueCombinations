import combinationGenerator as cg
import jaccardScore as js

if __name__ == '__main__':
    all_combinations = cg.combinationGenerator()
    # js.calculate()
    # now we have the combinations, we want to order them on 'uniqueness'
    # for each item, we will compare it's jaccard similarity score to every other item
    # we will then save the set together with it's score
    # and return the combinations with the lowest score

    print(len(all_combinations))

