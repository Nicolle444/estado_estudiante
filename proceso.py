from tkinter import *
from tkinter import messagebox,ttk
#----------------------
# funciones de la app
#----------------------
def aceptar():
    abrir_notas.destroy()
def salir():
    messagebox.showinfo("Tu información", "la página se cerrará")
    ventana_principal.destroy()
    
    
def guardar():
    messagebox.showinfo("Datos del estudiante","se guardaran los datos")

    nota1 = float(n1.get())
    nota2 = float(n2.get())
    nota3 = float(n3.get())
    nota4 = float(n4.get())  
    global codigo
    codigo= codigo.get() 
    global nombre
    nombre = nombre.get()
    promedio = (nota1 + nota2 + nota3 + nota4) / 4
    if promedio >= 10.0 and promedio <= 29.9:
        lb_c_img.config(image=img_t)
        t_resultados.insert(INSERT,"Debes esforzarte tu promedio esta perdido:c ")
    elif promedio >= 30.0 and promedio <=  40.9:
        lb_c_img.config(image=img_n)
        t_resultados.insert(INSERT,"Tu promedio es bueno, pero puedes dar más de ti._. ")
    else:
        lb_c_img.config(image=img_f)
        t_resultados.insert(INSERT,"Tienes un promedio excelente:D ")      
    t_resultados.insert(INSERT,"\nEl promedio del estudiante:"+ nombre  +",con código:"+codigo+" es: {:.1f}".format(promedio))
    p=float(pe.get())
    alt=float(al.get())
    IMC = p // (alt ** 2)
    if IMC < 16:
        lb_d_img.config(image=img_cari)
        t_r.insert(INSERT,"su diagnostico es criterio de ingreso en hospital")
    elif IMC > 16 and IMC < 17:
        lb_d_img.config(image=img_c1)
        t_r.insert(INSERT,"su diagnostico es infrapeso")
    elif IMC > 17 and IMC < 18:
        lb_d_img.config(image=img_c2)
        t_r.insert(INSERT,"su diagnostico es bajo peso")
    elif IMC > 18 and IMC < 25:
        lb_d_img.config(image=img_c4)
        t_r.insert(INSERT,"su diagnostico es peso normal(saludable)")
    elif IMC > 25 and IMC < 30:
        lb_d_img.config(image=img_c3)
        t_r.insert(INSERT,"su diagnostico es (obesidad grado I)")
    elif IMC > 30 and IMC < 35:
        lb_d_img.config(image=img_c2)
        t_r.insert(INSERT,"su diagnostico es (obesidad grado II)")
    elif IMC > 35 and IMC < 40:
        lb_d_img.config(image=img_c1)
        t_r.insert(INSERT,"su diagnostico es (obesidad grado III)")
    elif IMC > 40:
        lb_d_img.config(image=img_cari)
        t_r.insert(INSERT,"su diagnostico es (obesidad de grado IV)")
    
def abrir_notas_c():
    
    global abrir_notas
    global logo
    abrir_notas = Toplevel()
    abrir_notas.title("Tus notas")
    abrir_notas.resizable(False, False)
    abrir_notas.geometry("400x300")
    abrir_notas.config(bg="sky blue1")

    logo = PhotoImage(file="inge.png")
    lb_logo = Label(abrir_notas, image=logo,bg="sky blue1")
    lb_logo.place(x=210,y=-30)

    lb_c = Label(abrir_notas, text = "Nota 1 = ")
    lb_c.config(bg="light blue", fg="navy", font=("Helvetica", 18))
    lb_c.place(x=30, y=20)
    lb_f = Label(abrir_notas, text = "Nota 2 = ")
    lb_f.config(bg="light blue", fg="navy", font=("Helvetica", 18))
    lb_f.place(x=30, y=60)
    lb_q = Label(abrir_notas, text = "Nota 3 = ")
    lb_q.config(bg="light blue", fg="navy", font=("Helvetica", 18))
    lb_q.place(x=30, y=100)
    lb_l = Label(abrir_notas, text = "Nota 4 = ")
    lb_l.config(bg="light blue", fg="navy", font=("Helvetica", 18))
    lb_l.place(x=30, y=140)

    # caja de texto para valor en centigrados
    entry_c = Entry(abrir_notas, textvariable=n1)
    entry_c.config(bg="sky blue2", fg="navy", font=("Times New Roman", 18), width=6)
    entry_c.focus_set()
    entry_c.place(x=150,y=20)
    entry_w = Entry(abrir_notas, textvariable=n2)
    entry_w.config(bg="sky blue2", fg="navy", font=("Times New Roman", 18), width=6)
    entry_w.focus_set()
    entry_w.place(x=150,y=60)
    entry_r = Entry(abrir_notas, textvariable=n3)
    entry_r.config(bg="sky blue2", fg="navy", font=("Times New Roman", 18), width=6)
    entry_r.focus_set()
    entry_r.place(x=150,y=100)
    entry_l = Entry(abrir_notas, textvariable=n4)
    entry_l.config(bg="sky blue2", fg="navy", font=("Times New Roman", 18), width=6)
    entry_l.focus_set()
    entry_l.place(x=150,y=140)

   # boton para convertir
    bt_aceptar = Button(abrir_notas,text="Aceptar", command=aceptar)
    
    bt_aceptar.place(x=150, y=200, width=100, height=30)




ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Temperatura 1.0")

# tamaño de la ventana
ventana_principal.geometry("800x660")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)
nombre = StringVar()
codigo= StringVar()
pe=StringVar()
al=StringVar()
kf = ["femenino", "Masculino"]
kf_selected = StringVar()
c= ["Ing.Sistemas","Ing.Civíl","Ing.Mecánica","Ing.Química","Ing.Industrial","Ing.Eléctrica","Ing.Electrónica"]
c_selected=StringVar()
n1= StringVar()
n2= StringVar()
n3= StringVar()
n4= StringVar()
nr= StringVar()
img_t = PhotoImage(file="truste.png")
img_f = PhotoImage(file="feli.png")
img_n = PhotoImage(file="normal.png")
img_car= PhotoImage(file="car.png")
img_cari=PhotoImage(file="caritas.png")
img_c1=PhotoImage(file="caritas1.png")
img_c2=PhotoImage(file="caritas2.png")
img_c3=PhotoImage(file="caritas3.png")
img_c4=PhotoImage(file="caritas4.png")
img_fon=PhotoImage(file="fondo.png")



# color de fondo de la ventana
ventana_principal.config(bg="orchid2")
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="plum1", width=780, height=80)
frame_entrada.place(x=10, y=10)
lb_f=Label(frame_entrada,image=img_fon)
lb_f.place(x=0,y=0)
titulo = Label(frame_entrada, text="Conoce tu información")
titulo.config(bg="plum",fg="orchid4", font=("Times New Roman", 30))
titulo.place(x=210,y=10)

frame_b = Frame(ventana_principal)
frame_b.config(bg="plum1", width=780, height=40)
frame_b.place(x=10, y=100)
lb_b = Label(frame_b, text = "Ingresa tu nombre:")
lb_b.config(bg="plum2", fg="orchid4", font=("Times New Roman", 18))
lb_b.place(x=10, y=5)
entry_a = Entry(frame_b,textvariable=nombre)
entry_a.config(bg = "plum2", fg ="orchid4", font=("Times New Roman",18))
entry_a.focus_set()
entry_a.place(x=200,y= 5, width=260 , height=30)
frame_c = Frame(ventana_principal)
frame_c.config(bg="plum1", width=200, height=40)
frame_c.place(x=400, y=100)
lb_c = Label(frame_c, text = "Código:")
lb_c.config(bg="plum2", fg="orchid4", font=("Times New Roman", 18))
lb_c.place(x=10, y=5)
entry_b = Entry(frame_c,textvariable=codigo)
entry_b.config(bg = "plum2", fg ="orchid4", font=("Times New Roman",18))
entry_b.focus_set()
entry_b.place(x=100,y= 5, width=400 , height=30)
button_a = Button(frame_b, text = "Guardar datos",command = guardar)
button_a.config(bg="plum2", fg="orchid4", font =("Timer New Roman",10))
button_a.place(x = 630,y = 3, width=100 , height=35)

button_v = Button(ventana_principal, text = "Salir",command =salir)
button_v.pack()
button_v.config(bg="plum2", fg="orchid4", font =("Timer New Roman",10))
button_v.place(x = 630,y =620, width=100 , height=35)
frame_d = Frame(ventana_principal)
frame_d.config(bg="plum1", width=780, height=40)
frame_d.place(x=10, y=150)
lb_c = Label(frame_d, text = "Ingresa tu peso:")
lb_c.config(bg="plum2", fg="orchid4", font=("Times New Roman", 18))
lb_c.place(x=10, y=5)
entry_b = Entry(frame_d, textvariable=pe)
entry_b.config(bg = "plum2", fg ="orchid4", font=("Times New Roman",18))
entry_b.focus_set()
entry_b.place(x=180,y= 5, width=100 , height=30)
lb_d = Label(frame_d, text = "Ingresa tu altura:")
lb_d.config(bg="plum2", fg="orchid4", font=("Times New Roman", 18))
lb_d.place(x=290, y=5)
entry_b = Entry(frame_d,textvariable=al)
entry_b.config(bg = "plum2", fg ="orchid4", font=("Times New Roman",18))
entry_b.focus_set()
entry_b.place(x=460,y= 5, width=100 , height=30)

frame_e = Frame(ventana_principal)
frame_e.config(bg="plum1", width=780, height=40)
frame_e.place(x=10, y=200)
lb_d = Label(frame_e, text = "sexo:")
lb_d.config(bg="plum2", fg="orchid4", font=("Times New Roman", 18))
lb_d.place(x=10, y=3)
cmb_kf = ttk.Combobox(frame_e, textvariable=kf_selected, values=kf, font=("Helvetica", 12))
cmb_kf.place(x=70, y=7)
lb_d = Label(frame_e, text = "Sistema:")
lb_d.config(bg="plum2", fg="orchid4", font=("Times New Roman", 18))
lb_d.place(x=280, y=3)
cmb_kf = ttk.Combobox(frame_e, textvariable=c_selected, values=c, font=("Helvetica", 12))
cmb_kf.place(x=370, y=7)
lb_e = Label(frame_e, text = "Notas:")
lb_e.config(bg="plum2", fg="orchid4", font=("Times New Roman", 18))
lb_e.place(x=580, y=3)
notas = Button(frame_e, text="Aquí", command=abrir_notas_c)
notas.place(x=650, y=6)
frame_a=Frame(ventana_principal)
frame_a.config(bg="orchid4",width=320,height=40)
frame_a.place(x=10,y=250)
lb_a=Label(frame_a,text="Resultados Académicos")
lb_a.config(bg="orchid4",fg="plum2",font=("Times Nwe Roman",20))
lb_a.place(x=8,y=0)
frame_f= Frame(ventana_principal)
frame_f.config

frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="plum2", width=780, height=90)
frame_resultados.place(x=10, y=300)

# area de texto para los resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="plum2", fg="orchid4", font=("Timer New Roman", 18))
t_resultados.place(x=10,y=10,width=760,height=70)
lb_c_img=Label(t_resultados,bg="plum2")
lb_c_img.place(x=660,y=0)
frame_a=Frame(ventana_principal)
frame_a.config(bg="orchid4",width=320,height=40)
frame_a.place(x=10,y=400)
lb_a=Label(frame_a,text="Resultados Médicos")
lb_a.config(bg="orchid4",fg="plum2",font=("Times Nwe Roman",20))
lb_a.place(x=8,y=0)
frame_ac = Frame(ventana_principal)
frame_ac.config(bg="plum2", width=780, height=160)
frame_ac.place(x=10, y=450)

# area de texto para los resultados
t_r = Text(frame_ac)
t_r.config(bg="plum2", fg="orchid4", font=("Timer New Roman", 18))
t_r.place(x=10,y=10,width=760,height=140)
lb_c_img=Label(t_resultados,bg="plum2")
lb_c_img.place(x=650,y=0)
lb_d_img=Label(t_r,bg="plum2")
lb_d_img.place(x=0,y=28)




ventana_principal.mainloop()
