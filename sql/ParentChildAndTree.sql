SELECT TREE.ID,
    CASE
        WHEN TREE.ID IS NULL THEN 'ROOT'
        WHEN EXISTS (SELECT T.P_ID FROM TREE AS T WHERE T.P_ID = TREE.ID) THEN 'INNER'
        ELSE 'LEAF'
    END
FROM TREE
ORDER BY TREE.ID;