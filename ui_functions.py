from main import *

class UIFunctions(ui_windows):

    def animations(self,maxWidth, widget):
        # GET WIDTH
        width = widget.height()
        print(width)
        maxExtend = maxWidth
        standard = 0

        # SET MAX WIDTH
        if width == 0:
            widthExtended = maxExtend
        else:
            widthExtended = standard

        # ANIMATION

        self.animation = QPropertyAnimation(widget, b"maximumHeight")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()
