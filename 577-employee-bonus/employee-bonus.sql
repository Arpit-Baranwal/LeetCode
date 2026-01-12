# Write your MySQL query statement below
select n.name, b.bonus from Employee as n left join Bonus as b on 
n.empId = b.empId where b.bonus < 1000 or b.bonus is null