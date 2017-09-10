SELECT dept_name, COUNT(student_id) as student_number
FROM department
LEFT JOIN student ON student.dept_id = department.dept_id
GROUP BY department.dept_name
ORDER BY student_number DESC, department.dept_name;