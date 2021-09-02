-- Creates a trigger that resets the attribute valid_email only when the email has been changed.
CREATE TRIGGER reset_valid_email_on_email_change BEFORE
UPDATE ON users FOR EACH ROW IF (OLD.email != NEW.email)
UPDATE users
SET valid_email = 0
WHERE id = NEW.id;
END IF;
