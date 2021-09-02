-- Creates a trigger that resets the attribute valid_email only when the email has been changed.
CREATE TRIGGER reset_valid_email_on_email_change BEFORE
UPDATE ON users FOR EACH ROW
    WHEN (OLD.email <> NEW.email) BEGIN
UPDATE users
SET NEW.valid_email = 0
WHERE id = NEW.id;
END;
