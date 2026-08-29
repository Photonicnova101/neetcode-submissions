class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        rounds=0
        while rounds<len(students):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                rounds=0
            else:
                students.append(students.pop(0))
                rounds+=1
        return len(students)