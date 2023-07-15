list2: List[str] = []
count = 0

def on_button_pressed_a():
    global list2, count
    list2 = ["usama", "Muhammad", "Walid", "Nabil", "Nour"]
    basic.show_string("" + (list2[randint(0, 4)]))
    count = len(list2)
    basic.show_string("" + str((count)))
    basic.pause(100)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    for index in range(5):
        basic.show_icon(IconNames.HAPPY)
        basic.clear_screen()
        basic.pause(50)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global list2
    list2 = ["usama", "Muhammad", "Walid", "Nabil", "Nour"]
    for value in list2:
        basic.show_string("" + (value))
        basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)
