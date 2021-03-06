from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from .form import RegisterForm, EditForm
from django.contrib.auth.forms import SetPasswordForm
# from learning.models import student
# from learning.form import PostForm
from django.contrib.auth.decorators import login_required





def home(request):
    return render(request,'home.html')
def register(request):
    return render(request,'register.html')
def User_login(request):
    return render(request,'login.html')
@login_required(login_url='/login/', redirect_field_name='next')
def personal(request):
    return render(request,'personal.html')
@login_required(login_url='/login/', redirect_field_name='next') 
def User_logout(request):
    return render(request,'home.html')
@login_required(login_url='/login/', redirect_field_name='next') 
def coursestart(request):
    return render(request,'coursestart.html')
@login_required(login_url='/login/', redirect_field_name='next') 
def class1(request):
    return render(request,'class1.html') 
@login_required(login_url='/login/', redirect_field_name='next') 
def lesson0(request):
    return render(request,'lesson0.html')  
@login_required(login_url='/login/', redirect_field_name='next') 
def lesson_1(request):
    return render(request,'lesson1_1.html')
@login_required(login_url='/login/', redirect_field_name='next') 
def lesson_2(request):
    return render(request,'lesson1_2.html')
@login_required(login_url='/login/', redirect_field_name='next') 
def lesson_3(request):
    return render(request,'lesson1_3.html')
@login_required(login_url='/login/', redirect_field_name='next') 
def lesson_4(request):
    return render(request,'lesson2_1.html')
@login_required(login_url='/login/', redirect_field_name='next') 
def lesson_5(request):
    return render(request,'lesson2_2.html')
@login_required(login_url='/login/', redirect_field_name='next') 
def lesson_6(request):
    return render(request,'lesson2_3.html')
@login_required(login_url='/login/', redirect_field_name='next') 
def lesson_7(request):
    return render(request,'lesson2_4.html') 
@login_required(login_url='/login/', redirect_field_name='next')  
def lesson_8(request):
    return render(request,'lesson2_5.html')
@login_required(login_url='/login/', redirect_field_name='next') 
def lesson_9(request):
    return render(request,'lesson3_1.html')
@login_required(login_url='/login/', redirect_field_name='next') 
def lesson_10(request):
    return render(request,'lesson3_2.html')
@login_required(login_url='/login/', redirect_field_name='next') 
def lesson_11(request):
    return render(request,'lesson3_3.html')
@login_required(login_url='/login/', redirect_field_name='next') 
def lesson_12(request):
    return render(request,'lesson3_4.html')
@login_required(login_url='/login/', redirect_field_name='next') 
def lesson_13(request):
    return render(request,'lesson4_1.html')
@login_required(login_url='/login/', redirect_field_name='next') 
def lesson_14(request):
    return render(request,'lesson4_2.html')
@login_required(login_url='/login/', redirect_field_name='next') 
def lesson_15(request):
    return render(request,'lesson4_3.html')
@login_required(login_url='/login/', redirect_field_name='next') 
def lesson_16(request):
    return render(request,'lesson3_5.html')
   


def register(request):
  if request.method == 'POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
        new_user = form.save()
        # ??????????????????????????????????????????????????????????????????
        # ------------------------------------
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        # ------------------------------------
        return HttpResponseRedirect('/coursestart/')
  else:
    form = RegisterForm()
  return render(request,'register.html',{'form':form,})

# ???learning/views.py ?????? User_login
def User_login(request):
    # ???????????????????????????????????????
    # ????????????????????????
    if request.user.is_authenticated:
        return HttpResponseRedirect('/coursestart/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        # ??????User??????????????????login
        if user is not None: 
            login(request, user)           
            return HttpResponseRedirect('/coursestart/')
        else:
            # ??????????????????????????????????????????
            error_message = "???????????????????????????????????????????????????"
            return render(request,'login.html',{'error_message':error_message})
    return render(request,'login.html')

# ???learning/views.py?????????User_logout function
def User_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# ??? views.py ????????? personal function
# ??????????????????????????? view
def personal(request):
    instance = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        form = EditForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
    else:
        form = EditForm(instance=instance)
    return render(request, 'personal.html',
        {
            'account': request.user.username,
            'form':form
        })

def reset_password(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    form = SetPasswordForm(user=request.user, data=request.POST)
    if form.is_valid():
        form.save()
        #update_session_auth_hash(request, form.user)
        return HttpResponseRedirect('/logout/')
    return render(request, 'reset.html',{ 'form':form })

# ?????????
# def lesson0(request):  
# 	students = student.objects.all().order_by('id')  #???????????????, ??? id ????????????
# 	return render(request, "lesson0.html", locals())
	
# def post(request):
# 	if request.method == "POST":		#????????????POST???????????????
# 		mess = request.POST['username'] #????????????????????????
# 	else:
# 		mess="????????????????????????!"	
# 	return render(request, "post.html", locals())
	
# def post1(request):  #?????????????????????????????????
# 	if request.method == "POST":	  #????????????POST???????????????
# 		cName = request.POST['cName'] #????????????????????????
		
# 		cAddr =  request.POST['cAddr']
# 		#??????????????????
# 		unit = student.objects.create(cName=cName, cAddr=cAddr) 
# 		unit.save()  #???????????????
# 		return redirect('/lesson0/')	
# 	else:
# 		message = '???????????????(??????????????????)'
# 	return render(request, "post1.html", locals())	
	
# def post2(request):  #?????????????????????????????????
# 	if request.method == "POST":  #????????????POST???????????????
# 		postform = PostForm(request.POST)  #??????forms??????
# 		if postform.is_valid():			#??????forms??????
# 			cName = postform.cleaned_data['cName'] #????????????????????????
			
# 			cAddr =  postform.cleaned_data['cAddr']
# 			#??????????????????
# 			unit = student.objects.create(cName=cName, cAddr=cAddr) 
# 			unit.save()  #???????????????
# 			message = '?????????...'
# 			return redirect('/lesson0/')	
# 		else:
# 			message = '??????????????????'	
# 	else:
# 		message = '??????????????????????????????'
# 		postform = PostForm()
# 	return render(request, "post2.html", locals())		
		
# def delete(request,id=None):  #????????????
# 	if id!=None:
# 		if request.method == "POST":  #????????????POST???????????????
# 			id=request.POST['cId'] #???????????????????????????
# 		try:
# 			unit = student.objects.get(id=id)  
# 			unit.delete()
# 			return redirect('/lesson0/')
# 		except:
# 			message = "????????????!"			
# 	return render(request, "delete.html", locals())	
	
# def edit(request,id=None,mode=None):  
# 	if mode == "edit":  # ??? edit.html ??? submit
# 		unit = student.objects.get(id=id)  #??????????????????????????????	
# 		unit.cName=request.GET['cName']
		
# 		unit.cAddr=request.GET['cAddr']		
# 		unit.save()  #???????????????
# 		message = '?????????...'
# 		return redirect('/lesson0/')	
# 	else: # ????????????
# 		try:
# 			unit = student.objects.get(id=id)  #??????????????????????????????
# 			strdate=str(unitcAddr)
# 			strdate2=strdate.replace("???","-")
# 			strdate2=strdate.replace("???","-")
# 			strdate2=strdate.replace("???","-")
# 			unit.cAddry = strdate2
# 		except:
# 			message = "??? id????????????"	
# 		return render(request, "edit.html", locals())	
		
# def edit2(request,id=None,mode=None):
#     if mode == "load":  # ??? index.html ??? ????????? ???
#       unit = student.objects.get(id=id)  #???????????????????????????
#       strdate=str(unit.cAddr)
#       strdate2=strdate.replace("???","-")
#       strdate2=strdate.replace("???","-")
#       strdate2=strdate.replace("???","-")
#       unit.cAddry = strdate2		
#       return render(request, "edit2.html", locals())
#     elif mode == "save": # ??? edit2.html ??? submit		
#       unit = student.objects.get(id=id)  #??????????????????????????????	
#       unit.cName=request.POST['cName']
      
#       unit.cAddr=request.POST['cAddr']		
#       unit.save()  #???????????????
#       message = '?????????...'
#       return redirect('/lesson0/')
	  
# def postform(request):  #?????????????????????????????????
# 	postform = PostForm()  #??????PostForm??????
# 	return render(request, "postform.html", locals())		  


#????????????

