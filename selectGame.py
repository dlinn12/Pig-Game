import PySimpleGUI as sg


def game_selection():
    sg.theme('Material2')

    difficulty_selection = ''

    diff_layout = [[sg.Button('Oswald (EASY)', key='easy'), sg.Button('Peter (MEDIUM)', key='medium'), sg.Button('Simon (HARD)', key='hard')],
                   [sg.T('You must select a difficulty to proceed!', key='warn', text_color='red', visible=False)]]
    diff_frame = sg.Frame('Choose your difficulty for single player game', diff_layout, key='cont',  element_justification='center', pad=(10, 10), title_location='n')
    diff_box_layout = [[diff_frame]]
    diff_box = sg.Frame('', diff_box_layout, element_justification='center', border_width=0)

    singplayer = sg.InputText('', key='inp_sng', size=(20, 1))
    twoplayer = sg.InputText('', key='inp_twp', size=(20, 1))

    bot_layout = [[sg.Button('Go', key='go_btn'), sg.Exit()]]
    bot_frame = sg.Frame('', bot_layout, element_justification='center', border_width=0)
    bot_box_layout = [[bot_frame]]
    bot_box = sg.Frame('', bot_box_layout, element_justification='center', border_width=0, pad=(10, 10))

    layout = [[sg.T('Pig Game', font=('Georgia', 16))],
              [sg.T('Select Game Mode: Leave Player 2 empty for single player', key='label')],
              [sg.T('Player 1:'), singplayer],
              [sg.T('Player 2:'), twoplayer],
              [diff_box],
              [bot_box]]

    window = sg.Window('Pig Game', layout)

    while True:
        event, values = window.read()
        if event is None or event == 'Exit':
            return []

        elif event == 'go_btn':
            player1 = window['inp_sng'].get()
            player2 = window['inp_twp'].get()
            if player2 == '' and difficulty_selection == '':
                window['warn'].update(visible=True)
            elif player2 == '':
                window.close()
                return [0, player1, difficulty_selection]
            else:
                window.close()
                return [1, player1, player2]

        elif event == 'easy':
            difficulty_selection = 'easy'
            window['easy'].update(disabled=True)
            window['medium'].update(disabled=False)
            window['hard'].update(disabled=False)

        elif event == 'medium':
            difficulty_selection = 'medium'
            window['easy'].update(disabled=False)
            window['medium'].update(disabled=True)
            window['hard'].update(disabled=False)
        elif event == 'hard':
            difficulty_selection = 'hard'
            window['easy'].update(disabled=False)
            window['medium'].update(disabled=False)
            window['hard'].update(disabled=True)
