from tkinter import*
import tkinter.font as TKFont
from tkinter.ttk import Combobox 
import customtkinter
from tkinter import messagebox
from PIL import Image , ImageTk
from playsound import playsound 
import urllib.request
import subprocess
import os


root = customtkinter.CTk()
root.geometry('1200x700')
root.title('AntiBiotics Dose Calculator V1')


customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('blue')


############################### Functions ############# Functions ################## Functions ########################
def check_for():
     try:

        urllib.request.urlretrieve("https://raw.githubusercontent.com/weedsman530/projects/main/augmentin.py", "C://dose//augmentin.py")
        os.system('cmd /c "pyinstaller --noconfirm --onedir --windowed --icon "D:/pharm logo.ico" --add-data "C://dose//customtkinter;customtkinter//"  "C://dose//augmentin.py" --distpath "c://dose2//""')
    finally:
        root.destroy()




def ok_win2(win2):
    win2.destroy()

def show():
    global ok_final
    for a in ('Augmentin' , 'Curam' , 'Megamox' , 'Hibiotic' , 'Clavimox' ,'E-Mox Clav' , 'Averobios', 'DeltaClav'):
        if my_combo.get()==a:
            concentration=(num1.get())
            weight=(num2.get())
            concentration.isdigit() or weight.isdigit()
            item3 = float(weight) * 50 
            item4 = item3 *5
            item5 = item4/ float(concentration)
            item6 = item5 / 3
            item7=round(item6 , 2)
            result_entry.delete(0 , END)
            result_entry.insert( 0 , item7)
            result_label.config(text='ml Every 8 hours')
        elif len(my_combo.get())==0:
            win2 = customtkinter.CTkToplevel(root)
            win2.geometry('340x120')
            win2.title('Error ')
            win2.iconbitmap('E://pharm logo.ico')
            labe_error = customtkinter.CTkLabel(win2 , text="Please Choose Medication First \n and Enter Weight" , text_font=TKFont.Font(family='Cairo', size=12 , weight='bold')
            , image=error_final , compound=RIGHT)
            labe_error.pack(anchor=CENTER)
            #label_error2 = customtkinter.CTkLabel(win2 , image=error_final  , text='')
            #label_error2.pack(anchor=S)
            playsound('E:\error.mp3', block=FALSE)
            btn_ok = customtkinter.CTkButton(win2 , image=ok_final , text="OK"   ,command=lambda: ok_win2(win2), fg_color=None , text_font=TKFont.Font(family='Helvitica' , size=10 , weight='bold'))
            btn_ok.pack(side=BOTTOM)
            return
        x = ('600' , '642.9') 
    for num in x :
        
        if  concentration_entry.get()==num:
            item6 = item5 / 2
            result_label.config(text='ml Every 12 hours')
        
      
        
        


        
    for b in ( 'Xithrone' ,'Azi Once' , 'Zithrodose' , 'Azrolid' , 'Epizithro' , 'Zithromax'):
        if my_combo.get()== b:
            concentration=(num1.get())
            weight=(num2.get())
            concentration.isdigit() or weight.isdigit()
            item3 = float(weight) * 12 * 5  / float(concentration)
            result_entry.delete(0 , END)
            result_entry.insert( 0 , item3)
            result_label.config(text='ml Every 24 hours') 
        if len(my_combo.get())  ==0:
            win2 = customtkinter.CTkToplevel(root)
            win2.geometry('340x120')
            win2.title('Error ')
            win2.iconbitmap('E://pharm logo.ico')
            labe_error = customtkinter.CTkLabel(win2 , text="Please Choose Medication First" , text_font=TKFont.Font(family='Cairo', size=12 , weight='bold')
            , image=error_final , compound=RIGHT)
            labe_error.pack(anchor=CENTER)
            #label_error2 = customtkinter.CTkLabel(win2 , image=error_final  , text='')
            #label_error2.pack(anchor=S)
            playsound('E:\error.mp3', block=FALSE)
            btn_ok = customtkinter.CTkButton(win2 , image=ok_final , text="OK"   ,command=lambda: ok_win2(win2) , fg_color=None , text_font=TKFont.Font(family='Helvitica' , size=10 , weight='bold')
            )
            btn_ok.pack(side=BOTTOM)
            return
            
            
        
        
            
            
            
            
            


    for c in medication2:
        if my_combo.get()==c:
            concentration=(num1.get())
            weight=(num2.get())
            concentration.isdigit() or weight.isdigit()
            cetal = float(weight) * 10 * 5 /float(concentration)
            result_entry.delete(0 , END)
            result_entry.insert( 0 , cetal)
            result_label.config(text='ml Every 6 : 8 hours')

        

        
button_mode = True
def Switch_mode():
    global button_mode
    if button_mode:
        data_frame1.configure(border_color='#86073B')
        data_frame2.configure(border_color='#86073B')
        
        btn2.configure(image=on_new , text='Dark Mode' , fg_color=None  , hover_color=None)
        customtkinter.set_appearance_mode('dark')
        button_mode=False
    else:
        btn2.configure(image=off_new , text='Light mode' ,fg_color=None)
        customtkinter.set_appearance_mode('light')
        data_frame1.configure(border_color='#0B508C')
        data_frame2.configure(border_color='#0B508C')
        button_mode=True

def exit():
    root.quit()

def closewin(win1):
   win1.destroy()


def turn_off():
    global no_final , ok_final
    win1 = customtkinter.CTkToplevel(root)
    win1.geometry('330x100')
    win1.title('Confirm Exit ')
    win1.iconbitmap('E://exit.ico')
    
    btn1=customtkinter.CTkButton(win1 , text='YES'   , command=exit ,
    image=ok_final , bg_color=None , fg_color=None ,text_font=TKFont.Font(family='Helvitica' , size=10 , weight='bold') )
    btn1.grid(row=1 , column=0)
    
    btn2=customtkinter.CTkButton(win1 , text='NO' , image=no_final , bg_color=None ,command=lambda:closewin(win1)
    , fg_color=None , text_font=TKFont.Font(family='Helvitica' , size=10 , weight='bold'))
    btn2.grid(row=1 , column=1)
    
    label_1 = customtkinter.CTkLabel(win1 , text='Do you Want To Exit ?' , text_font=TKFont.Font(family='Cairo' , size=10 , weight='bold'))
    label_2=customtkinter.CTkLabel(win1 , text='هتقفل يا غالى ولا ايه ؟ ' , text_font=TKFont.Font(family='Cairo' , size=12 , weight='bold'))
    label_2.grid(row=0 , column=1)
    label_1.grid(row=0 , column=0)


def month_kg():
    age_month = (num3.get())
    if (age_month.isdigit()):
        try:

            result_kg= float(age_month) * .5
            final_weight= result_kg + 4     
            month_result_entry.delete(0 ,END)
            month_result_entry.insert(0 , final_weight)
            month_result_label.config(text='baby weight is : ')
        finally : 
            month_result_entry.insert(END , " KG")
    
def year_kg():
    age_year=(num4.get())
    if (age_year.isdigit()):
        try:

            result_year_weight= float(age_year) * 2 
            baby_weight= float(result_year_weight) + 8
            year_result_entry.delete(0 , END)
            year_result_entry.insert(0 ,baby_weight)
            year_result_label.config(text='baby weight is : ')
        finally:

             year_result_entry.insert(END , " KG")

    
    
    



def clear_all(): 
    weight_entry.delete(0 , END)
    concentration_entry.delete(0 , END)




########################################################

on=Image.open("E://on2.png")
resized_on=on.resize((60 , 30) , Image.ANTIALIAS)
on_new=ImageTk.PhotoImage(resized_on)

off = Image.open("E://off.png")
resized_off=off.resize((60 , 30 ) , Image.ANTIALIAS)
off_new=ImageTk.PhotoImage(resized_off)
  
show_img=Image.open('E://show.png')
show_res=show_img.resize((50 , 50))
result_img=ImageTk.PhotoImage(show_res)

dose_img=Image.open('E://dose.png')
dose_resized=dose_img.resize((50 , 50))
dose_final=ImageTk.PhotoImage(dose_resized)

power_img=Image.open('E://power.png')
power_res=power_img.resize((50 , 50))
power_final=ImageTk.PhotoImage(power_res)


no_1 = Image.open('E://no.png')
no_res=no_1.resize((50 ,50))
no_final=ImageTk.PhotoImage(no_res)


ok_1 = Image.open('E://ok.png')
ok_res=ok_1.resize((50 ,50))
ok_final=ImageTk.PhotoImage(ok_res)

clear_1= Image.open('E://clear.png')
clear_res=clear_1.resize((40 , 40))
clear_final=ImageTk.PhotoImage(clear_res)

search_1= Image.open('E://search.png')
search_res=search_1.resize((30 ,30))
search_final=ImageTk.PhotoImage(search_res)

month_img= Image.open('E://month.png')
month_res=month_img.resize((40 , 40))
month_final=ImageTk.PhotoImage(month_res)

weight_img= Image.open('E://weight.png')
weight_res=weight_img.resize((50 , 50))
weight_final=ImageTk.PhotoImage(weight_res)

year_weight = Image.open('E://baby year.png')
year_res= year_weight.resize((50 ,50 ))
year_final=ImageTk.PhotoImage(year_res)

error_img = Image.open('E://error.png')
error_reszized = error_img.resize((40 , 40 ))
error_final=ImageTk.PhotoImage(error_reszized) 


###########################################################
btn_upadte=customtkinter.CTkButton(root , text="Check For Update" , command=check_for)
btn_upadte.place(rely=.01 , relx=.8)
btn2 = customtkinter.CTkButton(root ,text='Light Mode', command=Switch_mode  , image=off_new , hover_color=None , bg_color=None , fg_color=None , text_font=TKFont.Font(family="Comic Sans MS",size=10,weight="bold"))
btn2.pack(side=TOP , anchor=NW)

btn_power=customtkinter.CTkButton(root , image=power_final , text='' , hover_color=None , bg_color=None , fg_color=None , command=turn_off)
btn_power.pack(anchor=N)

#################################### Frames ###################### Frames ######################## Frames #############
data_frame1 = customtkinter.CTkFrame(root , border_color='#A5274F' , border_width=3)
data_frame1.pack(fill="y" , expand="no" , pady=10 , side=LEFT , padx=10 , ipadx=20)


data_frame2=customtkinter.CTkFrame(root , border_color='#A5274F' , border_width=3)
data_frame2.pack(padx=10, pady=10 , side=TOP , expand='yes' , fill='y'  )

data_frame3=customtkinter.CTkFrame(root , border_color='#A5274F' , border_width=3)
data_frame3.pack(padx=10, pady=10 , side=BOTTOM, expand='yes' , fill='x'  )
################### medications ########################  medications  ###################################################################
medications=['Augmentin' , 'Curam' , 'Megamox' , 'Hibiotic' , 'Clavimox' ,'E-Mox Clav' , 'Averobios', 'DeltaClav' , 'Suprax' , 'Zithromax' , 'Septrin' , 'Septazole', 'Xithrone' ,
'Azi Once' , 'Zithrodose' , 'Azrolid' , 'Epizithro']
concentration_aug = ['600' , '642.9']
medication2 = ["Cetal" , "Temporal"]
medications.sort()
########################################################################################################################

my_combo = Combobox(data_frame1 , values=medications+medication2 )


my_combo.grid(pady=10 , row=0 , column=1 )


my_combo_label = customtkinter.CTkLabel(data_frame1 , text='Select Medication' , text_font=TKFont.Font(family='Cairo' , size=12 , weight='bold') , image=search_final
, compound=RIGHT)
my_combo_label.grid(row=0 , column=0, padx=5)

#######################################################################

num1 = StringVar()
num2 = StringVar()
num3 = StringVar()
num4 = StringVar()
concentration_entry=customtkinter.CTkEntry(data_frame1 ,  justify=CENTER , textvariable=num1, text_font=TKFont.Font(family="Comic Sans MS",size=10,weight="bold"))
concentration_entry.grid(pady=60 ,  row=1 , column=1)



concentration_label=customtkinter.CTkLabel(data_frame1 , text='Enter Concentration : ' ,  text_font=TKFont.Font(family='Cairo' , size=12 , weight='bold'))
concentration_label.grid( pady=60 ,row=1 , column=0 , padx=5)


weight_entry=customtkinter.CTkEntry(data_frame1 , justify=CENTER ,  textvariable=num2 , text_font=TKFont.Font(family="Cairo",size=10,weight="bold"))
weight_entry.grid(row=2 , column=1)


weight_label=customtkinter.CTkLabel(data_frame1 , text='Enter Weight : '  , text_font=TKFont.Font(family='Cairo' , size=12 , weight='bold'))
weight_label.grid(row=2 , column=0)



btn1 = customtkinter.CTkButton(data_frame1 , text='Show Dose' , command=show, image=result_img , compound=RIGHT , fg_color=None
, text_font=TKFont.Font(family='Cairo' , size=12, weight='bold') , border_color='#0B508C' , border_width=3)
btn1.grid(columnspan=3 , pady=70)

############################################ data frame 2 ###########################

result_label=customtkinter.CTkLabel(data_frame2 , text='', text_font=TKFont.Font(family='Helvitica' , size=10 , weight='bold'))
result_label.grid(row=0 , column=2 , pady=10 , padx=10)

result_entry=customtkinter.CTkEntry(data_frame2, justify=CENTER, text_font=TKFont.Font(family='Comic Sans Ms' , size=10 , weight='bold'))
result_entry.grid(row=0 , column=1, pady=10, padx=10)

result_label2=customtkinter.CTkLabel(data_frame2 , text='Dose is :', text_font=TKFont.Font(family='Helvitica' , size=10 , weight='bold')  , image=dose_final , compound=RIGHT)
result_label2.grid(row=0 , column=0 , pady=10 , padx=10)

btn_clear=customtkinter.CTkButton(data_frame2 , text='Clear ' , image=clear_final , compound=RIGHT  , text_font=TKFont.Font(family="Cairo",size=12,weight="bold")
,fg_color=None , border_color='#A5274F' , border_width=2 , command=clear_all)
btn_clear.grid(columnspan=3)

################################################################################ data frame 3 ##########################
month_label = customtkinter.CTkLabel(data_frame3 , text="Enter Age in Months \n ( from 1 to 12 months ) " , image=month_final , compound=RIGHT , text_font=TKFont.Font(family='Helvitica' , size=10 , weight='bold'))
month_label.grid(row=0 , column=0 , pady=10 , padx=10 ) 

month_entry= customtkinter.CTkEntry(data_frame3  , justify=CENTER , text_font=TKFont.Font(family='Comic Sans Ms' , size=10 , weight='bold') , 
textvariable=num3 )
month_entry.grid(row=0  , column=1)

btn_month=customtkinter.CTkButton(data_frame3 , text='Calclate Weight' , fg_color=None , command=lambda:(month_kg() , year_kg())
,text_font=TKFont.Font(family='Comic Sans Ms' , size=10 , weight='bold')  , image=weight_final , compound=RIGHT , border_color='#A5274F' , border_width=2)
btn_month.grid(row=0 , column=3 , pady=10 , padx=15)


month_result_label = customtkinter.CTkLabel(data_frame3  , text='' , text_font=TKFont.Font(family='Cabin' , size=12 , weight='bold'))
month_result_label.grid(row=1  , column=0 , pady=15 , padx=15)


month_result_entry= customtkinter.CTkEntry(data_frame3  , justify=CENTER , text_font=TKFont.Font(family='Comic Sans Ms' , size=10 , weight='bold') ,text_color='red')
month_result_entry.grid(row=1  , column=1 , pady=15 , padx=15)


year_label = customtkinter.CTkLabel(data_frame3 , text="Enter Age in Years \n (From 1 to 5 Years)"  , image=year_final , compound=RIGHT , text_font=TKFont.Font(family='Cairo', size=10 , weight='bold'))
year_label.grid(row=2 , column=0 , pady=15 , padx=15)

year_entry= customtkinter.CTkEntry(data_frame3  , justify=CENTER , text_font=TKFont.Font(family='Comic Sans Ms' , size=10 , weight='bold') , textvariable=num4)
year_entry.grid(row=2  , column=1 , pady=15 , padx=15)

year_result_label=customtkinter.CTkLabel(data_frame3  , text='' , text_font=TKFont.Font(family='Cabin' , size=12 , weight='bold'))
year_result_label.grid(row=3 , column=0 , pady=15 , padx=15)

year_result_entry= customtkinter.CTkEntry(data_frame3  , justify=CENTER , text_font=TKFont.Font(family='Comic Sans Ms' , size=10 , weight='bold') , text_color='red')
year_result_entry.grid(row=3 , column=1 , pady=15 , padx=15)

#month_result_label1 = customtkinter.CTkLabel(data_frame3  , text='' , bg_color='light blue')
#month_result_label1.grid(row=1  , column=3)


#month_result=customtkinter.CTkEntry(data_frame3  , justify=CENTER , text_font=TKFont.Font(family='Comic Sans Ms' , size=10 , weight='bold'))
#month_result.grid(row=0  , column=3)








#update(medications)


root.mainloop()
