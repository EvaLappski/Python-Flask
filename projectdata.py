from project import db, Student, Competency, Project

db.create_all()

Eva = Student('Eva', 'Lapp', 'https://www.linkedin.com/in/eva-lapp-01b27a60/', 'https://github.com/EvaLappski', 250, 1)
Dima = Student('Dima', 'Marachi', 'https://www.linkedin.com/in/dima-marachi', 'https://github.com/dmarachi/', 250, 2)
Shane = Student('Shane', 'McGuire', 'https://www.linkedin.com/in/shane-mcguire-100 ', 'https://github.com/shanemcg88/evolveu', 930, 1)
Linden = Student('Linden','Achen',	'https://www.linkedin.com/in/linden-achen',	'https://github.com/LindenAc', 210, 2)
Trent = Student('Trent', 'Apt', 'https://www.linkedin.com/in/trent-apt/', 'https://github.com/DuskGuard', 250, 2)
Ian = Student('Ian', "Austin", 'https://www.linkedin.com/in/ianqaustin', 'https://github.com/IanQAustin', 250, 3)
Cheryl = Student('Cheryl', 'Best', 'https://www.linkedin.com/in/cheryl-lyn-best/', 'https://github.com/cheryllynbest', 210, 2)
Seun = Student('Seun', "Mejule",'https://www.linkedin.com/in/seun-mejule-a9827939/', 'https://github.com/seunjule', 298, 1 )
Jarvis = Student('Jarvis','Gibb','https://www.linkedin.com/in/jarvisgibb/','https://github.com/JarvisRGibb', 230, 4)
Luis = Student('Luis','Cabana','https://www.linkedin.com/in/luiscabana/','https://github.com/luife69/', 250, 4) 
Gio = Student('Giovanni','Chajon',	'https://www.linkedin.com/in/giochajon/','https://github.com/giochajon/', 298, 4)
Byron = Student('Byron','Daniels',	'https://www.linkedin.com/in/byron-daniels/','https://github.com/byrondaniels', 298, 2)
Kristina = Student('Kristina','Davidson','https://www.linkedin.com/in/kristinadavidsonpeng','https://github.com/kldavids', 210, 3)
Lauren = Student('Lauren',	'Diederichs','https://www.linkedin.com/in/laurendiederichs/','https://github.com/ladieder', 250, 4)
Jawad = Student('Jawad','Farid', 'https://www.linkedin.com/in/jawad-farid',	'https://github.com/jawadfarid', 230, 1)
Matt= Student('Matt','Fisher','https://www.linkedin.com/in/mattfisherrr/','https://github.com/Matt-Fisherrr', 298, 2)
Greg = Student('Greg','Freson', 'https://www.linkedin.com/in/greg-freson-p-eng','https://github.com/GregFdev', 250, 1)
Licedt = Student('Licedt','Hernault','https://www.linkedin.com/in/licedthernault/',	'https://github.com/lhernault', 210, 3)
Omar = Student('Omar','Hussain','https://www.linkedin.com/in/omar-hussain',	'https://github.com/OmarHussainX', 298, 1)
Carrie = Student('Carrie','Nermo','https://www.linkedin.com/in/carrienermo','https://github.com/KrakenYYC', 150, 1)
Alex = Student('Alex','Jinga','https://www.linkedin.com/in/alex-jinga', 'https://github.com/alexjinga', 250, 4)
Dustin = Student('Dustin','Joynt', 'https://www.linkedin.com/in/dustin-joynt','https://github.com/dustinjoynt', 250, 4)
# James	Kiernan	https://www.linkedin.com/in/james-kiernan1/	https://github.com/JamesKiernanYYC
# Jinbong	Lee	www.linkedin.com/in/Jinbong	https://ljb6685.github.io
# Fawad	Malik	https://www.linkedin.com/in/fawad-malik/	https://github.com/Tech2019
# Roman	Mirakhmedov	https://www.linkedin.com/in/mirakhmedov/	https://github.com/rm-evolveu/
# Niloufar	Naderi	https://linkedin.com/in/nilou-naderi/	https://github.com/ninaderi
# Harpreet	Parhar	https://www.linkedin.com/in/harpreet-parhar-75594726/	https://github.com/Harpreet-Parhar-Canada
# Forest	Park	https://www.linkedin.com/in/forestpark	https://github.com/foresthpark
# LaTora	Prince	https://www.linkedin.com/in/latora-prince-6179361b/	https://github.com/xvcrimsajadevx	
# Steven	Rothenburger	https://www.linkedin.com/in/steven-rothenburger/	https://github.com/srothenburger1
# Monica	 Shi	https://www.linkedin.com/in/monica-shi-11749130/	https://github.com/Monicashi123
# Jingnan	Zhang	https://www.linkedin.com/in/jingnanzhang/	https://github.com/jingnanzh
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

db.session.add_all([Eva, Dima, Shane, Linden, Trent, Ian, Cheryl, Seun, Jarvis, Luis, Gio, Byron, Kristina, Lauren, Jawad, Matt, Greg, Licedt,Omar, Carrie, Alex, Dustin])
db.session.add_all([ a,b,c,d,e,f,g,h,i,j,k,l,m])
db.session.add_all([mindfuel, cultivatr, library, rainforester])

db.session.commit()

print(Eva.student_id)


print(c.comp_num)
print(mindfuel.project_name)






