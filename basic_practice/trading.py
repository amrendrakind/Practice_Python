employee_id = -1
while(employee_id != "-1"):
    employee_id = str(input("Enter Employee ID "))
    if (employee_id != "-1"):
        sum_trade_value = 0
        trade_value = 1
        while(trade_value != 0):
            trade_value = int(input("Enter trade value "))
            sum_trade_value += trade_value
        print(f'Total trading profit/loss for {employee_id} is',sum_trade_value)
    else:
        break
