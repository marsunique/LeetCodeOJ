SELECT TREE.ID,
    CASE
        WHEN TREE.P_ID IS NULL THEN 'ROOT'
        WHEN EXISTS (SELECT T.P_ID FROM TREE AS T WHERE T.P_ID = TREE.ID) THEN 'INNER'
        ELSE 'LEAF'
    END
FROM TREE
ORDER BY TREE.ID;


# Leetcode
# Write your MySQL query statement below
SELECT id,
    CASE
        WHEN p_id IS null THEN 'Root'
        WHEN tree.id IN (SELECT t.p_id FROM tree AS t) THEN 'Inner'
        ELSE 'Leaf'
    END as Type
FROM tree
ORDER BY tree.id;