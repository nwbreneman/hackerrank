def birthdayCakeCandles(ar):

    candles = {}
    largest_candle = float("-inf")

    for candle in ar:
        largest_candle = max(largest_candle, candle)
        if candle not in candles:
            candles[candle] = 0
        candles[candle] += 1

    return candles[largest_candle]

