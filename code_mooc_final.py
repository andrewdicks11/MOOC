import sqlite3
from sqlite3 import Error
import unittest
 
DATABASE = "MOOC_dos.db"


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    db_file = DATABASE
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None


class Class:

    # percent of students that received certification
    def get_certified(conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM Test_Activity_Results WHERE certificate_eligible == 'Y'")
        certified = cur.fetchall()

        cur.execute("SELECT * FROM Test_Activity_Results")
        total = cur.fetchall()

        return len(certified) / len(total)

    # number of students
    # returns a list of tuples
    def get_students(conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM Test_Activity_Results")
        students = cur.fetchall()

        return students

    # number of students that passed
    # returns a list of tuples
    def get_passed(conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM Test_Activity_Results WHERE grade >= 0.5")
        passed = cur.fetchall()

        return passed

    # number of students that failed
    # returns a list of tuples
    def get_failed(conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM Test_Activity_Results WHERE grade > 0.0 and grade < 0.5")
        failed = cur.fetchall()

        return failed

    # number of students incomplete
    # returns a list of tuples
    def get_incomplete(conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM Test_Activity_Results WHERE grade == 0.0")
        incomplete = cur.fetchall()

        return incomplete


class Average:

    def get_class_avg(conn,lst_of_tuples):
        students = lst_of_tuples

        grades = []
        for s in students:
            grades.append(s[3])

        return round((sum(grades)/len(students)),2)

    def get_class_tests_avgs(conn):
        cur = conn.cursor()
        cur.execute("SELECT test_unit1, test_unit2, test_unit3, test_unit4 FROM Test_Activity_Results")
        tests = cur.fetchall()

        # convert 'Not Attempted' to float 0.0
        tests_lst = []
        for test in tests:
            test_lst = []
            for t in test:
                if t == 'Not Attempted':
                    t = '0.0'
                try:
                    test_lst.append(float(t))
                except:
                    test_lst.append(t)
            tests_lst.append(test_lst)

        t1 = []
        t2 = []
        t3 = []
        t4 = []
        for t in tests_lst:
            t1.append(t[0])
            t2.append(t[1])
            t3.append(t[2])
            t4.append(t[3])

        t1_avg = sum(t1)/len(t1)
        t2_avg = sum(t2)/len(t2)
        t3_avg = sum(t3)/len(t3)
        t4_avg = sum(t4)/len(t4)
        tests_avg = sum([t1_avg, t2_avg, t3_avg, t4_avg])/4

        tests_avgs = {"tests":tests_avg, "t1":round(t1_avg,2), "t2":round(t2_avg,2), "t3":round(t3_avg,2), "t4":round(t4_avg,2)}

        return tests_avgs

    def get_class_activities_avgs(conn):
        cur = conn.cursor()
        cur.execute("SELECT activity_unit1, activity_unit2, activity_unit3 FROM Test_Activity_Results")
        activities = cur.fetchall()

        # convert 'Not Attempted' to float 0.0 (list of lists)
        activities_lst = []
        for activity in activities:
            activity_lst = []
            for a in activity:
                if a == 'Not Attempted':
                    a = '0.0'
                try:
                    activity_lst.append(float(a))
                except:
                    activity_lst.append(a)
            activities_lst.append(activity_lst)

        a1 = []
        a2 = []
        a3 = []
        for a in activities_lst:
            a1.append(a[0])
            a2.append(a[1])
            a3.append(a[2])

        a1_avg = sum(a1)/len(a1)
        a2_avg = sum(a2)/len(a2)
        a3_avg = sum(a3)/len(a3)
        activities_avg = sum([a1_avg, a2_avg, a3_avg])/3

        activities_avgs = {"activities":activities_avg, "a1":round(a1_avg,2), "a2":round(a2_avg,2), "a3":round(a3_avg,2)}

        return activities_avgs


# the sum of grades for a list of tuples of student data
# returns a float
def get_grade_total(conn,lst_of_tuples):
    students = lst_of_tuples

    lst_of_grades = []
    for s in students:
        lst_of_grades.append(s[3])
    
    return sum(lst_of_grades)


# grade distributions for Tests and Activities
# returns a string showing the scores received and the num students that received that grade
# writes data to a csv file
class Tests:

    def get_unit1(conn):
        cur = conn.cursor()
        cur.execute("SELECT test_unit1 FROM Test_Activity_Results")
        t1 = cur.fetchall()
        
        test_unit1 = {}
        for student in t1:
            grade = student[0]
            test_unit1[grade] = test_unit1.get(grade, 0) + 1
        # print("Test Unit 1")
        # print("-----------")
        
        test1 = []
        # ft1 = open('test_unit1.csv', 'w')
        for t in sorted(test_unit1, reverse=True):
            test1.append(t + ": " + str(test_unit1[t]))
            # ft1.write(t + ',' + str(test_unit1[t])+ ',\n')
        # ft1.close()
        return test1

    def get_unit2(conn):
        cur = conn.cursor()
        cur.execute("SELECT test_unit2 FROM Test_Activity_Results")
        t2 = cur.fetchall()

        test_unit2 = {}
        for student in t2:
            grade = student[0]
            test_unit2[grade] = test_unit2.get(grade, 0) + 1
        # print("Test Unit 1")
        # print("-----------")
        
        test2 = []
        # ft1 = open('test_unit1.csv', 'w')
        for t in sorted(test_unit2, reverse=True):
            test2.append(t + ": " + str(test_unit2[t]))
            # ft1.write(t + ',' + str(test_unit1[t])+ ',\n')
        # ft1.close()
        return test2

    def get_unit3(conn):
        cur = conn.cursor()
        cur.execute("SELECT test_unit3 FROM Test_Activity_Results")
        t3 = cur.fetchall()

        test_unit3 = {}
        for student in t3:
            grade = student[0]
            test_unit3[grade] = test_unit3.get(grade, 0) + 1
        # print("Test Unit 1")
        # print("-----------")
        
        test3 = []
        # ft1 = open('test_unit1.csv', 'w')
        for t in sorted(test_unit3, reverse=True):
            test3.append(t + ": " + str(test_unit3[t]))
            # ft1.write(t + ',' + str(test_unit1[t])+ ',\n')
        # ft1.close()
        return test3

    def get_unit4(conn):
        cur = conn.cursor()
        cur.execute("SELECT test_unit4 FROM Test_Activity_Results")
        t4 = cur.fetchall()

        test_unit4 = {}
        for student in t4:
            grade = student[0]
            test_unit4[grade] = test_unit4.get(grade, 0) + 1
        # print("Test Unit 1")
        # print("-----------")
        
        test4 = []
        # ft1 = open('test_unit1.csv', 'w')
        for t in sorted(test_unit4, reverse=True):
            test4.append(t + ": " + str(test_unit4[t]))
            # ft1.write(t + ',' + str(test_unit1[t])+ ',\n')
        # ft1.close()
        return test4

class Activities:

    def get_unit1(conn):
        cur = conn.cursor()
        cur.execute("SELECT activity_unit1 FROM Test_Activity_Results")
        a1 = cur.fetchall()

        activity_unit1 = {}
        for student in a1:
            grade = student[0]
            activity_unit1[grade] = activity_unit1.get(grade, 0) + 1
        # print("Activity Unit 1")
        # print("---------------")

        activity1 = []
        # fa1 = open('activity_unit1.csv', 'w')
        for a in sorted(activity_unit1, reverse=True):
            activity1.append(a + ": " + str(activity_unit1[a]))
        #     fa1.write(a + ',' + str(activity_unit1[a])+ ',\n')
        # fa1.close()
        return activity1

    def get_unit2(conn):
        cur = conn.cursor()
        cur.execute("SELECT activity_unit2 FROM Test_Activity_Results")
        a2 = cur.fetchall()

        activity_unit2 = {}
        for student in a2:
            grade = student[0]
            activity_unit2[grade] = activity_unit2.get(grade, 0) + 1
        # print("Activity Unit 1")
        # print("---------------")

        activity2 = []
        # fa1 = open('activity_unit1.csv', 'w')
        for a in sorted(activity_unit2, reverse=True):
            activity2.append(a + ": " + str(activity_unit2[a]))
        #     fa1.write(a + ',' + str(activity_unit1[a])+ ',\n')
        # fa1.close()
        return activity2

    def get_unit3(conn):
        cur = conn.cursor()
        cur.execute("SELECT activity_unit3 FROM Test_Activity_Results")
        a3 = cur.fetchall()

        activity_unit3 = {}
        for student in a3:
            grade = student[0]
            activity_unit3[grade] = activity_unit3.get(grade, 0) + 1
        # print("Activity Unit 1")
        # print("---------------")

        activity3 = []
        # fa1 = open('activity_unit1.csv', 'w')
        for a in sorted(activity_unit3, reverse=True):
            activity3.append(a + ": " + str(activity_unit3[a]))
        #     fa1.write(a + ',' + str(activity_unit1[a])+ ',\n')
        # fa1.close()
        return activity3


class Student:

    def get_usernames(conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM Test_Activity_Results")
        tar = cur.fetchall()
        
        # list of usernames
        users = []
        for user in tar:
            users.append(user[2])

        return users

    # student data
    # returns a tuple of all Test/Activity data for one student
    def get_student_data(conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM Test_Activity_Results")
        tar = cur.fetchall()
        
        # list of usernames
        users = []
        for user in tar:
            users.append(user[2])

        # enter username, if username in list of usernames, get username data from tar and save as student
        student = ()
        while True:
            username = input("Enter student username: ")
            if username in users:
                location = users.index(username)
                student = tar[location]
                break
            else:
                print(username + " not found")
                continue
        
        return student

    def get_student(conn, username):
        cur = conn.cursor()
        cur.execute("SELECT * FROM Test_Activity_Results")
        tar = cur.fetchall()
        
        # list of usernames
        users = []
        for user in tar:
            users.append(user[2])

        # enter username, if username in list of usernames, get username data from tar and save as student
        student = ()
        while True:
            if username in users:
                location = users.index(username)
                student = tar[location]
                break
            else:
                return "Wut."
                continue
        
        return student

    # individual test results
    # returns list of strings - [username, t1, t2, t3, t4]
    def get_tests(conn,username):
        cur = conn.cursor()
        cur.execute("SELECT username, test_unit1, test_unit2, test_unit3, test_unit4 FROM Test_Activity_Results")
        tests = cur.fetchall()

        # convert 'Not Attempted' to float 0.0
        tests_lst = []
        for test in tests:
            test_lst = []
            for t in test:
                if t == 'Not Attempted':
                    t = '0.0'
                try:
                    test_lst.append(float(t))
                except:
                    test_lst.append(t)
            tests_lst.append(test_lst)

        users = []
        u = []
        for user in tests_lst:
            users.append(user[0])
        while username:
            if username in users:
                location = users.index(username)
                u = tests_lst[location]
                break
            else:
                print(username + " not found")
                username = input("Enter student username: ")
                continue

        return u

    # individual activity results
    # returns list of strings - [username, a1, a2, a3]
    def get_activities(conn,username):
        cur = conn.cursor()
        cur.execute("SELECT username, activity_unit1, activity_unit2, activity_unit3 FROM Test_Activity_Results")
        activities = cur.fetchall()

        # convert 'Not Attempted' to float 0.0 (list of lists)
        activities_lst = []
        for activity in activities:
            activity_lst = []
            for a in activity:
                if a == 'Not Attempted':
                    a = '0.0'
                try:
                    activity_lst.append(float(a))
                except:
                    activity_lst.append(a)
            activities_lst.append(activity_lst)

        # list of usernames
        users = []
        for user in activities_lst:
            users.append(user[0])

        # if username in list of usernames
        u = []
        while username:
            if username in users:
                location = users.index(username)
                u = activities_lst[location]
                break
            else:
                print(username + " not found")
                username = input("Enter student username: ")
                continue
        
        return u


class Spanish:

    def get_students(conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM Test_Activity_Results WHERE cohort_name == 'Spanish'")
        spanish = cur.fetchall()
        
        return spanish

    def get_passed(conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM Test_Activity_Results WHERE grade >= 0.5 and cohort_name == 'Spanish'")
        spanish_pass = cur.fetchall()

        return spanish_pass

    def get_failed(conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM Test_Activity_Results WHERE grade > 0 and grade < 0.5 and cohort_name == 'Spanish'")
        spanish_fail = cur.fetchall()

        return spanish_fail

    def get_incomplete(conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM Test_Activity_Results WHERE grade == 0 and cohort_name == 'Spanish'")
        spanish_incomplete = cur.fetchall()

        return spanish_incomplete

class English:

    def get_students(conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM Test_Activity_Results WHERE cohort_name == 'English'")
        english = cur.fetchall()

        return english

    def get_passed(conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM Test_Activity_Results WHERE grade >= 0.5 and cohort_name == 'English'")
        english_pass = cur.fetchall()

        return english_pass

    def get_failed(conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM Test_Activity_Results WHERE grade > 0 and grade < 0.5 and cohort_name == 'English'")
        english_fail = cur.fetchall()

        return english_fail

    def get_incomplete(conn):
        cur = conn.cursor()
        cur.execute("SELECT * FROM Test_Activity_Results WHERE grade == 0 and cohort_name == 'English'")
        english_incomplete = cur.fetchall()

        return english_incomplete


class Stats:

    def num_students():
        database = "MOOC_dos.db"
        conn = create_connection(database)
        total_students = len(Class.get_students(conn))
        return total_students

    def num_passed():
        database = "MOOC_dos.db"
        conn = create_connection(database)
        students_passed = len(Class.get_passed(conn))
        total_students = len(Class.get_students(conn))
        percentage = str(round((students_passed/total_students)*100, 2))
        return students_passed, total_students, percentage

    def num_failed():
        database = "MOOC_dos.db"
        conn = create_connection(database)
        students_failed = len(Class.get_failed(conn))
        total_students = len(Class.get_students(conn))
        percentage = str(round((students_failed/total_students)*100, 2))
        return students_failed, total_students, percentage

    def num_incomplete():
        database = "MOOC_dos.db"
        conn = create_connection(database)
        students_incomplete = len(Class.get_incomplete(conn))
        total_students = len(Class.get_students(conn))
        percentage = str(round((students_incomplete/total_students)*100, 2))
        return students_incomplete, total_students, percentage

    def class_avg():
        database = "MOOC_dos.db"
        conn = create_connection(database)
        students = Class.get_students(conn)
        class_avg = Average.get_class_avg(conn,students)
        return class_avg

    def pass_avg():
        database = "MOOC_dos.db"
        conn = create_connection(database)
        students_passed = Class.get_passed(conn)
        grade_total = get_grade_total(conn,students_passed)
        return round(grade_total/len(students_passed),2)

    def pf_avg():
        database = "MOOC_dos.db"
        conn = create_connection(database)

        students_passed = Class.get_passed(conn)
        students_failed = Class.get_failed(conn)
        students_completed = len(students_passed) + len(students_failed)

        grade_total_passed = get_grade_total(conn,students_passed)
        grade_total_failed = get_grade_total(conn,students_failed)
        grade_total = grade_total_passed + grade_total_failed

        return round(grade_total/students_completed,2)

    def users():
        database = "MOOC_dos.db"
        conn = create_connection(database)
        users = Student.get_usernames(conn)
        return users

    def get_tests(username):
        database = "MOOC_dos.db"
        conn = create_connection(database)
        u = Student.get_tests(conn,username)
        return u

    def get_activities(username):
        database = "MOOC_dos.db"
        conn = create_connection(database)
        u = Student.get_activities(conn,username)
        return u

    def get_student_class_comp(username):
        database = "MOOC_dos.db"
        conn = create_connection(database)

        user = Student.get_student(conn,username)
        tests = Student.get_tests(conn,username)[1:]
        activities = Student.get_activities(conn,username)[1:]
        student_output = "<b><u>" + username + "</u></b><br/>Grade: " + str(user[3]) + "<br/>Test Average: " + str(round((sum(tests)/len(tests)),2)) + "<br/>T1: " + str(tests[0]) + ", T2: " + str(tests[1]) + ", T3: " + str(tests[2]) + ", T4: " + str(tests[3]) + "<br/>Activity Average: " + str(round((sum(activities)/len(activities)),2)) + "<br/>A1: " + str(activities[0]) + ", A2: " + str(activities[1]) + ", A3: " + str(activities[2])
        
        students = Class.get_students(conn)
        class_average = Average.get_class_avg(conn,students)
        class_tests = Average.get_class_tests_avgs(conn)
        class_activities = Average.get_class_activities_avgs(conn)
        class_output = "<b><u>Class</u></b>" + "<br/>Average: " + str(class_average) + "<br/>Test Average: " + str(class_tests["tests"]) + "<br/>T1 Avg: " + str(class_tests["t1"]) + ", T2 Avg: " + str(class_tests["t2"]) + ", T3 Avg: " + str(class_tests["t3"]) + ", T4 Avg: " + str(class_tests["t4"]) + "<br/>Activity Average: " + str(class_activities["activities"]) + "<br/>A1 Avg: " + str(class_activities["a1"]) + ", A2 Avg: " + str(class_activities["a2"]) + ", A3 Avg: " + str(class_activities["a3"])

        return student_output, class_output

    def lang_comp():
        database = "MOOC_dos.db"
        conn = create_connection(database)

        spanish_students = len(Spanish.get_students(conn))
        sp = len(Spanish.get_passed(conn))
        sf = len(Spanish.get_failed(conn))
        si = len(Spanish.get_incomplete(conn))
        spanish = "<b><u>Spanish</u></b>" + "<br/>Total: " + str(spanish_students) + " students" + "<br/>Passed: " + str(sp) + " (" + str(round((sp/spanish_students)*100,2)) + "%)" + "<br/>Failed: " + str(sf) + " (" + str(round((sf/spanish_students)*100,2)) + "%)" + "<br/>Incomplete: " + str(si) + " (" + str(round((si/spanish_students)*100,2)) + "%)"
        
        english_students = len(English.get_students(conn))
        ep = len(English.get_passed(conn))
        ef = len(English.get_failed(conn))
        ei = len(English.get_incomplete(conn))
        english = "<b><u>English</u></b>" + "<br/>Total: " + str(english_students) + " students" + "<br/>Passed: " + str(ep) + " (" + str(round((ep/english_students)*100,2)) + "%)" + "<br/>Failed: " + str(ef) + " (" + str(round((ef/english_students)*100,2)) + "%)" + "<br/>Incomplete: " + str(ei) + " (" + str(round((ei/english_students)*100,2)) + "%)"

        return spanish, english






class TestMoocFinal(unittest.TestCase):
    def setUp(self):
        database = "MOOC.db"
        try:
            self.conn = sqlite3.connect(database)
            return self.conn
        except Error as e:
            print(e)
     
        return None

    def test_GetPassed(self):
        num_passed = get_passed(self.conn)
        self.assertEqual(num_passed, 279)


if __name__ == "__main__":
    unittest.main(verbosity=2)
