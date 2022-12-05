from django.shortcuts import redirect, render

# Create your views here.

from doctor.models import client,doctor

def home_page(request):
    message=''
    Lcounter=0
    Ncounter=0
    Scounter=0
    if request.method == 'POST':
        didg = request.POST.get('did')
        u = request.POST.get('username')
        p = request.POST.get('password')
        for i in p:
            print(ord(i))
            if ord(i)>=97 and ord(i)<=122:
                Lcounter=Lcounter+1

            if ord(i)>=48 and ord(i)<=57:
                Ncounter=Ncounter+1 

            if ord(i)>=33 and ord(i)<=38:
                Scounter=Scounter+1

        if (Lcounter==0):
            message='The password most have letters!'

        if (Ncounter==0):
            
            message='The password most have numbers!' 
            
        
        if (Scounter==0):
            message='The password most have Special letters!'     
         

        if doctor.objects.filter(did=didg,username=u,password=p).exists():
             return redirect('client') 
    content = {'message':message}
    return render(request,'home.html',content)


def list_client(request):
    lst = client.objects.all()
    content = {'clients':lst}
    return render(request,'list_client.html',content)


def client_page(request):
    message =''
    message1=''
    message2=''
    message3=''
    message4=''
    message5=''
    message6=''
    message7=''
    message8=''
    message9=''

    content={}
    if request.method == 'POST':
        did = request.POST.get('did')
        name = request.POST.get('name')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        WBC=request.POST.get('WBC')
        Neut=request.POST.get('Neut')
        Lymph=request.POST.get('Lymph')
        RBC=request.POST.get('RBC')
        HCT= request.POST.get('HCT')
        Urea=request.POST.get('Urea')
        HB=request.POST.get('HB')
        Creatinine=request.POST.get('Creatinine')
        Iron=request.POST.get('Iron')
        HDL=request.POST.get('HDL')
        q1 = request.POST.get('q1')
        q2 = request.POST.get('q1')
        q3 = request.POST.get('q1')
        condition = request.POST.get('condition')
        client.objects.create(did=did,name=name,q1=q1,q2=q2,q3=q3,condition=condition,age= age,gender=gender,WBC=WBC,Neut=Neut,Creatinine=Creatinine,Lymph=Lymph,RBC=RBC,HCT=HCT,Urea=Urea,HB=HB,Iron=Iron,HDL=HDL)
        if ((int)(age)>=18 and (int)(WBC)>=4500 and (int)(WBC)<=11000) or ((int)(age)>=4 and (int)(age)<=17 and (int)(WBC)>=5500 and (int)(WBC)<=15500) or ((int)(age)>=0 and (int)(age)<=3 and (int)(WBC)>=6000 and (int)(WBC)<=17500):
            message='The white blood cells number is good'
        
        if ((int)(age)>=4 and (int)(age)<=17 and (int)(WBC)>15500) or ((int)()>=18 and (int)(WBC)>11000) or ((int)(age)>=0 and (int)(age)<=3 and  (int)(WBC)>17500) :
            message='The white blood cells number is higher than normal : Most often indicate the presence of an infection, if there is a fever. In other cases, very rare, mayVery high values indicate blood disease or cancer.'
           

        if ((int)(age)>=4 and (int)(age)<=17 and (int)(WBC)<4500) or ((int)()>=18 and (int)(WBC)<5500) or ((int)(age)>=0 and (int)(age)<=3 and  (int)(WBC)<6000) :
            message='The white blood cells number is lower than normal :Indicate viral disease, immune system failure and in very rare cases cancer. '




        if (int)(Neut)>=28 and (int)(Neut)<=54:
            message1='The persentage of the protective WBC is good'

        if (int)(Neut)>54:
            message1='High values: Most often indicate a bacterial infection.'
        if (int)(Neut)<28:
            message1='Low values: indicate a disorder of blood formation, a tendency to bacterial infections and in rare cases - a process cancerous.'
        #//////////////////////////////////////////////

        if (int)(Lymph)>=36 and (int)(Lymph)<=52:
            message2='The virus fighting WBC number is good'

        if (int)(Lymph)<36:
            message2='The virus fighting WBC number is lower than normal: Indicate a problem in the formation of blood cells'

        if (int)(Lymph)>52:
            message2='The virus fighting WBC number is higher than normal: May indicate a prolonged bacterial infection or lymphoma cancer.'

        #///////////////////////////////////////////////

        if (float)(RBC)>=(4.5) and (float)(RBC)<=(6.0):
            message3='The binding oxygen RBCs number is good'

        if (float)(RBC)<4.5:
            message3='Low values: May indicate anemia or severe bleeding'
        if (float)(RBC)>6:
            message3='High values: may indicate a disturbance in the blood production system. High levels were also observed in smokers and in patients In lung diseases.'    
        #///////////////////////////////////////////////////
        
        if  gender=="Male":
            if (int)(HCT)>=37 and (int)(HCT)<=54:
                message4='The HCT is fine'

            if (int)(HCT)<37:
                message4='Low values: Most often indicate bleeding or anemia.'

            if (int)(HCT)>54:
                message4='High values: Common in smokers.'

        if gender=="Female":
            if (int)(HCT)>=33 and (int)(HCT)<=47:
                message4='The HCT is fine'

            if (int)(HCT)<33:
                message4='Low values: Most often indicate bleeding or anemia.'

            if (int)(HCT)>47:
                message4='High values: Common in smokers.'

        #//////////////////////////////////
        if (int)(Urea)>=17 and (int)(Urea)<=(43):
            message5='Level urinated in the blood is fine.'

        if (int)(Urea)<17:
            message5='Low values: malnutrition, low-protein diet or liver disease.'    

        if (int)(Urea)>43:
            message5='High values: May indicate kidney disease, dehydration or a high-protein diet.'

        #///////////////////////////////////////////////////////
        if gender=="Female" and (int)(age)>17:
            if  (float)(HB)>=12 and  (float)(HB)<=16:
                message6='The HB is good'
            if  (float)(HB)<12:
                message6='Low values: Indicates anemia. This can be due to a hematologic disorder, iron deficiency and bleeding.'
        if gender=="Male" and (int)(age)>17:
            if  (float)(HB)>=12 and  (float)(HB)<=18:
                message6='The HB is good'
            if  (float)(HB)<12:
                message6='Low values: Indicates anemia. This can be due to a hematologic disorder, iron deficiency and bleeding.'
        if (int)(age)<18:
            if (float)(HB)>=11.5 and  (float)(HB)<=15.5:
                message6='The HB is good'
            if  (float)(HB)<11.5:
                message6='Low values: Indicates anemia. This can be due to a hematologic disorder, iron deficiency and bleeding.'
        
        #////////////////////////////////////////////////////////////////////////
        if (int)(age)>=0 and (int)(age)<=2:
            if (float)(Creatinine)>=0.2 and (float)(Creatinine)<=0.5:
                message7='The Creatinine is good'
            if (float)(Creatinine)<0.2:
                message7='Low values: Most commonly seen in patients with very poor muscle mass and malnourished people who do not consume enough protein.'
            if (float)(Creatinine)>0.5:
                message7='High values: may indicate a kidney problem and in severe cases kidney failure.'
        if (int)(age)>=3 and (int)(age)<=17:
            if (float)(Creatinine)>=0.5 and (float)(Creatinine)<=1.0:
                message7='The Creatinine is good'
            if (float)(Creatinine)<0.5:
                message7='Low values: Most commonly seen in patients with very poor muscle mass and malnourished people who do not consume enough protein.'
            if (float)(Creatinine)>1.0:
                message7='High values: may indicate a kidney problem and in severe cases kidney failure.'
        if (int)(age)>=18 and (int)(age)<=59:
            if (float)(Creatinine)>=0.6 and (float)(Creatinine)<=1.0:
                message7='The Creatinine is good'
            if (float)(Creatinine)<0.6:
                message7='Low values: Most commonly seen in patients with very poor muscle mass and malnourished people who do not consume enough protein.'
            if (float)(Creatinine)>1.0:
                message7='High values: may indicate a kidney problem and in severe cases kidney failure.'
        if (int)(age)>=60:
            if (float)(Creatinine)>=0.6 and (float)(Creatinine)<=1.2:
                message7='The Creatinine is good'
            if (float)(Creatinine)<0.6:
                message7='Low values: Most commonly seen in patients with very poor muscle mass and malnourished people who do not consume enough protein.'
            if (float)(Creatinine)>1.2:
                message7='High values: may indicate a kidney problem and in severe cases kidney failure.'
        #//////////////////////////////////////////////
        if gender=="Male":
            if (int)(Iron)>=60 and (int)(Iron)<=160:
                message8='The Iron is good'
            if (int)(Iron)<60:
                message8='Low levels: usually indicates an inadequate diet or an increase in the need for iron (for example during pregnancy) or blood loss Following bleeding.'
            if (int)(Iron)>160:
                message8='High levels: May indicate iron poisoning.'
        if gender=="Female":
            if (int)(Iron)>=0.8*60 and (int)(Iron)<=0.8*160:
                message8='The Iron is good'
            if (int)(Iron)<0.8*60:
                message8='Low levels: usually indicates an inadequate diet or an increase in the need for iron (for example during pregnancy) or blood loss Following bleeding.'
            if (int)(Iron)>0.8*160:
                message8='High levels: May indicate iron poisoning.'
        #//////////////////////////////////////////////
        if gender=="Male":
            if (int)(HDL)>=29 and (int)(HDL)<=62:
                message9='The HDL is good'
            if (int)(HDL)>62:
                message9='High levels: are usually harmless. Exercise raises "good" cholesterol levels.'
            if (int)(HDL)<29:
                message9='Low levels: may indicate risk of heart disease, hyperlipidemia (hyperlipidemia) or adult-onset diabetes.'
        if gender=="Female":
            if (int)(HDL)>=34 and (int)(HDL)<=82:
                message9='The HDL is good'
            if (int)(HDL)>82:
                message9='High levels: are usually harmless. Exercise raises "good" cholesterol levels.'
            if (int)(HDL)<34:
                message9='Low levels: may indicate risk of heart disease, hyperlipidemia (hyperlipidemia) or adult-onset diabetes.'
        #//////////////////////////////////////////////



        content = {'message':message,'message1':message1,'message2':message2,'message3':message3,'message4':message4,'message5':message5,'message6':message6,'message7':message7,'message8':message8,'message9':message9}
        return render(request,'table.html',content)



    content = {}
    return render(request,'client_page.html',content)