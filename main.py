from tkinter import *
from pygame import mixer
from tkinter import filedialog
import os


class SoundPlayer:
    def __init__(self):
        self.window = Tk()
        self.menu()
        self.buttons()
        self.song_listbox = Listbox(self.window, selectmode=SINGLE, bg="white", fg="black", font=('arial', 15),
                                    height=12, width=47, selectbackground="gray", selectforeground="black")
        self.song_listbox.place(x=300, y=200)

        self.song_listbox.grid(column=1, row=0)

    def buttons(self):
        self.play_button = Button(self.window, text="Play", fg="blue", command=self.play_sound)
        self.pause_button = Button(self.window, text="Pause", fg="red", command=self.pause_sound)
        self.resume_button = Button(self.window, text="Resume", fg="green", command=self.resume_sound)

        self.play_button.place(x=300, y=450)
        self.pause_button.place(x=400, y=450)
        self.resume_button.place(x=500, y=450)

    def mainloop(self):
        mixer.init()
        self.window.title('Audio player')
        self.window.geometry("800x600+500+250")
        self.window.mainloop()

    def play_sound(self):
        active_song = self.song_listbox.get(ACTIVE)
        song_path = os.getcwd() + "/media/audio/" + active_song
        mixer.music.load(song_path)
        mixer.music.play()

    def pause_sound(self):
        mixer.music.pause()

    def resume_sound(self):
        mixer.music.unpause()

    # def song_list(self):
    #     song_listbox = Listbox(self.window, selectmode=SINGLE, bg="white", fg="black", font=('arial', 15), height=12,
    #                            width=47,
    #                            selectbackground="gray", selectforeground="black")
    #     song_listbox.place(x=300, y=200)
    #
    #     song_listbox.grid(column=1, row=0)
    #
    #     return song_listbox

    def menu(self):
        menu = Menu(self.window)
        file_menu = Menu(menu, tearoff=0)
        file_menu.add_command(label="Add song", command=self.add_song)
        file_menu.add_command(label="Delete song", command=self.add_song)
        file_menu.add_separator()

        file_menu.add_command(label="Exit", command=self.window.quit)

        menu.add_cascade(label="File", menu=file_menu)
        self.window.config(menu=menu)

    def add_song(self):
        songs = filedialog.askopenfilenames(initialdir="audio/", title="Choose a song",
                                            filetypes=(("mp3 Files", "*.mp3"),))
        for song in songs:
            song = song.replace(os.getcwd() + '/media/audio/', '')
            self.song_listbox.insert(END, song)


s = SoundPlayer()
s.mainloop()
