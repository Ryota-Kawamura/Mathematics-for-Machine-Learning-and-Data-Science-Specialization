import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import ipywidgets as widgets
from ipywidgets import interact_manual



class monty_hall_game:
    def __init__(self) -> None:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
        self.fig = fig
        self.ax = ax1
        self.results_ax = ax2
        self.memory_wins = {"switch": 0, "stay": 0}
        self.memory_games = {"switch": 0, "stay": 0}
        self.games_finished = 0
        self.start()

        self.cpoint = self.fig.canvas.mpl_connect("button_press_event", self.click_plot)

    def start(self) -> None:

        self.ax.clear()
        values = [10, 10, 10]
        door_numbers = ["Door 1", "Door 2", "Door 3"]

        self.ax.spines["top"].set_color("none")
        self.ax.spines["right"].set_color("none")
        self.ax.spines["left"].set_color("none")
        self.ax.get_yaxis().set_visible(False)

        self.ax.bar(
            door_numbers,
            values,
            color=["brown", "brown", "brown"],
            width=0.6,
            edgecolor=["black", "black", "black"],
        )
        self.ax.set_title(f"New game started, pick any door.")

        self.prize_coordinates = [-0.15, 0.85, 1.85]

        self.doors, self.winner_index = self.init_monty_hall()
        self.prizes = list(map(lambda x: "GOAT" if x == 0 else "CAR", list(self.doors)))

        self.choice = None
        self.switch = None
        self.temptative_final_door = None
        self.final_choice = None
        self.first_pick = True
        self.game_over = False
        self.won = None
        self.ilegal_move = False

    def click_plot(self, event):
        
        if event.inaxes in [self.ax]:
            if self.game_over:
                self.start()
                return

            # if self.choice and self.final_choice:
            #     self.start()

            if self.first_pick:
                self.first_pick_mtd(event.xdata)
            else:
                self.second_pick_mtd(event.xdata)

            if ((self.choice is not None) or (self.final_choice is not None)) and (
                not self.ilegal_move
            ):
                self.update_bar_chart()

    def first_pick_mtd(self, x_coord):

        if (x_coord >= -0.3) and (x_coord <= 0.3):
            self.choice = 0
        elif (x_coord >= 0.7) and (x_coord <= 1.3):
            self.choice = 1
        elif (x_coord >= 1.7) and (x_coord <= 2.3):
            self.choice = 2
        else:
            self.choice = None
#             print("click a door")
            # self.ax.set_title(f"Click on a door to move forward")
            self.start()

    def second_pick_mtd(self, x_coord):

        if (x_coord >= -0.3) and (x_coord <= 0.3):
            self.final_choice = 0
        elif (x_coord >= 0.7) and (x_coord <= 1.3):
            self.final_choice = 1
        elif (x_coord >= 1.7) and (x_coord <= 2.3):
            self.final_choice = 2
        else:
            self.final_choice = None
#             print("click a door")
            # self.ax.set_title(f"Click on a door to move forward")
            self.start()

        if self.final_choice == self.opened_door:
            self.ax.set_title(
                f"You selected the opened door.\nThis game doesn't count"
            )
            self.ilegal_move = True
            self.game_over = True

    def update_bar_chart(self):

        if self.first_pick:
            values = [10, 10, 10]
            colors = ["brown", "brown", "brown"]
            edge_colors = ["black", "black", "black"]
            linewidths = [1, 1, 1]
            # colors[self.choice] = "red"
            edge_colors[self.choice] = "red"
            linewidths[self.choice] = 5

            door_numbers = ["Door 1", "Door 2", "Door 3"]
            self.opened_door = self.open_door()
            # values[opened_door] = 0

            colors[self.opened_door] = "gray"

            self.ax.clear()
            self.ax.text(
                self.prize_coordinates[self.opened_door],
                5,
                f"{self.prizes[self.opened_door]}",
            )

            # self.ax.text(0,10,f"You chose door {self.choice} and host opened door {opened_door}")
            # self.ax.text(0.4,5,f"{self.doors}")
            # self.results_ax.bar(door_numbers, values, color = colors,width = 0.6, edgecolor = ['black', 'black', 'black'])

            self.ax.bar(
                door_numbers,
                values,
                color=colors,
                width=0.6,
                edgecolor=edge_colors,
                linewidth=linewidths,
            )
            self.ax.set_title(
                f"You chose door {self.choice+1} and host opened door {self.opened_door+1}.\nDecide your final door."
            )
            self.first_pick = False
        else:
            values = [10, 10, 10]
            colors = ["gray", "gray", "gray"]
            colors[self.winner_index] = "green"
            edge_colors = ["black", "black", "black"]
            edge_colors[self.final_choice] = "red"
            linewidths = [1, 1, 1]
            linewidths[self.final_choice] = 5
            door_numbers = ["Door 1", "Door 2", "Door 3"]
            self.ax.clear()
            for i in range(3):
                self.ax.text(self.prize_coordinates[i], 5, f"{self.prizes[i]}")
            self.ax.bar(
                door_numbers,
                values,
                color=colors,
                width=0.6,
                edgecolor=edge_colors,
                linewidth=linewidths,
            )
            self.game_over = True
            self.check_if_switch()
            msg = " " if self.switch else " NOT "
            self.ax.set_title(
                f"You decided{msg}to switch and chose door #{self.final_choice+1}\n You got a {self.prizes[self.final_choice]}"
            )

            self.games_finished += 1
            if self.switch:
                self.memory_wins["switch"] += self.doors[self.final_choice]
                self.memory_games["switch"] += 1
            else:
                self.memory_wins["stay"] += self.doors[self.final_choice]
                self.memory_games["stay"] += 1

            self.update_results_chart()

    def update_results_chart(self):
        self.results_ax.clear()
        self.results_ax.set_title(
            f"Games finished: {self.games_finished}\nGames you switched: {self.memory_games['switch']}, Games you stayed: {self.memory_games['stay']}"
        )
        self.results_ax.scatter(
            ["switch", "stay"],
            [
                self.memory_wins["switch"] / self.memory_games['switch'],
                self.memory_wins["stay"] / self.memory_games['stay'],
            ],
            s=350,
        )
        self.results_ax.set_ylim(0, 1)

    def check_if_switch(self):
        self.switch = False if self.choice == self.final_choice else True

    def init_monty_hall(self):
        doors = np.array([0, 0, 0])
        winner_index = np.random.randint(0, 3)
        doors[winner_index] = 1

        return doors, winner_index

    def open_door(self):
        openable_doors = [
            i for i in range(3) if i not in (self.winner_index, self.choice)
        ]
        door_to_open = np.random.choice(openable_doors)

        return door_to_open

    


def success_rate_plot(f):
    def _plot(switch, n_iterations):
        wins = 0
        # iterations = 1000

        for _ in range(n_iterations):
                wins += f(switch=switch)

        win_rate = wins / n_iterations
        loss_rate = 1 - win_rate

        fig, ax = plt.subplots(1, 1, figsize=(10, 4))
        ax.pie(
            [win_rate, loss_rate],
            labels=["Win a car", "Win... a goat?"],
            colors=sns.color_palette("pastel")[2:],
            autopct="%.0f%%",
        )

        msg = "always" if switch else "never"
        ax.set_title(f"Win rate if you {msg} switch doors ({n_iterations} simulations)")
        plt.show()
        
    def _plot_generalized(switch, n_iterations, n = 3, k = 1):
        wins = 0
        # iterations = 1000

        for _ in range(n_iterations):
            wins += f(switch=switch, n = n, k = k)

        win_rate = wins / n_iterations
        loss_rate = 1 - win_rate

        fig, ax = plt.subplots(1, 1, figsize=(12, 4))
        ax.pie(
            [win_rate, loss_rate],
            labels=["Win a car", "Win... a goat?"],
            colors=sns.color_palette("pastel")[2:],
            autopct="%.0f%%",
        )

        msg = "always" if switch else "never"
        ax.set_title(f"Win rate if you {msg} switch doors ({n_iterations} simulations)")
        plt.show()


    n_iterations_selection = widgets.SelectionSlider(
        options=[1, 10, 100, 1000],
        value=1,
        description="# iterations",
        disabled=False,
        continuous_update=False,
        orientation="horizontal",
        readout=True,
    )

    strategy_selection = widgets.RadioButtons(
        options=[True, False],
        value=False,
        description="Switch Doors?",
        disabled=False,
    )
    
    if f.__qualname__ == 'monty_hall':
        
        interact_manual(
        _plot, switch=strategy_selection, n_iterations=n_iterations_selection,
    )
        
    
        
    if f.__qualname__ == 'generalized_monty_hall':
        
        disabled = False

        n_selection = widgets.SelectionSlider(
        options=range(3,101),
        value=3,
        description="n",
        disabled=disabled,
    )
        
        
        k_selection = widgets.SelectionSlider(
        options=range(0,99),
        value=1,
        description="k",
        disabled=disabled,
    )
        
        interact_manual(
        _plot_generalized, switch=strategy_selection, n_iterations=n_iterations_selection, n = n_selection, k = k_selection
    )
