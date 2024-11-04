# 1. Create a data structure
trading_list = [{"id":"001", "Order":"Buy","Type":"Add","Price":20.00,"Quantity":100},
                {"id":"002", "Order":"Sell","Type":"Add","Price":25.00,"Quantity":200},
                {"id":"003", "Order":"Buy","Type":"Add","Price":23.00,"Quantity":50},
                {"id":"004", "Order":"Buy","Type":"Add","Price":23.00,"Quantity":70},
                {"id":"003", "Order":"Buy","Type":"Remove","Price":23.00,"Quantity":50},
                {"id":"005", "Order":"Sell","Type":"Add","Price":28.00,"Quantity":100},
                ]

# 2. Implement and and remove operation
def add(order, operation_type, price, quantity):
    #Most of the error validations here
    if order not in ["Buy", "Sell"]:
        return "Only Buy or Sell orders"
    elif operation_type not in ["Add", "Remove"]:
        return "Only Add and Remove operations available"
    elif type(price) != float:
        return "Provide an float for a price"
    elif type(quantity) != int:
        return "Provide an integer for a quantity"
    elif price < 0:
        return "Price cannot be negative"
    elif quantity <= 0:
        return "Quantity cannot be less than or equal 0"
    elif operation_type == "Remove":
        return "Please provide a operation id you wish to remove"

    #find the maximum id and then increment it
    max_id = max(int(trade["id"]) for trade in trading_list)
    new_id = f"{max_id + 1:003}"

   #Actual list operation
    trading_list.append({
        "id":new_id,
        "Order":order,
        "Type":operation_type,
        "Price":price,
        "Quantity":quantity
    })

def remove(id, operation_type):
    if not id.isdigit() or not (1 <= int(id) <= 999):
        return "id must be a string between '001' and '999'"
    elif operation_type not in ["Add", "Remove"]:
        return "Only Add and Remove operations available"

    formatted_id = f"{int(id):03}"

    for trade in trading_list:
        if trade["id"] == formatted_id and trade["Type"] == operation_type:
            trading_list.remove(trade)
        else:
            continue

# 3. Implement an order placing
def place_order(order_type):
    if order_type not in ["Buy", "Sell"]:
        return "Only Buy or Sell orders"

    latest_orders = {}

    # Populate the dictionary with the latest status for each ID
    for order in trading_list:
        latest_orders[order["id"]] = order

    # Filter only the entries where we have add operation
    active_orders = [order for order in latest_orders.values() if order["Type"] == "Add"]
    if not active_orders:
        return "No active Orders available for matching"

    if order_type == "Buy":
        best_sell_orders = [order for order in active_orders if order["Order"] == "Sell"]
        if not best_sell_orders:
            return "No active Sell Orders to match with this Buy order"
        best_sell_order = min(best_sell_orders, key=lambda x: x["Price"])
        return f"Best sell price to buy from: {best_sell_order['Price']}"

    elif order_type == "Sell":
        best_buy_orders = [order for order in active_orders if order["Order"] == "Buy"]
        if not best_buy_orders:
            return "No active Buy Orders to match with this Sell order"
        best_buy_order = max(best_buy_orders, key=lambda x: x["Price"])
        return f"Best sell price to buy from: {best_buy_order['Price']}"

# We can add a new operation to see it the autoincrementation of id works
add("Buy", "Add", 20.00, 500)
# We can add a new operation to sell to see if "place_order" chooses the cheapest order to buy
add("Sell","Add",25.00, 200)
# We can remove the best selling option to ensure that model chooses the second best after removing
remove("007","Add")
print(place_order("Buy"))
#Let's print the list after operations
for ele in trading_list:
    print(ele)

#TODO
# Ensure that the price * quantity is taken under consideration not just one unit price
