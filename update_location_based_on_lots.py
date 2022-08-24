#Normal login info here 

######





## Need lot ID
lot = 'insert lot id'

##Amount to update

atu = '1000'



## search for all on hand locations, where the lot is located. 


product_location = models.execute_kw(db, uid, password, 'stock.quant', 'search_read', [['&', ['lot_id', '=', lot],['on_hand','=',True]]])
for i in product_location:

    update_qty = models.execute_kw(db, uid, password, 'stock.quant', 'write', [[product_location[0]['id']], {'available_quantity': atu,'quantity': atu}])
    
    
print('done')

