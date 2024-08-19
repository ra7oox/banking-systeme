#Ra7oox
from tkinter import *
from tkinter import messagebox,simpledialog  

tries = 3
login = "0000"
password = "0000"
sold = 100

root = Tk()
root.title("bank system")
root.geometry("400x400")

login_label = Label(root, text="Login")
login_label.place(x=40, y=20)

login_entry = Entry(root)
login_entry.place(x=100, y=20)

password_label = Label(root, text="Password")
password_label.place(x=40, y=50)

password_entry = Entry(root, show="*")
password_entry.place(x=100, y=50)

def page2():
    global tries, root2
    
    # Check if both login and password are correct
    if login_entry.get() == login and password_entry.get() == password:
        messagebox.showinfo("Success", "Connected successfully")
        root.destroy()
        
        root2 = Tk()
        root2.geometry("400x400")
        root2.title("Bank System")
        
        def deposit():
            global sold
            amount = simpledialog.askfloat("Deposit", "Enter amount to deposit:")
            if amount and amount > 0:
                sold += amount
                messagebox.showinfo("Success", f"{amount} deposited. New balance: {sold} DH ")
            else:
                messagebox.showwarning("Invalid", "Please enter a valid amount.")
        
        def withdrawal():
            global sold
            amount = simpledialog.askfloat("Withdraw", "Enter amount to withdraw:")
            if amount and amount > 0:
                if amount <= sold:
                    sold -= amount
                    messagebox.showinfo("Success", f"{amount} withdrawn. New balance: {sold} DH")
                else:
                    messagebox.showwarning("Insufficient Funds", "You do not have enough balance.")
            else:
                messagebox.showwarning("Invalid", "Please enter a valid amount.")
        
        def show():
            messagebox.showinfo("Balance", f"Current balance: {sold} DH")
        
        btn_deposit = Button(root2, text="Deposit", command=deposit)
        btn_deposit.place(x=50, y=20)
        
        btn_withdraw = Button(root2, text="Withdraw", command=withdrawal)
        btn_withdraw.place(x=50, y=50)
        
        btn_show = Button(root2, text="Show Balance", command=show)
        btn_show.place(x=50, y=80)
    
    else:
        tries -= 1
        messagebox.showwarning("Warning", "Login or password incorrect")
        
        if tries == 0:
            messagebox.showerror("Blocked", "Account blocked")
            root.destroy()  # Close the login window
            # root2.destroy() is not necessary because root2 doesn't exist if login fails

btn_login = Button(root, text="Login", command=page2)
btn_login.place(x=40, y=80)

root.mainloop()
