class Product:
    def __init__(self, id, name, import_price, quantity, storage_fee):
        self.__id = id
        self.__name = name 
        self.__import_price = import_price
        self.__quantity = quantity
        self.__storage_fee = storage_fee
        self.__total_value = 0
        self.__stock_status = ""

        # Tính toán ngay khi khởi tạo
        self.calculate_total_value()
        self.classify_stock_status()
        
    @property
    def id(self): return self.__id

    @property
    def name(self): return self.__name
    
    @property
    def import_price(self): return self.__import_price
    
    @property
    def quantity(self): return self.__quantity
    
    @property
    def storage_fee(self): return self.__storage_fee
    
    @property
    def total_value(self): return self.__total_value
    
    @property
    def stock_status(self): return self.__stock_status
    
    def calculate_total_value(self):
        self.__total_value = (self.__import_price * self.__quantity) + self.__storage_fee
    
    def classify_stock_status(self):
        if self.__total_value < 9000000:
            self.__stock_status = "Thấp(An toàn)"
        elif self.__total_value < 15000000:
            self.__stock_status = "Trung Bình"
        elif self.__total_value < 30000000:
            self.__stock_status = "Cao(Cần chú ý)"
        else:
            self.__stock_status = "Rất cao (Rủi ro ứ đọng vốn)"
    
    def update_info(self, import_price, quantity, storage_fee):
        self.__import_price = import_price
        self.__quantity = quantity
        self.__storage_fee = storage_fee
        self.calculate_total_value()
        self.classify_stock_status()

class ProductManager:
    def __init__(self):
        self.products = []

    def find_by_id(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        return None

    def add_product(self):
        try:
            product_id = input("Nhập mã sản phẩm: ").strip()
            if self.find_by_id(product_id):
                print("Mã sản phẩm đã tồn tại!")
                return
            
            product_name = input("Nhập tên sản phẩm: ").strip()
            import_price = float(input("Nhập giá nhập: "))
            quantity = int(input("Nhập số lượng: "))
            storage_fee = float(input("Nhập chi phí kho: "))

            product = Product(product_id, product_name, import_price, quantity, storage_fee)
            self.products.append(product)
            print("Thêm sản phẩm thành công!")
        except ValueError:
            print("Dữ liệu nhập không hợp lệ!")

    def update_product(self):
        product_id = input("Nhập mã sản phẩm cần cập nhật: ")
        product = self.find_by_id(product_id)
        if not product:
            print("Không tìm thấy sản phẩm!")
            return
        
        try:
            price = float(input("Nhập giá mới: "))
            qty = int(input("Nhập số lượng mới: "))
            fee = float(input("Nhập phí kho mới: "))
            product.update_info(price, qty, fee)
            print("Cập nhật thành công!")
        except ValueError:
            print("Dữ liệu không hợp lệ!")

    def delete_product(self):
        product_id = input("Nhập mã sản phẩm cần xóa: ")
        product = self.find_by_id(product_id)
        if product:
            self.products.remove(product)
            print("Đã xóa sản phẩm!")
        else:
            print("Không tìm thấy sản phẩm!")

    def show_all(self):
        if not self.products:
            print("Danh sách rỗng")
            return
        for p in self.products:
            print(f"Mã: {p.id} | Tên: {p.name} | Tổng giá trị: {p.total_value} | Trạng thái: {p.stock_status}")

    def search_product(self):
        keyword = input("Nhập từ khóa tìm kiếm: ").lower()
        results = [p for p in self.products if keyword == p.id.lower() or keyword in p.name.lower()]
        if not results: print("Không tìm thấy!")
        for p in results: print(f"{p.id} - {p.name} - {p.total_value} - {p.stock_status}")

def main():
    while True:
        header = f" MENU ".center(50, "=")
        user_choice = input(f"""
{header}
1. Hiển thị danh sách sản phẩm trong kho
2. Nhập sản phẩm mới vào kho
3. Cập nhật thông tin sản phẩm
4. Xóa sản phẩm khỏi kho
5. Tìm kiếm sản phẩm theo tên
6. Thoát
{'='*len(header)}
Nhập lựa chọn của bạn (1-6): """)

        match user_choice:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                print("Cảm ơn bạn đã sử dụng hệ thống quản lý kho hàng!")
                break
            case _:
                print("Lựa chọn không hợp lệ vui lòng nhập lại")

if __name__ == "__main__":
    main()
