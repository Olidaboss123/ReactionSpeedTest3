#Layout for the program
from guizero import *
import winsound
import random
import pickle
app = App()



# Function for underline
def underline():
    underline_text = Box(app, width=250, height=1)
    underline_text.bg = "black"

# Functions for start page button
def color_yellow_start():
    start_mode.text_color = "yellow"


def color_black_start():
    start_mode.text_color = "black"



# Function for window change
def change_window_start():
    start_window.show()
    app.hide()
    image_button.bg = "red"
    timer.value = "0"
    white_text.value = "0"
    white_text_2.value="0"
    affirmation_text.value = ""
    age_input.value = 12
    name_input.value = ""
    white_text_3.value = "0"

def change_window_leaderboard():
    leaderboard.show()
    app.hide()

# Functions for finish text
def color_yellow_finish_test():
    finish_test.text_color = "yellow"


def color_black_finish_test():
    finish_test.text_color = "black"


# Functions for quitting application
def color_yellow_quit():
    end_test.text_color = "yellow"


def color_black_quit():
    end_test.text_color = "black"

def quit():
    app.destroy()

#Set starting app and text
app.set_full_screen()
app.bg = "#A2A0A3"
buffer_box_1 = Box(app, width="fill", height=20)
title_box = Box(app, width="fill", height=30)
title = Text(title_box, text = "Reaction Time Test", width="fill", font="Impact")
title.text_size = 20
underline()
buffer_box_5 = Box(app, width="fill", height=50)
options_box = Box(app, width=500, height="fill", align="left", layout="grid")

#Buffer box set between buttons on front page
buffer_box_2 = Box(options_box, align="left", width=200, height=200, grid=[0,0])

#Setting up all the buttons on the start page
start_box = Box(options_box, width=300, height=40, align="left", grid=[0,1], border=True)
start_mode = Text(start_box, width=300, text="Start", font="Gadugi")
start_mode.when_mouse_enters = color_yellow_start
start_mode.when_mouse_leaves = color_black_start
start_mode.text_size = 20
start_mode.when_clicked = change_window_start
start_window = Window(app)
start_window.hide()

buffer_box_3 = Box(options_box, align="left", width=200, height=40, grid=[0,4])

finish_test_box = Box(options_box, align="left", grid=[0,5], width=300, height=40, border=True)
finish_test = Text(finish_test_box, text="Finish test", width=300, font="Gadugi")
finish_test.when_mouse_enters = color_yellow_finish_test
finish_test.when_mouse_leaves = color_black_finish_test
finish_test.when_clicked = change_window_leaderboard
finish_test.text_size = 20


buffer_box_4 = Box(options_box, align="left", width=200, height=40, grid=[0,6])

end_test_box = Box(options_box, align="left", grid=[0,7], width=300, height=40, border=True)
end_test = Text(end_test_box, text="Quit", width=300, font="Gadugi")
end_test.when_mouse_enters = color_yellow_quit
end_test.when_mouse_leaves = color_black_quit
end_test.text_size = 20
end_test.when_clicked = quit
image_box = Box(app, align="right", width="fill", height="fill")
image = Picture(image_box, image="Images/clock.png")

"""
Normal mode page
"""
#Setting class for each students data
class Input:
    age = 0
    name = ""
    time = ""
    average = 0.0

list_of_people = []



#Setting data when user clicks start
def set_info():
    try:
        print(int(name_input.value))
        app.warn("Wrong Input", "Must be a name")
    except ValueError:
        if white_text_3.value == "3":
            info_list = Input()
            info_list.age = age_input.value
            info_list.name = name_input.value
            info_list.time = timer.value
            info_list.average = float(white_text_2.value)
            white_text_all_time.value = "0"
            white_text_counter.value = "0"
            list_of_people.append(info_list)
            file = open("test.pickle", "wb")
            pickle.dump(list_of_people, file)
            file.close()
            start_window.hide()
            app.show()
        else:
            app.warn("Too little", "Has to be 3 tries")

#Function for setting time for button to change colours and for resetting inputs
def timer_change():
    if white_text_3.value < "3":
        global image_button
        checker = True
        time = random.randint(2000, 5000)
        image_button.after(time, change_color)
        image_button.bg = "red"
        timer.value = "0"
        affirmation_text.value = ""
        white_text.value = "0"
        tries = int(white_text_3.value)
        tries += 1
        white_text_3.value = str(tries)
        print(white_text_3.value)
    elif white_text_3.value >= "3":
        app.error("Too much", "Can only do 3 tries")

#Function for detecting if user clicks button at the right time
def do_this():
    global number_text
    if white_text.value == "0":
        timer.cancel(change_color)
        affirmation_text.value = "Wrong Time"
    elif white_text.value == "1":
        timer.cancel(reduce_time)
        affirmation_text.value = "Right Time"
        all_time = float(white_text_all_time.value)
        all_time = all_time + float(timer.value)
        white_text_all_time.value = str(all_time)
        counter = float(white_text_counter.value)
        counter += 1.0
        white_text_counter.value = str(counter)
        average = all_time/counter
        white_text_2.value = average
#Function for changing color of button
def change_color():
    image_button.bg = "green"
    app.repeat(1, reduce_time)
    white_text.value = "1"
#Function for starting timer after button changes color
def reduce_time():
    timer.value = float(timer.value) + 1


timer_list = []
#Creating page with different widgets
start_window.bg = "#a2a0a3"
title = Text(start_window, text="Standard Mode", font="Impact",size=20)
instruction_1 = Text(start_window)
age_and_name_box = Box(start_window, width="fill", height=50)
age_box = Box(age_and_name_box, width="fill", height=50, align="left")
name_box= Box(age_and_name_box, width="fill", height=50, align="right")
age_text = Text(age_box, width= 20, height=50, text="Input age: ", align="left", font="Gadugi")
age_input = Slider(age_box, width=500, height=50, align="left", end=18, start=12)
name_text = Text(name_box, width= 20, height=50, text="Input name: ", align="left", font="Gadugi")
name_input = TextBox(name_box, width=50, height=50, align="left")
start = PushButton(start_window, command=timer_change, text="Start")
buffer_box = Box(start_window, width="fill", height=20)
timer = Text(start_window, text="0")
image_button = Drawing(start_window, height=200, width=200)
image_button.bg = "red"

#Creating the text which is used in checking if data is correct
affirmation_text= Text(start_window, font="Gadugi")
white_text = Text(start_window, text="0", visible=False)
average_text = Text(start_window, text="Average: ")
white_text_2 = Text(start_window, text="0")
white_text_all_time = Text(start_window, text="0", visible=False)
white_text_counter = Text(start_window, text="0", visible=False)
white_text_3 = Text(start_window, text="0", visible=False)
number_text = Text(start_window, text=0, visible=False)
image_button.when_clicked = do_this
finished_test = PushButton(start_window, text="Finish Test", command=set_info)
start_window.set_full_screen()

"""
Leaderboard page
"""

start_time = 0
#Setting up leaderboard page
leaderboard = Window(app)
leaderboard.hide()
leaderboard.bg = "#a2a0a3"

list_of_winners = []

#Function used to calculate the fastest, slowest and average
def calculate_winners(age):
    #Set numbers to check by
    num_1 = 0.0
    num_2 = 1000000.0
    num_3 = 0.0
    average_1 = 0.0
    counter_1 = 0.0
    name_2_value = ""
    name_3_value = ""
    #Open save files to use data
    file = open("test.pickle", "rb")
    test_dict_reconstructed = pickle.load(file)
    file.close()
    #For loop to find slowest value
    for i in range(len(test_dict_reconstructed)):
        if test_dict_reconstructed[i].average > num_1 and test_dict_reconstructed[i].age == float(age):
            print(num_1)
            num_1 = test_dict_reconstructed[i].average
            name_2_value = i
        else:
            continue
    #Set leaderboard value to the number from for loop
    fastest_value.value = str(num_1)
    #If statement used if no data available
    if name_2_value == "":
        name_value_fastest.value = "No-one"
    else:
        name_value_fastest.value = test_dict_reconstructed[name_2_value].name
    #For loop to find fastest value
    for i in range(len(test_dict_reconstructed)):
        if test_dict_reconstructed[i].average < num_2 and test_dict_reconstructed[i].age == float(age):
            num_2 = test_dict_reconstructed[i].average
            name_3_value = i
        else:
            continue
    #Set leaderboard value to the number from for loop
    slowest_value.value = str(num_2)
    #IF statement if no data is available
    if name_3_value == "":
        name_value_slowest.value = "No-one"
    else:
        name_value_slowest.value = test_dict_reconstructed[name_3_value].name
    #For loop to find average speed
    for i in range(len(test_dict_reconstructed)):
        if test_dict_reconstructed[i].age == float(age):
            num_3 += test_dict_reconstructed[i].average
            counter_1 += 1.0
            average_1 = num_3/counter_1
    average_value.value = str(average_1)
def back_to_home_screen():
    leaderboard.hide()
    app.show()

#Setting up page with widgets
combo_box = Box(leaderboard, height=100, width="fill")
leaderboard_title = Text(combo_box, size=20, font="Impact", text="Leaderboard", align="top")
leaderboard_info = Text(combo_box, size=12, font="Gadugi", text="Choose an age and see its stats:", align="bottom")
choose_section = Box(leaderboard, height=150, width="fill",border=True)
Combo = Combo(choose_section, width=75, command=calculate_winners, options=[12,13,14,15,16,17,18])
leaderboard_section = Box(leaderboard, height=300, width="fill", border=True)
bottom_section = Box(leaderboard, height=50, width="fill")
bottom_section_button = PushButton(bottom_section, command=back_to_home_screen, text="Back")
left_section = Box(leaderboard_section,height="fill", width="fill",align="left")
right_section = Box(leaderboard_section, height="fill", width="fill", align="right")
number_section = Box(leaderboard_section, height="fill", width= "fill", align="left", border=True)
number_title = Box(number_section, width="fill", height="fill", border=True)
top_1 = Box(number_section, width="fill", height=50, border=True)
top_2 = Box(number_section, width="fill", height=50, border=True)
top_3 = Box(number_section, width="fill", height=50, border=True)

#Creating  sections for names
name_section = Box(leaderboard_section, height="fill", width="fill", align="right", border=True)
name_title = Box(name_section, width="fill", height="fill",border=True)
name_1 = Box(name_section, width="fill", height=50, border=True)
name_2 = Box(name_section, width="fill", height=50, border=True)
name_3 = Box(name_section, width="fill", height=50, border=True)

#Creating section for ages
age_section = Box(leaderboard_section, height="fill", width="fill", align="right", border=True)
age_title = Box(age_section,width="fill", height="fill", border=True)
age_1 = Box(age_section, width="fill", height=50, border=True)
age_2 = Box(age_section, width="fill", height=50, border=True)
age_3 = Box(age_section, width="fill", height=50, border=True)

#Setting titles for each of the criteria
title_number = Text(number_title, text="Standings", size=30, align="left", font="Gadugi")
title_name = Text(name_title, text = "Name", size=30, align="left", font="Gadugi")
time_number = Text(age_title, text="Time", size=30, align="left", font="Gadugi")

#Setting titles for criteria of speed
average_text = Text(top_1, text="Average", size=12, align="left", font="Gadugi")
fastest_text = Text(top_2, text="Slowest", size=12, align="left", font="Gadugi")
slowest_text = Text(top_3, text="Fastest", size=12, align="left", font="Gadugi")

#Setting text for names
name_value_average = Text(name_1, text="All", size=12, align="left", font="Gadugi")
name_value_fastest = Text(name_2, text="", size=12, align="left", font="Gadugi")
name_value_slowest = Text(name_3, text="", size=12, align="left", font="Gadugi")

#Setting text for speed values
average_value = Text(age_1, text="", size=12, align="left", font="Gadugi")
fastest_value = Text(age_2, text="", size=12, align="left", font="Gadugi")
slowest_value = Text(age_3, text="", size=12, align="left", font="Gadugi")


leaderboard.set_full_screen()
app.display()
