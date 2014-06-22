"""
Cookie Clicker Simulator
"""

import simpleplot

from math import ceil   # used in ClickerState.time_until

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0
#SIM_TIME = 100.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """

    def __init__(self):
        self.tot_cookies = 0.0
        self.cur_cookies = 0.0
        self.time = 0.0
        self.cps = 1.0
        self.history = [(0.0, None, 0.0, 0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """
        return "\nCurrent time:" + str(self.time) +\
               "\nCurrent cookies:" + str(self.cur_cookies) +\
               "\nCurrent CPS:"+ str(self.cps) +\
               "\nTotoal cookies:" + str(self.tot_cookies)

    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self.cur_cookies

    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self.cps

    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self.time

    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: (0.0, None, 0.0, 0.0)
        """
        return self.history

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        return ceil(cookies/self.cps)

    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0
        """
        if time>0:
            self.time += time
            self.cur_cookies += time*self.cps
            self.tot_cookies += time*self.cps

    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if cost <= self.cur_cookies:
            self.cur_cookies -= cost
            self.cps += additional_cps
            self.history.append((self.time, item_name, cost, self.tot_cookies))
   

def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to game.
    """
    st = ClickerState()
    local_info = build_info.clone()
    while duration >= 0:
        item = strategy(st.cur_cookies, st.cps, duration, local_info)
        cost = local_info.get_cost(item)
        time = st.time_until(cost-st.cur_cookies)
        if time > duration:
            break
        else:
            duration -= time
            st.wait(time)
            st.buy_item(item, cost, local_info.get_cps(item))
            local_info.update_item(item)
    st.wait(duration)
    return st


def strategy_cursor(cookies, cps, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic strategy does not properly check whether
    it can actually buy a Cursor in the time left.  Your strategy
    functions must do this and return None rather than an item you
    can't buy in the time left.
    """
    return "Cursor"

def strategy_none(cookies, cps, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that you can use to help debug
    your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, time_left, build_info):
    return None

def strategy_expensive(cookies, cps, time_left, build_info):
    return None

def strategy_best(cookies, cps, time_left, build_info):
    return None
        
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation with one strategy
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
    run_strategy("Cursor", SIM_TIME, strategy_cursor)

    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    # run_strategy("Best", SIM_TIME, strategy_best)

run()
