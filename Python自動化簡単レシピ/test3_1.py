import PySimpleGUI as sg

layout = [[sg.Text("あなたの名前は？")],
          [sg.Input()],
          [sg.Button("実行")]]

window = sg.Window("test1",layout)
while True:
    event, values = window.read()
    if event == None:
        break
window.close()
