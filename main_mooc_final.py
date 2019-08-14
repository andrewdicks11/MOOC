import code_mooc_final

DATABASE = "MOOC_dos.db"

conn = code_mooc_final.create_connection(DATABASE)

from flask import Flask
app = Flask(__name__)


# Opening page
@app.route("/")
def index():

	message = """
	<h1>Statistical Report</h1>

	This is a statistical report showing the progress and participation of the MOOC class.<br/><br/>

	<a href="http://127.0.0.1:5000/Class+Statistics">Class Statistics</a><br/>
	<a href="http://127.0.0.1:5000/Individual+Statistics">Individual Statistics</a><br/>
	<a href="http://127.0.0.1:5000/Language+Statistics">Language Statistics</a><br/>

	"""

	return message


# Main links to stats
@app.route("/<select>")
def statistics(select):
	home = "<a href='http://127.0.0.1:5000/'>Home</a><br/><br/>"

	# Class Stats
	if select == 'Class+Statistics':
		lst = []

		# number of students in the class
		num_students = "Number of students: <b>" + str(code_mooc_final.Stats.num_students()) + "</b>"
		lst.append(num_students)
		
		# number of students that are passing
		passing = code_mooc_final.Stats.num_passed()
		p = "Number of students --> Passing: <b>" + str(passing[0]) + "</b><br/>" + str(passing[0]) + "/" + str(passing[1]) + " = (" + passing[2] + "%)"
		lst.append(p)

		# number fo students that are failing
		failing = code_mooc_final.Stats.num_failed()
		f = "Number of students --> Failing: <b>" + str(failing[0]) + "</b><br/>" + str(failing[0]) + "/" + str(failing[1]) + " = (" + failing[2] + "%)"
		lst.append(f)

		# number of students that have no completed any work
		incomplete = code_mooc_final.Stats.num_incomplete()
		i = "Number of students --> Incomplete: <b>" + str(incomplete[0]) + "</b><br/>" + str(incomplete[0]) + "/" + str(incomplete[1]) + " = (" + incomplete[2] + "%)"
		lst.append(i)

		# class average grade
		class_avg = code_mooc_final.Stats.class_avg()
		class_average = "Class average: <b>" + str(class_avg) + "</b>"
		lst.append(class_average)

		# passing students average grade
		pass_avg = code_mooc_final.Stats.pass_avg()
		pass_average = "Average (passing students): <b>" + str(pass_avg) + "</b>"
		lst.append(pass_average)

		# passing and failing students average grade
		pf_avg = code_mooc_final.Stats.pf_avg()
		pf_average = "Average (passing and failing students): <b>" + str(pf_avg) + "</b>"
		lst.append(pf_average)

		output = ""
		for item in lst:
			output += item
			output += "<br/><br/>"

		return home + output

	# Idividual Student Stats
	elif select == 'Individual+Statistics':
		users = code_mooc_final.Stats.users()
		output = ""
		for user in users:
			output += "<a href='http://127.0.0.1:5000/Individual+Statistics/" + user + "'>" + user + "</a>"
			output += "<br/>"
		return home + output

	# Language Distributon Stats
	elif select == 'Language+Statistics':
		lang_comp = code_mooc_final.Stats.lang_comp()
		return home + lang_comp[0] + "<br/><br/>" + lang_comp[1]

	else:
		return home + "Invalid, try again."


# Returns the test and activity results for invidual students
# Compares their results to the class
@app.route("/Individual+Statistics/<username>")
def user(username):
	back = "<a href='http://127.0.0.1:5000/Individual+Statistics'>Back</a><br/><br/>"

	users = code_mooc_final.Stats.users()
	if username in users:
		ut = code_mooc_final.Stats.get_tests(username)
		tests = str(ut[1]) + ", " + str(ut[2]) + ", " + str(ut[3]) + ", " + str(ut[4])
		test_results = ut[0] + " test results: <br/>" + tests

		ua = code_mooc_final.Stats.get_activities(username)
		activities = str(ua[1]) + ", " + str(ua[2]) + ", " + str(ua[3])
		activity_results = ut[0] + " activity results: <br/>" + activities

		comp = code_mooc_final.Stats.get_student_class_comp(username)
		comp_results = comp[0] + "<br/><br/>" + comp[1]
		
		return back + test_results + "<br/><br/>" + activity_results + "<br/><br/>" + comp_results

	else:
		return back + "Try again."



if __name__ == '__main__':
	app.run(debug=True)