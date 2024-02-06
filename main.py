#####################################################
# IMPORTS                                           #
#####################################################
import os
import sys
import click

from who_is_on_my_wifi import *

import perfbench
import netbench


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
def networkscan():
    dev = device()
    print(f"""
    PC Name:            {dev[0]}
    PC Product-Name:    {dev[1]}
    MAC Address:        {dev[2]}
    IP Address (host):  {dev[3]}
    IP Address:         {dev[4]}
    Public IP:          {dev[5]}
    PC HostName:        {dev[6]}
    WiFi Name:          {dev[7]}
    Gateway:            {dev[8]}
    DNS 1:              {dev[9]}
    DNS 2:              {dev[10]}
    Password:           {dev[11]}
    Security:           {dev[12]}
    Interface:          {dev[13]}
    Frequency:          {dev[14]}
    Signal:             {dev[15]}
    Channel:            {dev[16]}


    Country:            {dev[17]}
    Region:             {dev[18]}
    City:               {dev[19]}
    Zip Code:           {dev[20]}
    Latitude:           {dev[21]}
    Longitude:          {dev[22]}
    Map:                {dev[23]}
    ISP:                {dev[24]}
    """)

@click.command()
def perfbenchmark():
    perfbench.getBenchmark()
    perfbench.configureBenchmark()
    perfbench.runBenchmark()

@click.command()
@click.argument("ip", type=click.STRING, required=True)
@click.argument('packets', type=click.INT, default=5)
def netbenchmark(ip, packets):
    netbench.runBenchmark(ip, str(packets))


#####################################################
# CLICK GROUP                                       #
#####################################################
app_commands.add_command(hello)         # Test Command
app_commands.add_command(add_todo)      # Test Command

app_commands.add_command(networkscan)   # 0 - Network Scan on Wifi
app_commands.add_command(perfbenchmark)
app_commands.add_command(netbenchmark)
# TBD ...


#####################################################
# MAIN ENTRY POINT                                  #
#####################################################
if __name__ == "__main__":
    app_commands()