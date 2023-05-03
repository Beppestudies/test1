def on_gesture_logo_up():
    music.play_melody("G F G A - F E D ", 120)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)
