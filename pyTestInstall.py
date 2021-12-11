# Defines common routines
import os

# COLORED TEXT
# Example:
# prcolor(1, "prints a red text here")
def pr_colour(colour, text):
    test = 1
    colours = [("l_orange", '\033[38;5;209m'),
               ("orange", '\033[38;5;208m'),
               ("d_orange", '\033[38;5;202m'),
               ("l_blue", '\033[38;5;74m'),
               ("blue", '\033[38;5;26m'),
               ("d_blue", '\033[38;5;18m'),
               ("l_green", '\033[38;5;2m'),
               ("green", '\033[38;5;28m'),
               ("d_green", '\033[38;5;22m'),
               ("l_yellow", '\033[38;5;227m'),
               ("yellow", '\033[38;5;11m'),
               ("d_yellow", '\033[38;5;178m'),
               ("l_pink", '\033[38;5;177m'),
               ("pink", '\033[38;5;163m'),
               ("d_pink", '\033[38;5;161m'),
               ("l_purple", '\033[38;5;91m'),
               ("purple", '\033[38;5;54m'),
               ("d_purple", '\033[38;5;53m'),
               ("l_red", '\033[38;5;203m'),
               ("red", '\033[38;5;9m'),
               ("d_red", '\033[38;5;88m'),
               ("brown", '\033[38;5;94m'),
               ("olive", '\033[38;5;58m'),
               ("black", '\033[38;5;232m'),
               ("grey", '\033[38;5;241m'),
               ("white", '\033[38;5;15m'),
               ("cyan", '\033[38;5;6m'),
               ("num_p", '\033[43;30m')]
    
    for col in colours:
        
        if test == 1:
            col_def = col[1]
            print(col_def + "All the Colours \033[0m")
            # print("Col(0): {} Col(1): {} Colour: {}".format(col(0), col(1), colour))
            
            
        else:
            if col[0] == colour:
                col_out = col[1]
                # print("Col(0): {} Col(1): {} Colour: {}".format(col[0], col_out, colour))
                break
            else:
                col_out = '\033[00m'
    # print(col_out + " " + text + '\033[00m')
    if test == 1:
        return "end \033[00m"
    else:
        return col_out + text + '\033[00m'

# CLEAR SCREEN
def clear_screen(lines=100):
    if os.name == 'posix':
        os.system('clear')
    elif os.name in ('nt', 'dos', 'ce'):
        os.system('cls')
    else:
        print('\n' * lines)

# PRINT WITH TAB
def print_tab(text):
    print("\t" + text)

# PAUSE FUNCTION 
def pause():
    input("\n\tHit Enter to Continue...")
    
# Silent PAUSE FUNCTION 
def s_pause():
    input("...")
    

if __name__ == "__main__":
    
    #print("\nFORMAT OUTPUTS \n")
   
    
    # TEST PR_COLOUR
    #print("\nTEST pr_colour Examples:")
    #print(pr_colour("orange","1 RED"))
    # print(pr_colour(2,"2 GREEN"))
    # print(pr_colour(3,"3 YELLOW"))
    # print(pr_colour(4,"4 BLUE"))
    # print(pr_colour(5,"5 PINK"))
    # print(pr_colour(6,"6 CYAN"))
    # print(pr_colour(7,"7 LIGHT GREY?"))
    # print(pr_colour(8,"8 BLACK?"))
    


    # TEST PRINT TAB
    #print("\nTEST print_tab Example:")
    #print_tab("<Print Tabbed>")
    
    
    # words = '\033[33  
    #var ='\033[43;30m' + " RAM 3467 " + '\033[0m'
    #print(var)
  
    
