import datetime
import traceback
from subclass import Recruiter, Programmer, Candidate, Vacancy, UnableToWorkException


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

    print(worker2.work())
    ###########################
    # # not hired yet except.
    # worker6.work()

    try:
        worker6.work()
    except UnableToWorkException as err:
        print(err)
    finally:
        print('It`s Ok.')
    ################################
    # except. logger

    def main():
        raise ValueError
    try:
        main()
    except Exception as err:
        with open('logs.txt', 'a') as f:
            f.write(str(datetime.datetime.today()) + '\n')
            f.write(type(err).__name__ + '\n')
            f.write(traceback.format_exc() + '\n')
            print('Error was logged!')
    finally:
        print('It`s Ok.')
