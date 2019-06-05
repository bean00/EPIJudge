from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    return sort_then_loop_through(prices)


def sort_then_loop_through(prices):
    price_and_index = []

    for i, price in list(enumerate(prices)):
        price_and_index.append((price, i))

    price_and_index.sort()
    print(price_and_index)

    # price index: index for each price from unsorted array
    # position index: index for each position in sorted array
    # start_...: start index at beginning of nested while loop
    # current_...: current index in while loop
    start_pos_index = 0
    max_i = len(price_and_index) - 1
    discovered_indices = set()
    max_profit = 0

    while start_pos_index <= len(price_and_index) - 2:
        print(f'start_pos_index: {start_pos_index}')
        start_price = price_and_index[start_pos_index][0]
        start_price_index = price_and_index[start_pos_index][1]
        j = start_pos_index
        to_visit = set()
        for k in range(start_price_index + 1, max_i + 1):
            if k not in discovered_indices:
                to_visit.add(k)

        while to_visit and (j <= len(price_and_index) - 2):
            j += 1
            curr_price = price_and_index[j][0]
            curr_price_index = price_and_index[j][1]
            if curr_price_index <= start_price_index:
                continue

            print(f'to_visit: {to_visit}')
            profit = curr_price - start_price
            print(f'j: {j}, profit: {profit}')
            max_profit = profit if profit > max_profit else max_profit
            print(f'max_profit: {max_profit}')

            discovered_indices.add(curr_price_index)
            if curr_price_index in to_visit:
                to_visit.remove(curr_price_index)

        max_i = start_price_index - 1
        start_pos_index = j + 1

    return max_profit


if __name__ == '__main__':
    # exit(
    #     generic_test.generic_test_main("buy_and_sell_stock.py",
    #                                    "buy_and_sell_stock.tsv",
    #                                    buy_and_sell_stock_once))

    prices = [3, 5, 2, 6, 3, 4]
    # prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
    # prices = [0.2, 2.9, 1.3, 3.3, 1.1, 1.0, 0.3, 2.4, 2.8, 0.6, 2.4, 3.1, 1.3, 2.7, 0.6, 1.2, 1.2, 1.6, 1.0, 1.5, 2.8, 2.5, 3.1,
    #  1.9, 1.2, 1.2, 1.1, 3.3, 2.3, 0.8, 2.8, 2.2, 0.1, 1.0, 2.2]
    print(buy_and_sell_stock_once(prices))
