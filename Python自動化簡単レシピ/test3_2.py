import PySimpleGUI as sg

layout = [[sg.Text("一行目-1"), sg.Text("一行目-2")],
          [sg.Text("二行目-1"), sg.Input("二行目-2")],
          [sg.Button("三行目")]]

window = sg.Window("test2", layout)
while True:
    event, values = window.read()
    if event == None:
        break
window.close()
