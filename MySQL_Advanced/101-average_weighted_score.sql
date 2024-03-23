-- Create a stored procedure that computes the average weighted score for each user
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users AS U, 
        (SELECT U.id, SUM(score * weight) / SUM(weight) AS weight_average_score
        FROM users AS U 
        JOIN corrections as C ON U.id=C.user_id 
        JOIN projects AS P ON C.project_id=P.id 
        GROUP BY U.id)
    AS WA
    SET U.average_score = WA.weight_average_score
    WHERE U.id=WA.id;
END //
DELIMITER ;
