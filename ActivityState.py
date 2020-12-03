def SetActivityState(states):
    # START: CONDITIONAL SETTING STATE LOGIC
    displayState = ""
    isDefaultState = True

    qSetOwnState = input('\nWould you like to choose your own state? (Y/n): ')
    isDefaultState = False if qSetOwnState.lower() == 'y' else True

    # IF: DEFAULT STATE
    if isDefaultState:
        displayState = states[0]
    # END: DEFAULT STATE

    # IF: CHOOSE OWN STATE
    else:
        qUsePresetStates = input(
            '> Use preset States? (Y/n): ')
        isUsePresetStates = True if qUsePresetStates.lower() == 'y' else False
        # START: USE PRESET STATES
        if isUsePresetStates:
            ListStates(states)
            getWhichState = input(
                ':: Enter the number of your chosen state?: ')
            displayState = states[int(getWhichState)-1]
        # END: USE PRESET STATES

        # START: TYPE OWN STATE
        else:
            qWhatState = input(':: Enter State: ')
            displayState = qWhatState
        # END: TYPE OWN STATE
    # END: CHOOSE OWN STATE
    # END: CONDITIONAL SETTING STATE LOGIC
    print('::👌 Ayt Got It!!!')
    return displayState


def ListStates(states):
    print("\n- - - - - - - - - -")
    print("List of States:: ")
    order = 0
    for each_state in states:
        order = order + 1
        print(str(order) + ' - ' + each_state)
    print("- - - - - - - - - -")
