import PySimpleGUI as sg
from player import Player
from selectGame import game_selection
import time


def init_game(mode, p1, p2):
    if mode == 0:
        p1 = Player(p1)
        p2 = Player(p2)
    else:
        p1 = Player(p1)
        p2 = Player(p2)
    return p1, p2


mode = game_selection()
player1, player2 = init_game(mode[0], mode[1], mode[2])

sg.theme("Material2")

display = sg.T('Wecome to Pig Game', size=(30, 3), key='display')
display_box = sg.Frame('', layout=[[display]], relief='flat')
player1_score = sg.T('0', key='player1_score', size=(4, 1),)
player2_score = sg.T('0', key='player2_score', size=(4, 1))
turn_score = sg.T('0', key='turn_score', size=(4, 1))
roll_ptns = sg.T('0', key='roll_ptns')
score_box = sg.Frame('', [[sg.T('Turn Score:'), turn_score, sg.T(' ' * 10), sg.T('Roll:'), roll_ptns]], relief='flat')
btn_roll = sg.Button('ROLL', key='btn_roll')
btn_hold = sg.Button('HOLD', key='btn_hold')
player1_name = sg.T(player1.name + ':', font=('Helvetica', 16))
player2_name = sg.T(player2.name + ':', font=('Helvetica', 16))
player1_box = sg.Frame('', layout=[[player1_name, player1_score]], relief='flat')
player2_box = sg.Frame('', layout=[[player2_name, player2_score]], relief='flat')
control_box = sg.Frame('', [[btn_roll, btn_hold, sg.T(' ' * 28), sg.Exit()]], pad=(10, 5), relief='flat')

layout = [[display_box],
          [player1_box, player2_box],
          [score_box],
          [control_box]]


window = sg.Window('Pig Game', layout)


def switch(curr):
    if curr is player1:
        return player2
    else:
        return player1


def startup():
    global player1
    window.finalize()
    window['display'].update('Welcome to Pig Game\nClick ROLL to begin')
    while True:
        event, values = window.read()
        if event is None or event == 'Exit':
            window.close()
        elif event == 'btn_roll':
            window['display'].update(player1.name + '\'s turn\nClick ROLL')
            break


def check_win(score):
    return score >= 100


startup()
current_player = player1

while True:
    event, values = window.read()
    if event is None or event == 'Exit':
        break
    if event == 'btn_roll':
        turn = current_player.take_turn()
        if turn == 0:
            current_player = switch(current_player)
            window['turn_score'].update('0')
            window['roll_ptns'].update('0')
            window['display'].update(current_player.name + '\'s turn\nClick ROLL')
        else:
            window['turn_score'].update(str(current_player.turn))
            window['roll_ptns'].update(str(current_player.last_roll))

    if event == 'btn_hold':
        current_player.hold()
        window['turn_score'].update(0)
        window['roll_ptns'].update(0)
        window['player1_score'].update(player1.score)
        window['player2_score'].update(player2.score)
        if check_win(current_player.score):
            sg.popup('WINNER', current_player.name + ' has won the match with ' + str(current_player.score) + ' points!')
            break
        else:
            current_player = switch(current_player)
            window['display'].update(current_player.name + '\'s turn\nClick ROLL')

window.close()
