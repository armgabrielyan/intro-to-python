market = {
  'dairy': ['yogurt', 'cheese'],
  'fruits': ['banana', 'apple', 'orange', 'lemon', 'apple', 'banana', 'banana'],
}

market_updated = market.copy()
market_updated['candies'] = ['mars', 'kinder', 'twix']
market_updated['fruits'] = sorted(list(set(market_updated['fruits'])))

print('Before:', market)
print('After:', market_updated)
