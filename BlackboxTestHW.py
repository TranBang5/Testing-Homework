def calculate_shipping_fee(order_value: int, distance: int) -> int:
    # Kiểm tra đầu vào hợp lệ
    if order_value < 0 or order_value > 5000000:
        raise ValueError("Giá đơn hàng không hợp lệ (0 - 5.000.000 VND)")
    if distance <= 0 or distance > 100:
        raise ValueError("Khoảng cách giao hàng không hợp lệ (0 - 100 km)")
    
    # Xác định phí vận chuyển cơ bản
    base_shipping_fee = 20000 if distance < 10 else 30000
    
    # Xác định mức giảm giá vận chuyển
    if order_value < 100000:
        discount = 0  # Không giảm giá
    elif order_value <= 500000:
        discount = 0.3  # Giảm 30%
    else:
        discount = 0.5  # Giảm 50%
    
    # Tính toán phí vận chuyển cuối cùng
    final_shipping_fee = int(base_shipping_fee * (1 - discount))
    return final_shipping_fee

if __name__ == "__main__":
    # Kiểm thử theo dòng điều khiển
    test_cases_flow = [
        # Kiểm thử biên theo Giá trị đơn hàng
        (-1, 1),          # Lỗi
        (1, -1),          # Lỗi
        (50000, 5),    # 20.000 VND
        (50000, 10),    # 30.000 VND
        (100000, 5),    # 14.000 VND
        (600000, 5),    # 10.000 VND
    ]
 
    print("Flow Chart Testing")
    for order_value, distance in test_cases_flow:
        try:
            fee = calculate_shipping_fee(order_value, distance)
            print(f"Order: {order_value} VND, Distance: {distance} km -> Shipping Fee: {fee} VND")
        except ValueError as e:
            print(f"Error: {e}")
