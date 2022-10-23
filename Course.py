import copy
class Course:
    graph={}
    in_degree={}
    available_course_codes={}

    def __init__(self,course_code,title,credit):
        self.course_code=course_code
        self.title=title
        self.credit=credit
        self.prerequisites=[]
        Course.available_course_codes[course_code]=1
        Course.in_degree[course_code]=0
        Course.graph[course_code]=[]
    
    def check_cycle(self):
        queue=[]
        degree=copy.deepcopy(Course.in_degree)
        for i in Course.in_degree:
            if Course.in_degree[i]==0:
                queue.append(i)

        while len(queue)!=0:
            u=queue.pop(0)
            for v in Course.graph[u]:
                degree[v]-=1;
                if degree[v]==0:
                    queue.append(v)

        for i in degree:
            if degree[i]!=0:
                return True
        return False

    
    def add_edge(self,u,v):
        Course.in_degree[v]+=1
        Course.graph[u].append(v)

    def remove_edge(self,u,v):
        Course.in_degree[v]-=1
        Course.graph[u].pop()
    
    def add_prerequisite(self,pre_code):
        if pre_code not in Course.available_course_codes:
            return 1
        self.add_edge(pre_code,self.course_code)
        if self.check_cycle()==True:
            self.remove_edge(pre_code,self.course_code)
            return 2
        self.prerequisites.append(pre_code)
        return 3