#####################################################
# IMPORTS                                           #
#####################################################
import os
import sys
import click

import perfbench
import netbench
import client
import server
import scanarp
# import scanself


#####################################################
# CLICK COMMANDS                                    #
#####################################################

@click.group()
def app_commands():
    pass

@click.command()
@click.option("--name", default="World", prompt="Enter a name", help="Name to greet for the hello funtion")
def hello(name):
    click.echo(f"Hello {name}!")

PRIORITIES = {
    "o": "Optional",
    "l": "Low",
    "m": "Medium",
    "h": "High",
    "c": "Critical"
}

@click.command()
@click.argument("priority", type=click.Choice(PRIORITIES.keys()), default="m")
@click.argument("todofile", type=click.Path(exists=False), required=False)
@click.option("--name", "-n", prompt="Enter the todo name", help="Name of the todo item")
@click.option("--description", "-d", prompt="Enter the todo description", help="Description of the todo item")
def add_todo(name, description, priority, todo_file):
    file = todo_file if todo_file is not None else "my_todo.txt"
    with open(file, "a+") as f:
        f.write(f"{PRIORITIES[priority]}: {name} - {description}\n")

@click.command()
def perfbenchmark():
    perfbench.getBenchmark()
    perfbench.configureBenchmark()
    perfbench.runBenchmark()

@click.command()
@click.argument("ip", type=click.STRING, required=True)
@click.argument('packets', type=click.INT, default=10)
def netbenchmark(ip, packets):
    netbench.runBenchmark(ip, str(packets))

@click.command()
@click.option("--debug", help="Enable debug mode for terminal output", type=click.BOOL, default=True)
def startclient(debug):
    client.wait(debug)

@click.command()
@click.option("--debug", help="Enable debug mode for terminal output", type=click.BOOL, default=True)
def startserver(debug):
    server.serve(debug)

@click.command()
def arpscan():
    scanarp.scanall()

# @click.command()
# def selfscan():
#     scanself.scanme()




#####################################################
# CLICK GROUP                                       #
#####################################################
app_commands.add_command(hello)         # Test Command
app_commands.add_command(add_todo)      # Test Command

# app_commands.add_command(selfscan)   # 0 - Network Scan on Wifi
app_commands.add_command(arpscan)
app_commands.add_command(perfbenchmark)
app_commands.add_command(netbenchmark)

app_commands.add_command(startclient)
app_commands.add_command(startserver)
# TBD ...


#####################################################
# MAIN ENTRY POINT                                  #
#####################################################
if __name__ == "__main__":
    app_commands()