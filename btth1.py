"""
Hệ Thống Quản Lý Giỏ Hàng SHOPEE
"""

cart_items = [
    {"id": "P001", "name": "Dien thoai iPhone 15", "number": 1, "price": 25000000},
    {"id": "P002", "name": "Op lung Silicon", "number": 2, "price": 150000},
]

while True:
    print(
        "\n====================================================\n"
        "           SHOPEE CART MANAGEMENT SYSTEM\n"
        "====================================================\n"
        "1. Xem chi tiết giỏ hàng & Tính tổng tiền\n"
        "2. Thêm sản phẩm mới / Cộng dồn số lượng\n"
        "3. Cập nhật số lượng của một sản phẩm\n"
        "4. Xóa sản phẩm khỏi giỏ hàng\n"
        "5. Thoát chương trình\n"
        "===================================================="
    )

    choice = input("Mời bạn chọn chức năng (1-5): ")

    match choice:

        # ======= XEM GIỎ HÀNG =======
        case "1":
            print("\n--- CHI TIẾT GIỎ HÀNG ---")
            print(f"{'STT':<5}| {'Mã SP':^6}| {'Tên Sản Phẩm':<25}| {'SL':^3}| {'Đơn giá':<15}| {'Thành tiền':<15}")
            print("-" * 78)

            total_number = 0
            total_price = 0

            for i, item in enumerate(cart_items, start=1):
                thanh_tien = item["number"] * item["price"]
                total_number += item["number"]
                total_price += thanh_tien

                print(
                    f"{i:<5}| "
                    f"{item['id']:^6}| "
                    f"{item['name']:<25}| "
                    f"{item['number']:^3}| "
                    f"{item['price']:,}đ{'':<7}| "
                    f"{thanh_tien:,}đ"
                )

            print("-" * 78)
            print("=> Tổng số lượng:", total_number)
            print(f"=> Tổng tiền thanh toán: {total_price:,}đ")

        # ======= THÊM / CỘNG DỒN =======
        case "2":
            id_sp = input("Mã sản phẩm: ").strip().upper()

            # tìm sản phẩm
            index = next((i for i, item in enumerate(cart_items) if item["id"] == id_sp), -1)

            try:
                quantity = int(input("Số lượng: "))
                if quantity <= 0:
                    print("Số lượng phải > 0")
                    continue
            except ValueError:
                print("Số lượng phải là số nguyên")
                continue

            if index != -1:
                cart_items[index]["number"] += quantity
                print("Đã cộng thêm số lượng sản phẩm.")
            else:
                name = input("Tên sản phẩm: ").strip()

                try:
                    price = int(input("Đơn giá: "))
                    if price <= 0:
                        print("Giá phải > 0")
                        continue
                except ValueError:
                    print("Giá phải là số nguyên")
                    continue

                cart_items.append({
                    "id": id_sp,
                    "name": name,
                    "number": quantity,
                    "price": price
                })
                print("Đã thêm sản phẩm mới.")

        # ======= CẬP NHẬT =======
        case "3":
            update_id = input("Nhập mã sản phẩm cần cập nhật: ").strip().upper()

            product = next((item for item in cart_items if item["id"] == update_id), None)

            if product:
                try:
                    new_qty = int(input("Nhập số lượng mới: "))
                    if new_qty > 0:
                        product["number"] = new_qty
                        print("Cập nhật thành công")
                    else:
                        print("Số lượng phải > 0")
                except ValueError:
                    print("Phải nhập số nguyên")
            else:
                print("Không tìm thấy sản phẩm")

        # ======= XÓA =======
        case "4":
            delete_id = input("Nhập mã sản phẩm muốn xóa: ").strip().upper()

            product = next((item for item in cart_items if item["id"] == delete_id), None)

            if product:
                cart_items.remove(product)
                print("Đã xóa sản phẩm khỏi giỏ hàng")
            else:
                print("Không tìm thấy sản phẩm")

        # ======= THOÁT =======
        case "5":
            print("Đã thoát chương trình")
            break

        case _:
            print("Lựa chọn không hợp lệ (1-5)")
