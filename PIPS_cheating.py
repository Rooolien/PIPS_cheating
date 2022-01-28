## This function helps you to cheat on your PIPS assignment Q3.2P.1 - Q3.2P.5. Give the number of the assignment
## you want to cheat on in the function and you will get tips and tricks!!


def cheat(number):
    if number == 1:
        print("Solution: Simulate data with 'np.random.normal' and use 'plt.boxplot' and 'sns.stripplot' for plotting.")
    elif  number == 2:
        print("Sorry, I don't give you this solution, because this assignment took me also more than 2 hours....")
    elif number == 3:
        print("Solution: Load data and convert to pandas dataframe, make the plot with 'sns.regplot'.")
    elif number == 4:
        print("Solution: Create subplots with 'plt.subplot()', create plots with 'sns.heatmap', and 'sns.kdeplot'.")
    elif number == 5:
        print("Solution: Use a string as an argument in the function and use an 'if-elif-else-statement' in the function")
    else:
        print("You have to this exercise by yourself!")
# Give the number of the assignment you want to cheat on between the brackets, e.g. 2

cheat(2)