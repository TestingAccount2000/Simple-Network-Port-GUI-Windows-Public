import os
from subprocess import *
import subprocess
import sys
from tkinter import * 
import tkinter as tk
import tkinter.scrolledtext as st


###PORT RULE METHODS

def addPortRule(port, protocol, action): #protocol can be tcp or udp, action can be DROP or ACCEPT
    ruleName="{action} port {port} on {protocol}: Simple Network Tool Rule".format(action=action, port=port, protocol=protocol)
    command="netsh advfirewall firewall add rule name= \'{ruleName}\' dir=in action={action} protocol={protocol} localport={port}".format(ruleName=ruleName, action=action, port=port, protocol=protocol)
    run(['powershell.exe', command], shell=True)
    

def remPortRule(port, protocol, action): #Same parameters as addPortRule, only change is the delete keyword in the command to delete
    ruleName="{action} port {port} on {protocol}: Simple Network Tool Rule".format(action=action, port=port, protocol=protocol)
    command="netsh advfirewall firewall delete rule name= '{ruleName}'".format(ruleName=ruleName)
    run(['powershell.exe', command], shell=True)
    

def listPorts(): #returns the list of ports
    pw=ROOT_PW
    command='Get-NetFirewallRule'
    result = run(['powershell.exe', "Get-NetFirewallRule"],encoding='UTF-8', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdoutString = str(result.stdout)
    returnString = ''
    for line in stdoutString.splitlines():
        if "Simple Network Tool Rule" in line:
            returnString += line
    return str(returnString)

###GUI AND ITS METHODS

def display_ports():
    global ROOT_PW 
    ROOT_PW = ent_password.get()
    outputtemp = listPorts()
    text_area.delete("1.0","end")
    text_area.insert(tk.INSERT, outputtemp)
    


def addRemRule():
    ruleCheck = True

    portNum = ent_port.get()
    if portNum.isdigit():
        if 0<int(portNum)<65354:
            pass
    else:
        lbl_result["text"] = "Please input integer (1-65353) for port \n(22 for port 22, for example)"
        ruleCheck = False

    portProtocol = ent_protocol.get()
    if portProtocol == "TCP" or portProtocol == "UDP":
        pass
    else:
        lbl_result["text"] = "Please input 'TCP' or\n 'UDP' for Port Protocol"
        ruleCheck = False

    portAction = ent_action.get()
    if portAction == "BLOCK" or portAction == "ALLOW":
        pass
    else:
        lbl_result["text"] = "Please input 'ALLOW' or\n 'BLOCK' for Action"
        ruleCheck = False

    ruleChange = ent_remOrAdd.get()
    if ruleChange == "ADD" or ruleChange == "REMOVE":
        pass
    else:
        lbl_result["text"] = "Please input 'ADD' or\n 'REMOVE' for Rule Change"
        ruleCheck = False

    ROOT_PW = ent_password.get()
    

    if ruleCheck == True:
        if ruleChange == "ADD":
            addPortRule(portNum, portProtocol, portAction)
            lbl_result["text"] = "Rule Added"
        else:
            remPortRule(portNum, portProtocol, portAction)    
            lbl_result["text"] = "Rule Removed"
        

def print2File():
    file1 = open("rules.txt", "w+")
    rules = listPorts()
    file1.write(rules)
    file1.close()
    

# Set up the window
window = tk.Tk()
window.title("Simple Network Port GUI (Windows)")
window.resizable(width=True, height=True)
window.configure(bg='#C0D4D8')

# widget and label in it
frm_entry = tk.Frame(master=window)

ent_port = tk.Entry(width=10)
ent_protocol = tk.Entry(width=10)
ent_action = tk.Entry(width=10)
ent_password = tk.Entry(show="*", width=10)
ent_remOrAdd = tk.Entry(width=10)


lbl_port = tk.Label(text="Port (1-65353)",bg='#C0D4D8')
lbl_protocol = tk.Label(text="Protocol (TCP/UDP)",bg='#C0D4D8')
lbl_action = tk.Label(text="Action (ALLOW/BLOCK)",bg='#C0D4D8')
lbl_password = tk.Label(text="Root Password",bg='#C0D4D8')
lbl_remOrAdd = tk.Label(text="Rule Change (ADD or REMOVE)",bg='#C0D4D8')
lbl_title1 = tk.Label(text="Contact: https://github.com/TestingAccount2000", bg='#C0D4D8')
#lbl_title2 = tk.Label(text="-Windows Edition ", bg='#C0D4D8')


# Create the conversion Button and result display Label
btn_convert = tk.Button(
    master=window,
    text="Press to list port rules",
    command=display_ports
)

btn_addRemRule = tk.Button(
    master=window,
    text="Press to add or remove \n above inputs as a rule",
    command=addRemRule
)


btn_exportRules = tk.Button(
    master=window,
    text="Press to export rules to file\n (Rules.txt)",
    command=print2File
)

lbl_result = tk.Label(master=window, text="PRESS ABOVE FOR PORT RULES", font=("Courier New", 8))


# Use the .grid() geometry manager


ent_port.grid(row=0, column=2, padx = 10, sticky="w")
lbl_port.grid(row=0, column=0, sticky="w")

ent_protocol.grid(row=1, column=2, padx = 10, sticky="w")
lbl_protocol.grid(row=1, column=0, sticky="w")

ent_action.grid(row=2, column=2, padx = 10, sticky="w")
lbl_action.grid(row=2, column=0, sticky="w")

ent_remOrAdd.grid(row=3, column=2, padx = 10, sticky="w")
lbl_remOrAdd.grid(row=3, column=0, sticky="w")

lbl_title1.grid(row=0, column=2, sticky="e")

text_area = st.ScrolledText(window,width = 70,height = 10,font = ("Courier New",8))

window.rowconfigure(9, weight=1)
window.columnconfigure(2, weight=1)
text_area.grid(column = 0, row = 9, pady = 10, padx = 10, columnspan=3, sticky="news")


# Set up the layout using the .grid() geometry manager
btn_addRemRule.grid(row=5, columnspan=3, pady=10)
btn_exportRules.grid(row=6, columnspan=3)
btn_convert.grid(row=7, columnspan=3, pady=10)
lbl_result.grid(row=8, column=0, columnspan = 3) 


################################################################

# Run the application


if __name__ == "__main__":
    window.mainloop()
    
