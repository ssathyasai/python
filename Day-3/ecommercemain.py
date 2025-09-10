import ecommerceutil
cart={"phone":100,"laptop":200,"fridge":300}
vals=list(cart.values())
sum=0
for i in vals:
    sum+=i
ecommerceutil.generate_invoice(cart)
    
print("---------------------")
print("subtotal:",sum)
p=ecommerceutil.apply_discount(sum,10)
print("After 10 dicount :",p)
q=ecommerceutil.add_gst(sum,18)
print("After 18 gst :",q)
