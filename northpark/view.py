from django.http import HttpResponse
from django.shortcuts import render
import datetime


trash_task_completed,hall_task_completed,kitchen_task_completed=[],[],[]
members=['Zakir','Yasser','Fawad','Nawad','Siddiq']
TRASH_INDEX=1
KITCHEN_INDEX=1
HALL_INDEX=1
CHANGED=True
person_t="Zakir"
person_k="Zakir"
person_h="Zakir"

def home(request):
	global person_t,person_h,person_k,CHANGED
	if request.method == 'POST':
		 if request.POST.get("trash"):
			 CHANGED=True
			 addUser("trash",person_t,str(datetime.datetime.now()))
			 person_t=getUser("trash")
		 if request.POST.get("kitchen"):
			 CHANGED=True
			 addUser("kitchen",person_k,str(datetime.datetime.now()))
			 person_k=getUser("kitchen")
		 if request.POST.get("hall"):
			 print ("here")
			 CHANGED=True
			 addUser("hall",person_k,str(datetime.datetime.now()))
			 person_h=getUser("hall")

	return render(request, 'home.html',{'person_t':person_t,'person_k':person_k,'person_h':person_h})
def trash(request):
	global CHANGED
	CHANGED=False
	return render(request, 'trash.html',  {'trash_task_completed':trash_task_completed,"hall_task_completed":hall_task_completed,"kitchen_task_completed":kitchen_task_completed})



def addUser(task,username,time):
	global trash_task_completed,kitchen_task_completed,hall_task_completed
	if task is "trash":
		print ("trash..")
		trash_task_completed.append({'name':username,'date':time})
	if task is "kitchen":
		print("here")
		kitchen_task_completed.append({'name':username,'date':time})
	if task is "hall":
		print("here")
		hall_task_completed.append({'name':username,'date':time})




def getUser(category):
	global TRASH_INDEX
	global KITCHEN_INDEX
	global HALL_INDEX
	global CHANGED

	if category is "trash":
		if(TRASH_INDEX>4):
			TRASH_INDEX=0
		user=members[TRASH_INDEX]
		TRASH_INDEX+=1
		return user
	if category is "kitchen":
		print ("in kitchen")
		if(KITCHEN_INDEX>4):
			KITCHEN_INDEX=0
		user=members[KITCHEN_INDEX]
		KITCHEN_INDEX+=1
		return user
	if category is "hall":
		print ("in hall")
		if(HALL_INDEX>4):
			HALL_INDEX=0
		user=members[HALL_INDEX]
		HALL_INDEX+=1
		return user
