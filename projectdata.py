from project import db, Student, Competency, Project

db.create_all()

Eva = Student('Eva', 'Lapp', 'https://www.linkedin.com/in/eva-lapp-01b27a60/', 'https://github.com/EvaLappski', 250, 1)
Dima = Student('Dima', 'Marachi', 'www.linkedin.com/in/dima-marachi', 'https://github.com/dmarachi/', 250, 2)
Shane = Student('Shane', 'McGuire', 'www.linkedin.com/in/shane-mcguire-100 ', 'https://github.com/shanemcg88/evolveu', 930, 1)
a = Competency('Python - Full Stack',250, 4, 93.94)
b = Competency('PostgreSQL', 930, 3, 87.88)
c = Competency('Python - Flask', 240, 3, 83.33)
d = Competency('Javascript Basic Logic', 100, 5, 7.58)
e = Competency("Javascript Events/DOM", 110, 8, 19.70)
f = Competency('Git', 910, 2, 22.73)
g = Competency('ReactJS', 120, 3, 27.27)
h = Competency('Javascript TDD', 130, 2, 30.30)
i = Competency('Javascript OO', 140, 14, 51.52)
j = Competency('Javascript Algorithms', 150, 4, 57.58)
k = Competency('Javascript Open API JSON', 160, 1, 59.09)
l = Competency('Javascript React Redux ', 170, 3, 63.64)
m = Competency('D3', 180, 2, 66.67)
n = Competency('Front End Checklist', 198, 2, 69.70)
o = Competency('Python - Getting Started - Logic', 200, 2, 72.73)
p = Competency('Python - Environment Conda', 210, 1, 74.24)
q = Competency('Python - File IO', 220, 1, 75.76)
r = Competency('Python - Excel', 230, 2, 78.79)
s = Competency('Heroku', 940, 2, 96.97)
t = Competency("Docker", 950, 1, 99.98)
u = Competency("Back End Checklist", 298, 1, 100.00)
mindfuel = Project('MindFuel')
cultivatr = Project('Cultivatr')
library = Project('Calgary Public Library')
rainforester = Project('Rainforester')

print(Eva.student_id)

db.session.add_all([Eva, Dima, Shane])
db.session.add_all([ a,b,c,d,e,f,g,h,i,j,k,l,m])
db.session.add_all([mindfuel, cultivatr, library, rainforester])

db.session.commit()

print(Eva.student_id)


print(c.comp_num)
print(mindfuel.project_name)




