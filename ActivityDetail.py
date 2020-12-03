def SetActivityDetail(details):
    # START: CONDITIONAL SETTING DETAIL LOGIC
    displayDetail = ""
    isDefaultDetail = True

    qSetOwnDetail = input(
        '\nWould you like to choose your own detail? (Y/n): ')
    isDefaultDetail = False if qSetOwnDetail.lower() == 'y' else True

    # IF: DEFAULT DETAIL
    if isDefaultDetail:
        displayDetail = details[0]
    # END: DEFAULT DETAIL

    # IF: CHOOSE OWN DETAIL
    else:
        qUsePresetDetails = input(
            '> Use Preset Details? (Y/n): ')
        isUsePresetDetails = True if qUsePresetDetails.lower() == 'y' else False
        # START: USE PRESET DETAIL
        if isUsePresetDetails:
            ListDetails(details)
            getWhichDetail = input(
                ':: Enter the number of your chosen detail?: ')
            displayDetail = details[int(getWhichDetail)-1]
        # END: USE PRESET DETAIL

        # START: TYPE OWN DETAIL
        else:
            qWhatDetail = input(':: Enter Detail: ')
            displayDetail = qWhatDetail
        # END: TYPE OWN DETAIL
    # END: CHOOSE OWN DETAIL
    # END: CONDITIONAL SETTING DETAIL LOGIC
    print('::👌 Ayt Got It!!!')
    print("\n- - - - - - - - - -")
    return displayDetail


def ListDetails(details):
    print("\n- - - - - - - - - -")
    print("List of Details:: ")
    order = 0
    for each_detail in details:
        order = order + 1
        print(str(order) + ' - ' + each_detail)
    print("- - - - - - - - - -")
