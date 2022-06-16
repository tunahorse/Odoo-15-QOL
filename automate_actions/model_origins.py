### Write the sales origin to stock picking/other related moves. 
### Make your own field, and it to the transfer records.


for record in records:
  if record.origin:
    so = env['mrp.production'].search([('name','=',record.origin)])
    if so:
      record.write({"x_sales_order_origin":so.origin})


