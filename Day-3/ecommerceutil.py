def apply_discount(price, dis_per):
    dic_price = price - (price * dis_per / 100) 
    return dic_price

def add_gst(price, gst_price=18):
    new_price = price + (price * gst_price / 100) 
    return new_price                              

def generate_invoice(cart):
    print("------------INVOICE----------")
    for i, j in cart.items():
        print(i, "               ", j)
