from tkinter import *
from tkinter import messagebox
from tcp_client import Client


class Interface:
    def window_c(self):
        self.window = Tk()
        self.window.title('Авторизація')
        self.window.geometry('450x230')
        self.window.resizable(False, False)

        self.font_header = ('Arial', 15)
        self.font_entry = ('Arial', 12)
        self.label_font = ('Arial', 11)
        self.base_padding = {'padx': 10, 'pady': 8}
        self.header_padding = {'padx': 10, 'pady': 12}


    def clicked(self):
        client.connection()

        username = self.username_entry.get()
        password = self.password_entry.get()

        message = client.send_message(username, password)

        messagebox.showinfo('Інформація', f'{message}')


    def entry(self):
        main_label = Label(self.window, text='Авторизація', font=self.font_header, justify=CENTER, **self.header_padding)
        main_label.pack()

        self.username_label = Label(self.window, text='Ім`я користувача', font=self.label_font , **self.base_padding)
        self.username_label.pack()

        self.username_entry = Entry(self.window, bg='#fff', fg='#444', font=self.font_entry)
        self.username_entry.pack()

        self.password_label = Label(self.window, text='Пароль', font=self.label_font , **self.base_padding)
        self.password_label.pack()

        self.password_entry = Entry(self.window, bg='#fff', fg='#444', font=self.font_entry)
        self.password_entry.pack()

        send_btn = Button(self.window, text='Увійти', command=self.clicked)
        send_btn.pack(**self.base_padding)


if __name__ == '__main__':

    client = Client()
    interface = Interface()

    interface.window_c()
    interface.entry()
    interface.window.mainloop()