-- Creates a stored procedure AddBonus that adds a new correction for a student.
-- AddBonus takes following three inputs:
-- user_id: a users.id value
-- project_name: a new or already existing project name. If no projects.name found in table, create it
-- score: the score value for the new correction
DELIMITER $$
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    SET @project_id = (SELECT projects.id FROM projects WHERE projects.name = project_name);
    IF @project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET @project_id = LAST_INSERT_ID();
    END IF;
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, @project_id, score);
END$$
DELIMITER ;
