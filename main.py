from time import sleep
import pyautogui as pg

WAIT: int = 5
pg.FAILSAFE = True
currentSlide: int = 0


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def nextSlide() -> None:
    global currentSlide
    match currentSlide:
        case 0:
            print("Changing to leaderboards")
            pg.press("right")
            currentSlide = 1
        case 1:
            print("Changing to logo")
            pg.press("left")
            currentSlide = 0


def updateCharts() -> None:
    try:
        print("Pressing escape")
        pg.press("esc")
        sleep(1)
        pg.moveTo(pg.locateOnScreen(resource_path("tools.png")))
        print("Clicking tools")
        pg.click()
        pg.moveTo(pg.locateOnScreen(resource_path("linked.png")))
        print("Clicking linked objects")
        pg.click()
        pg.moveTo(pg.locateOnScreen(resource_path("reload.png")))
        print("Clicking reload")
        pg.click()
        pg.moveTo(pg.locateOnScreen(resource_path("update.png")))
        print("Clicking update")
        pg.click()
    except pg.ImageNotFoundException:
        print("Could not find one of the images")


def refreshPresentation() -> None:
    sleep(0.75)
    pg.moveTo(pg.locateOnScreen(resource_path("slideshow.png")))
    print("Entering presentation mode")
    pg.click()


def main() -> None:
    count: int = 0
    while True:
        count += 1
        print(f"{count = }")
        nextSlide()
        sleep(2)
        if count == 3:
            updateCharts()
            sleep(1)
            refreshPresentation()
            count = 1
        sleep(WAIT)


if __name__ == '__main__':
    print("Make sure to be on the slideshow in present mode! App will start in 15 seconds...")
    sleep(15)
    main()
