import customtkinter
import tkinter

#Variables
#Sizes
WIDTH, HEIGHT = 400, 647
DISPLAY_W, DISPLAY_H = WIDTH - 40, (HEIGHT - 40)*(1/3)
FONT_SIZE = [30, 20, 15]

#Color Variables
MAIN_COLOR = "#FDF1F5"
SECONDARY_COLOR = "#F9ADC7"
HOVER_COLOR = "#FBCDDD"
TEXT_COLOR = "white"
NUM_COLOR = "#FF748C"
MODE = "light"


#Dictionary containing the themes for the change_theme()
THEMES = {"penk": {"main_color":"#FDF1F5",
                  "secondary_color": "#F9ADC7",
                  "hover_color": "#FBCDDD",
                  "text_color": "white",
                   "num_color":"#FF748C",
                  "mode": "light"
                   },
          "blue": {"main_color":"#F1F1FF",
                  "secondary_color": "#36719F",
                  "hover_color": "#86A9C5",
                  "text_color": "white",
                   "num_color":"#5A97C7",
                  "mode": "light"
                   },
          "light": {"main_color":"white",
                  "secondary_color": "#DBDBDB",
                  "hover_color": "#999999",
                  "text_color": "black",
                   'num_color': "gray",
                  "mode": "light"
                   },
          "dark": {"main_color":"#323232",
                  "secondary_color": "#191919",
                  "hover_color": "#232323",
                  "text_color": "white",
                   "num_color":"black",
                  "mode": "dark"
                   },
          }

#The class to create the side panel
class SidePanel(customtkinter.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        #Innitialize the parent class
        super().__init__(master = parent, fg_color = HOVER_COLOR, corner_radius = 10)

        #initialize vairables
        self.window = parent
        self.start_pos = start_pos + 0.01
        self.end_pos = end_pos
        self.height = abs(start_pos - end_pos)

        #animation logic
        self.pos = self.start_pos
        self.in_start_pos = True

        #pantapal dun sa maling kulay
        self.tapal = customtkinter.CTkFrame(self, fg_color = HOVER_COLOR)
        self.tapal.place(rely = 0.98, relx = 0,relwidth = 0.1, relheight = 0.1)

        #displays the side panel on the window
        self.place(rely = self.start_pos, relx = 0.4, relheight = self.height, relwidth = 0.58)

        #displays tet on the panel
        self.label = customtkinter.CTkLabel(self, text = "THEMES", font = ("Arial", FONT_SIZE[1]), text_color = TEXT_COLOR)
        self.label.pack(pady = (30,10))

        #buttons for changing themes, containing the commands change_theme()
        self.PENK = customtkinter.CTkButton(self,
                                            text="PENK",
                                            font=("Arial", FONT_SIZE[1]),
                                            text_color=TEXT_COLOR,
                                            fg_color=SECONDARY_COLOR,
                                            width=200,
                                            hover_color = THEMES["penk"]["secondary_color"],
                                            command=lambda: self.change_theme('penk'))
        self.BLUE = customtkinter.CTkButton(self,
                                             text = "BLUE",
                                             font = ("Arial", FONT_SIZE[1]),
                                             text_color = TEXT_COLOR,
                                             fg_color = SECONDARY_COLOR,
                                             width = 200,
                                            hover_color=THEMES["blue"]["secondary_color"],
                                            command = lambda: self.change_theme('blue'))
        self.LIGHT = customtkinter.CTkButton(self,
                                            text="LIGHT",
                                            font=("Arial", FONT_SIZE[1]),
                                            text_color=TEXT_COLOR,
                                            fg_color=SECONDARY_COLOR,
                                            width=200,
                                             hover_color=THEMES["light"]["secondary_color"],
                                             command=lambda: self.change_theme('light'))
        self.DARK = customtkinter.CTkButton(self,
                                             text="DARK",
                                             font=("Arial", FONT_SIZE[1]),
                                             text_color=TEXT_COLOR,
                                             fg_color=SECONDARY_COLOR,
                                             width = 200,
                                            hover_color=THEMES["dark"]["secondary_color"],
                                            command=lambda: self.change_theme('dark'))

        #displays the buttons
        self.PENK.pack(padx=5, pady=(0, 5))
        self.BLUE.pack(padx=5, pady=(0, 5))
        self.LIGHT.pack(padx=5, pady=(0, 5))
        self.DARK.pack(padx=5, pady=(0, 5))

    def animate(self):
        """Docstring: Animates the side panel depending on whether it is in starting position or not"""
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backward()

    def animate_forward(self):
        """Docstring: Animates the side panel to show"""
        if self.pos < self.end_pos:
            self.pos += 0.01
            self.place(rely = self.pos, relx = 0.4, relheight = self.height, relwidth = 0.58)
            self.after(10, self.animate_forward)
        else:
            self.in_start_pos = False

    def animate_backward(self):
        """Docstring: Animates the side pannel to hide it"""
        if self.pos > self.start_pos:
            self.pos -= 0.01
            self.place(rely = self.pos, relx = 0.4, relheight = self.height, relwidth = 0.58)
            self.after(10, self.animate_backward)
        else:
            self.in_start_pos = True

    def change_theme(self, theme):
        """Docstring: Changes the theme of the calculator"""
        #set the variables global
        global MAIN_COLOR, SECONDARY_COLOR, HOVER_COLOR, TEXT_COLOR, NUM_COLOR, MODE

        #modify the variables according to the THEMES dictionary
        MAIN_COLOR = THEMES[theme]["main_color"]
        SECONDARY_COLOR = THEMES[theme]["secondary_color"]
        HOVER_COLOR = THEMES[theme]["hover_color"]
        TEXT_COLOR = THEMES[theme]["text_color"]
        NUM_COLOR = THEMES[theme]["num_color"]
        MODE = THEMES[theme]["mode"]

        #updates the color on the window
        self.window.update_color()

#Creates the frame for displaying the input and the output
class DisplayFrame(customtkinter.CTkFrame):
    def __init__(self, master, input, output, **kwargs):
        #initialize the parent class
        super().__init__(master, fg_color = NUM_COLOR, border_width = 0, **kwargs)

        #initialize variables
        self.window = master
        self.input = input
        self.output = output

        #create the text boxes for displayign the texts
        self.input_box = customtkinter.CTkEntry(self,
                                                width = DISPLAY_W-20,
                                                height = DISPLAY_H//2 - 20,
                                                bg_color = "transparent",
                                                fg_color = NUM_COLOR,
                                                border_width = 0,
                                                corner_radius = 5,
                                                textvariable = self.input,
                                                font = ("Arial", FONT_SIZE[0]),
                                                state = "disabled",
                                                text_color = TEXT_COLOR)
        self.equal = customtkinter.CTkLabel(self,
                                            text = "=",
                                            height = DISPLAY_H//2 - 20,
                                            font = ("Arial", FONT_SIZE[0]),
                                            text_color = TEXT_COLOR)
        self.output_box = customtkinter.CTkLabel(self,
                                                 textvariable = self.output,
                                                 text = "0",
                                                 height = DISPLAY_H//2 - 20,
                                                 font = ("Arial", FONT_SIZE[0]),
                                                 text_color = TEXT_COLOR)

        #display the created text boxes from earlier
        self.input_box.pack(pady=10, padx=10)
        self.equal.pack(side="left", padx=20)
        self.output_box.pack(side = "right", padx = 10)

class NumButtons(customtkinter.CTkFrame):
    def __init__(self, master, item_list, **kwargs):
        #initialize parent class
        super().__init__(master, fg_color = MAIN_COLOR, **kwargs)

        #initialize variables
        self.window = master
        self.item_list = item_list
        self.width = DISPLAY_W - 20
        self.height = HEIGHT - DISPLAY_H - 20

        #the list the will contain the buttons that will be added to the calculator
        self.button_list = []
        for i, item in enumerate(item_list):
            #create the buttons and add it to the list
            self.add_buton(item)

    def add_buton(self, item):
        """Docstring: Creates a button"""

        #create a button object
        button = customtkinter.CTkButton(self,
                                         text = item,
                                         width = (self.width)/4,
                                         height = (self.height-30)/6,
                                         fg_color = NUM_COLOR if self.window.button_labels[item][0] == "number" else SECONDARY_COLOR,
                                         text_color = TEXT_COLOR,
                                         font = ("Arial", FONT_SIZE[1], "bold"),
                                         hover_color = HOVER_COLOR,
                                         command=lambda: self.process_input(item))

        #display the button according to its position in the input list
        button.grid(row = len(self.button_list)//4, column = (len(self.button_list))%4, padx = 3, pady = 2)
        self.button_list.append(button)

    def process_input(self, button):
        """Docstring: Processes the inputs from the buttons"""

        #checks if the equal sign is already pressed to allow chained operations
        if self.window.eqpressed:
            self.window.input = f"{self.window.ans}"
            self.window.eqpressed = 0

        #checks if the buttons pressed is a number type
        if self.window.button_labels[button][0] == "number":
            self.window.input += button
            self.window.input_display.set(self.window.input)

        #checks if the buttons pressed is a operator type
        if self.window.button_labels[button][0] == "operator":
            self.window.input += self.window.button_labels[button][1]
            self.window.input_display.set(self.window.input)

        #checks if the buttons pressed is a function type
        if self.window.button_labels[button] == "function":
            #checks if the = is pressed to start the computation
            if button == "=":
                self.window.eqpressed = 1

                #try-except for error handling
                try:
                    answer = self.compute()
                    self.window.output.set(answer)
                    self.window.ans = answer
                except Exception as e:
                    # Get the type of the exception


                    error_type = type(e).__name__
                    if error_type == "ZeroDivisionError":
                        self.window.output.set("Math Error")

                    if error_type == "SyntaxError" or error_type == "IndexError":
                        print(error_type)
                        self.window.output.set("Syntax Error")

            #clears the screen if the CLEAR button was pressed
            if button == "CLEAR":
                print("yes")
                self.window.input = ""
                self.window.input_display.set(self.window.input)
                self.window.output.set("0")

            #removes the last letter if the DEL button was clicked
            if button == "DEL":
                self.window.input = self.window.input[:-1]
                self.window.input_display.set(self.window.input)

    def compute(self):
        """Docstring: Computes the input expression"""

        #convert the input into workable string
        cleaned_input = self.clean(self.window.input)

        #use eval() to compute the input
        output = str(round(eval(cleaned_input),10))

        #if the output is so long, use scientific notation
        if len(output) > 15:
            print(len(output))
            new = "{:.10e}".format(float(output))
            return new
        else:
            return output

    def clean(self, input):
        """Docstring: Transforms characters that can't be processed by eval()"""
        _input = input
        output = ""
        while "^" in _input or "√" in _input:
            if "√" in _input:
                index = _input.index("√")
                output = _input[:index] + "(" + _input[index + 1:]
                if _input[index + 1] == "(":
                    while True:
                        if _input[index] == ")":
                            output = output[:index + 1] + "**0.5)" + output[index + 1:]
                            print(output)
                            _input = output
                            break

                        else:
                            index += 1

            if "^" in _input:
                output = _input[:_input.index("^")] + ("**") + _input[_input.index("^") + 1:]
                _input = output
        else:
            output = _input

        output = output.replace("÷", "/")
        output = output.replace("×", "*")
        return output

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__(fg_color= MAIN_COLOR)
        self.title("Calculator")
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.eqpressed = 0
        self.ans = ""

        self.calc_state = "ON"
        self.input_display = tkinter.StringVar()
        self.input = ""
        self.output = tkinter.StringVar()
        self.output.set("0")

        self.display = DisplayFrame(self, self.input_display, self.output)
        self.display.pack(pady = (20,5))

        self.button_labels = {"THEME":"None", "DEL":"function", "CLEAR":"function", "%":["operator", "%"],
                              "(":["operator", "("], ")":["operator", ")"], "√":["operator", "√("], "^":["operator", "^"],
                              "7":["number"], "8":["number"], "9":["number"],"÷":["operator", "÷"],
                              "4":["number"], "5":["number"], "6":["number"], "×":["operator", "×"],
                              "1":["number"], "2":["number"], "3":["number"], "-":["operator", "-"],
                              ".":["operator", "."], "0":["number"], "=":"function", "+":["operator", "+"]}
        self.buttons = NumButtons(self, self.button_labels)
        self.buttons.pack()
        self.side_panel = SidePanel(self,  -0.5, -0.01)

        self.buttons.button_list[0].configure(font = ("Arial", FONT_SIZE[2],"bold"), command = self.side_panel.animate)
        self.bind('<KeyPress>', lambda event: self.update_input(event))

    def update_input(self, event):
        """Docstring: Processes keyboard inputs from user"""
        char = event.char.lower()
        if char in self.button_labels:
            self.buttons.process_input(event.char)

        if char == "x" or char == "*":
            self.buttons.process_input("×")

        if char == "/":
            self.buttons.process_input("÷")

        if char == "c":
            self.buttons.process_input("CLEAR")

        if event.keysym == "BackSpace":
            self.buttons.process_input("DEL")

        if event.keysym == "Return":
            self.buttons.process_input("=")
        print(event)

    def update_color(self):

        """Docstring: Updates colors when the theme was changed"""
        customtkinter.set_appearance_mode(MODE)
        self.configure(fg_color = MAIN_COLOR)
        self.buttons.configure(fg_color = MAIN_COLOR)
        self.display.configure(fg_color = NUM_COLOR)
        self.display.input_box.configure(fg_color = NUM_COLOR, text_color = TEXT_COLOR)
        self.display.equal.configure(text_color = TEXT_COLOR)
        self.display.output_box.configure(text_color = TEXT_COLOR)
        self.side_panel.configure(fg_color = HOVER_COLOR)
        self.side_panel.tapal.configure(fg_color = HOVER_COLOR)
        self.side_panel.label.configure(text_color = TEXT_COLOR)
        self.side_panel.PENK.configure(fg_color = SECONDARY_COLOR, text_color = TEXT_COLOR)
        self.side_panel.BLUE.configure(fg_color = SECONDARY_COLOR, text_color = TEXT_COLOR)
        self.side_panel.LIGHT.configure(fg_color = SECONDARY_COLOR, text_color = TEXT_COLOR)
        self.side_panel.DARK.configure(fg_color = SECONDARY_COLOR, text_color = TEXT_COLOR)

        for i in self.buttons.button_list:
            i.configure(fg_color = NUM_COLOR if self.button_labels[i.cget("text")][0] == "number" else SECONDARY_COLOR, hover_color = HOVER_COLOR, text_color = TEXT_COLOR)

if __name__ == "__main__":
    customtkinter.set_appearance_mode(MODE)
    app = App()
    app.mainloop()
