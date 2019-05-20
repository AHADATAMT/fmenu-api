from src import db

dish_option = db.Table('dish_option',
                      db.Column('dish_id', db.Integer, db.ForeignKey(
                          'dish.id'), primary_key=True),
                      db.Column('option_id', db.Integer, db.ForeignKey(
                          'option.id'), primary_key=True)
                      )
                      
order_dish = db.Table('order_dish',
                           db.Column('order_id', db.Integer, db.ForeignKey(
                               'order.id'), primary_key=True),
                           db.Column('dish_id', db.Integer, db.ForeignKey(
                               'dish.id'), primary_key=True)
                           )
