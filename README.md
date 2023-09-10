# Windows-Network-Port-GUI-Tool

## Introduction

This is a simple, open source tool to allow the adding of custom firewall rules based on port. It allows you to block or allow certain ports by adding them to your Windows Firewall list. You can then list your custom firewall rules or export them to a text document in the same directory as where the script or the compiled .exe is. 

This distributable comes in two forms within each separate directory: a python script "Simple Network Port GUI (Windows).py" and a pre-compiled executable, "Simple Network Port GUI (Windows).exe"

## UI


<img src="https://github.com/TestingAccount2000/Simple-Network-Port-GUI-Windows/assets/98635532/46c3b4f3-a71b-4e0e-8c11-d75c3b5b6c5d" alt="GUI Image" width="500">





## Commonly Asked Questions

Q: “When I run the executable or python code, I get no outputs or response?”

A: Run the file or executable as administrator. Unfortunately you need to typically on accounts, so if you have any qualms about admin executables, review the code yourself then run the python file. Alternatively, make sure you have some custom port rules already made, this program will not display ones made in other programs.


Q: “My antivirus is saying the executable is a Trojan Virus?” 

A: Antivirus software will (rightfully) recognize random, unsigned executables as viruses typically. This is not one, but if you rather not take the risk just review the python code and run it yourself.

## Future Planned Improvements

1. Replace port rule inputs with radio buttons where applicable (for two choice options)
2. Improve speed of operations
3. Add option to ask user for elevated permissions at start of script
4. Incorporate the entire firewall ruleset in Windows for editting




