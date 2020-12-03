# START: IMPORTS
from Layouts import LayoutStart
from StartDiscordRPC import StartDiscordRPC
from ActivityDetail import SetActivityDetail, ListDetails
from ActivityState import SetActivityState, ListStates
# END: IMPORTS


# START: ACTIVITY DETAILS DATA
details = [
    "🦅 ADZU-Ateneo de Zoom University",
    "🇵🇭 FILI12(FF)-Panitikan ng Pilipinas",
    "📐 MATH21(G)-University Precalculus",
    "🦅 INTACT11(O2)-Introduction to Ateneo Culture and Traditions",
    "💻 CSCI21(B)-Introduction to Programming I"
]
# END: ACTIVITY DETAILS DATA

# START: ACTIVITY STATES DATA
states = [
    "🏫 A/Sync Academics",
    "🎥 Having Synchronous Class",
    "📚 Doing Asynchronous Stuff",
    "⛔ DO NOT DISTURB",
    "😛 SLACKING OFF",
    "🥴 NOT LISTENING",
    "🧐 PRODUCTIVE",
    "👻 DYING"
]
# END: ACTIVITY STATES DATA


# START: START ADZU-RPC CLI
LayoutStart()
# END: START ADZU-RPC CLI

displayDetail = SetActivityDetail(details)
displayState = SetActivityState(states)

# START: START DISCORD RPC
StartDiscordRPC(displayDetail, displayState)
# END: START DISCORD RPC
