-- Creates a trigger that decreases the quantity of an item after adding a new order.
-- Quantity in the table items can be negative.
CREATE TRIGGER decrease_quantity_after_add_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items SET quantity = quantity - NEW.number WHERE items.name = NEW.item_name;
END;
