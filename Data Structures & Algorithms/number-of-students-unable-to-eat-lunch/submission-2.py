class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        #what are the bottlenecks
        #keep iterating til we see a sandwhich that wouldn't be taken because there are no more students with that preference

        q = deque()
        for i in range(len(students)):
            q.append(students[i])
        
        s_count = Counter(students)
        print(s_count)
        print(s_count[0])
        count=0
        while students and sandwiches:

            if students[0]==sandwiches[0]:
                q.popleft()
                to_pop = students.pop(0)
                s_count[to_pop]-=1
                sandwiches.pop(0)
            elif s_count[sandwiches[0]]==0:
                count+=len(students)
                break
            elif students[0]!=sandwiches[0]:
                to_pop = students.pop(0)
                q.append(to_pop)
                students.append(to_pop)
        
        return count

