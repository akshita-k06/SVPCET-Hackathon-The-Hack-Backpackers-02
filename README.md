# SVPCET-Hackathon-Comet-12

Project submitted under SVPCET Virtual Hackathon.

Team Members:
1. Akshita Khandelwal (Team Leader)
2. Vrushali Nagrale
3. Pradyumna Mahajan
4. Ritika Chouthmal
  
## Problem Statement

In India, many of the problems like road repairing, electricity etc of
people can't reach to the person in charge responsible for that problemor sometimes the person in charge doesn't pay heed to the problem.
Your task is to design and develop a system/software which will allow
people to directly report the problems to the concerned authorities. The
system must contain following :
1. Fake problem detection mechanism
2. Option to filter problems on the basis of category of the
problem.

## Solution
Considering the above problem, building an application that hears all the problems faced by citizens is the need of the hour. We have tried to build a website where the citizens can share their problems by posting them on it. Also, this application will convey all the complaints to the respected authorities and tell the time required to resolve the problem.
To avoid fake problems, the complainant is bound to share the picture of the problem. One more feature has been added here two maintain transparency, an OTP would be sent on the registered Email ID to check the staunchness. The User also has to upload their scanned Adhaar card while registering.
The type of problems that can be caused is already set up in a prioritised hierarchy to solve the emergency issues first. For example, issues such as leakage in pipelines are prioritized on a higher level to avoid wastage of water. Hence this application acts as an intermediate between the citizens and the respective authority.


## Project Description
The project has a starting page where the individual can register either as a complainant or the complaint solver. While registering the user has to provide details such as name, userID, password, aadhaar, address, city, state followed by an OTP to get registered properly. Also, the Adhaar should be a scanned original copy. There is also the functionality of the forgot password in case the user forgets later.
After registration, the user would lead to another page where the individual has to choose the type of problems related to it. There are options for Electricity, Garbage, Roads, Water, and Safety in the respective locality. After clicking on the chosen category certain possible options are given, from which the user can choose the relatable one, or type the one if not mentioned in the given options. After selecting the options the complaint would get registered and the time taken to resolve the complaint would be provided.
FEATURES:
1.	Secure login-logout (password encryption)
2.	User Friendly
3.	Transparency in application
4.	Fully Informative
5.	Filtration in complaints using hierarchy.




## Problem Faced
1.	 Firstly as everything was online while contributing code it was a difficult and time consuming process.
2.	Certain connectivity issues led to a waste of time a bit.
3.	As it is the term end time, there were a lot of submissions and slide presentations simultaneously going on in the college.
4.	Debugging errors was a bit difficult.
But if we look at the positive side we learnt time management quite well and it was a great experience for us working as a team on this project.



## Tech-Stack Used

1. Python(Django) 
2. Database sqlite and mysql

## Website link

To see our porject, please check out our website link : http://socialshout.psmweb.in/


## Video Link

To see the demo, check out : https://drive.google.com/file/d/1L_N-xwezTMVNQJB-PwS1gcyqgfwJ9q1g/view?usp=sharing

## To run this project, run following commands

**Note: Mention all the commands/steps to run this project, here**

Download all repository files


1 - First setup python


2 -then venv — Creation of virtual environments (https://docs.python.org/3/library/venv.html)

3) run the following commands: 

### `command 1`

pip install django

### `command 2`

pip install mysqlclient


### `command 3`

pip install wheel

### `command 4`

pip install Pillow

### `command 5`

for windows run 
python manage.py collectstatic
for linux
python3 manage.py collectstatic

### `command 6`

python manage.py runerver 

it start devlopment server



## Mention Any other details here:

...
...


## References

**Note: Mention all the references used in the project her**

**Example :**
Reference 1 : https://docs.djangoproject.com/en/3.1/
