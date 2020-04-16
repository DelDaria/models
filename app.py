from subclass import Recruiter, Programmer, Candidate, Vacancy

if __name__ == '__main__':
    worker1 = Recruiter('Stan', 'Stanson', 'ss@gmail.com', 200, 3)
    print(worker1)
    worker2 = Programmer('Nick', 'Nickson', 'nn@gmail.com', 300, 2)
    print(worker2)
    worker3 = Programmer('Jack', 'Jackson', 'jjj@gmail.com', 350, 33)
    print(worker3)

    worker4 = Candidate('Thom', 'Thomson', 'fff@gmail.com', 0, ['t1', 't2', 't3'], 't2', 3)
    print(worker4)
    worker5 = Candidate('Alex', 'Black', 'aaa@gmail.com', 0, ['t4', 't5', 't1'], 't1', 5)
    print(worker5)
    worker6 = Candidate('Max', 'White', 'mmm@gmail.com', 0, ['t6', 't3', 't1'], 't3', 4)
    print(worker6)

    vacancy1 = Vacancy('V1', 't2', 2)
    vacancy2 = Vacancy('V2', 't3', 3)
    print(vacancy1)
