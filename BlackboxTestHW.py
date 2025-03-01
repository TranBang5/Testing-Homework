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

# Kiểm thử biên
if __name__ == "__main__":
    # Kiểm thử theo bảng quyết định
    test_cases_table = [
        (-1, 5),          # Lỗi
        (50000, -1),      # Lỗi
        (50000, 5),       # 20.000 VND
        (50000, 10),      # 30.000 VND
        (50000, 101),     # Lỗi
        (300000, 5),      # 14.000 VND
        (300000, 10),     # 21.000 VND
        (600000, 5),      # 10.000 VND
        (600000, 10),     # 15.000 VND
        (6000000, 5),     # Lỗi
    ]

    # Kiểm thử theo biên
    test_cases_boundary = [
        # Kiểm thử biên theo Giá trị đơn hàng
        (-1, 50),          # Lỗi
        (0, 50),          # Lỗi
        (1, 50),          # 30.000 VND
        (4999999, 50),    # 15.000 VND
        (5000000, 50),    # 15.000 VND
        (5000001, 50),    # Lỗi
        (2500000, 50),    # 15.000 VND
        
        # Kiểm thử biên theo Khoảng cách
        (2500000, -1),     # Lỗi
        (2500000, 0),      # 15.000 VND
        (2500000, 1),      # 15.000 VND
        (2500000, 99),     # 21.000 VND
        (2500000, 100),    # 21.000 VND
        (2500000, 101),     # 21.000 VND
    ]

    print("Table Testing")
    for order_value, distance in test_cases_table:
        try:
            fee = calculate_shipping_fee(order_value, distance)
            print(f"Order: {order_value} VND, Distance: {distance} km -> Shipping Fee: {fee} VND")
        except ValueError as e:
            print(f"Error: {e}")
    
    print("Boundary Testing")
    for order_value, distance in test_cases_boundary:
        try:
            fee = calculate_shipping_fee(order_value, distance)
            print(f"Order: {order_value} VND, Distance: {distance} km -> Shipping Fee: {fee} VND")
        except ValueError as e:
            print(f"Error: {e}")
