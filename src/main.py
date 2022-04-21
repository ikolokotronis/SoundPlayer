from pathlib import Path
from tkinter import *
from pygame import mixer
from tkinter import filedialog
import os
import shutil


class SoundPlayer:
    def __init__(self):
        mixer.init()
        self.window = Tk()
        self.song_listbox = Listbox(self.window, selectmode=SINGLE, bg="grey40", fg="black", font=('arial', 15),
                                    height=10, width=42, selectbackground="grey70", selectforeground="black")

        self.song_listbox.place(x=45, y=25)

        self.slider = Scale(self.window,
                            from_=100, to=0,
                            fg="black", bg="grey30",
                            command=self.set_volume,
                            showvalue=False)
        self.slider.set(50)
        self.slider.pack()
        self.slider.place(x=12, y=285)

    def configuration(self):
        self.window.title('Sound Player')
        self.window.geometry("555x400+650+250")
        self.window.resizable(False, False)
        self.window.configure(background='grey23')

        self.menu()
        self.buttons()

    def auto_song_add(self):
        song_list = os.listdir('../media/audio/')
        for song in song_list:
            self.song_listbox.insert(END, song)

    def buttons(self):

        self.play_button = Button(self.window, text="Play", fg="black", bg="forest green", command=self.play_sound)
        self.pause_button = Button(self.window, text="Pause", fg="black", bg="yellow4", command=self.pause_sound)
        self.resume_button = Button(self.window, text="Resume", fg="black", bg="dark green", command=self.resume_sound)

        self.delete_all_button = Button(self.window, text="Delete all ", fg="black", bg="dark red", command=self.delete_all)

        self.pause_button.place(x=185, y=350)
        self.resume_button.place(x=250, y=350)
        self.play_button.place(x=326, y=350)

        self.delete_all_button.place(x=45, y=280)

        
    def mainloop(self):
        self.window.mainloop()

    def play_sound(self):
        active_song = self.song_listbox.get(ACTIVE)
        song_path = os.getcwd() + "/../media/audio/" + active_song
        mixer.music.load(song_path)
        mixer.music.play()

    def pause_sound(self):
        mixer.music.pause()

    def resume_sound(self):
        mixer.music.unpause()

    def set_volume(self, volume):
        mixer.music.set_volume(self.slider.get()/100)

    def menu(self):
        menu = Menu(self.window)
        file_menu = Menu(menu, tearoff=0)
        file_menu.add_command(label="Add song", command=self.add_song)
        file_menu.add_command(label="Delete song", command=self.delete_song)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.window.quit)
        menu.add_cascade(label="Menu", menu=file_menu)

        self.window.config(menu=menu)

    def add_song(self):
        songs = filedialog.askopenfilenames(initialdir=str(Path.home() / "Downloads"), title="Choose a song to add",
                                            filetypes=(("mp3 Files", "*.mp3"),))
        for song in songs:
            song_name = os.path.basename(song)
            shutil.copy2(song, os.getcwd() + "/../media/audio/")
            self.song_listbox.insert(END, song_name)

    def delete_song(self):
        songs = filedialog.askopenfilenames(initialdir="../media/audio//", title="Choose a song to delete",
                                            filetypes=(("mp3 Files", "*.mp3"),))
        for song_path in songs:
            song_list = os.listdir('../media/audio/')
            for song in song_list:
                if os.path.basename(song_path) == song:
                    os.remove(song_path)
                    self.song_listbox.delete(END, song_list.index(song))

    def delete_all(self):
        self.song_listbox.delete(0, END)
        song_list = os.listdir('../media/audio/')
        for song_path in song_list:
            os.remove(os.getcwd() + "/../media/audio/"+song_path)


s = SoundPlayer()
s.configuration()
s.auto_song_add()
s.mainloop()
