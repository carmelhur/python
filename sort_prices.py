def sort_prices(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: float(x[1]), reverse=True)
