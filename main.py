import pikepdf
import os
import tkinter as tk
import time
from tkinter.filedialog import askdirectory



root= tk.Tk()
root.title("Sblocca pdf")
    
canvas1 = tk.Canvas(root, width = 600, height = 500)
canvas1.pack()

label1 = tk.Label(root, text='Sblocca PDF con password')
label1.config(font=('helvetica', 14))
canvas1.create_window(300, 25, window=label1)



def set_text(text):
    # entry1.delete(0,END)
    entry1.insert(0,text)
    return

def GetFilePath():
    path =  askdirectory()
    set_text(path)
    return
    



buttonFilePath = tk.Button(text='Seleziona percorso:', command=GetFilePath, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(300, 100, window=buttonFilePath)

entry1 = tk.Entry(root) 
canvas1.create_window(300, 130, window=entry1, width=300 )





label3 = tk.Label(root, text='Inserisci password:')
label3.config(font=('helvetica', 10))
canvas1.create_window(300, 160, window=label3)
entry2 = tk.Entry(root, show='*')
canvas1.create_window(300, 180, window=entry2, width=300)





def ConvertiPdf(file,psw,directory):
    try:
        pdf = pikepdf.open(file,password=psw)
        fileName = file[:-4]
        pdf.save(fileName+'_UNLOCKED.pdf')
        ScriviResult('Operazione completata')
        os.startfile(directory)
    except Exception as ex:
        ScriviResult('Operazione fallita')
    return


def ScriviResult( testo):
        label3 = tk.Label(root, text=testo ,font=('helvetica', 10))
        canvas1.create_window(300, 260, window=label3)
       
        time.sleep(1)
        return 

def Converti():
    directory = str(entry1.get())
    psw = str(entry2.get())
    for entry in os.scandir(directory):
        if entry.path.endswith(".pdf") and entry.is_file():
            #print('Converto il file: ')
            #print(os.path.splitext(entry.path)[0])
            file = os.path.splitext(entry.path)[0]   
            ConvertiPdf(entry.path,psw,directory)





button1 = tk.Button(text='Sblocca pdf', command=Converti, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(300, 210, window=button1)



root.mainloop()
