from time import sleep
import pyautogui as pg

WAIT: int = 5
pg.FAILSAFE = True
currentSlide: int = 0


def nextSlide() -> None:
    global currentSlide
    match currentSlide:
        case 0:
            pg.press("right")
            currentSlide = 1
        case 1:
            pg.press("left")
            currentSlide = 0


def updateCharts() -> None:
    pg.press("esc")
    sleep(1)
    pg.moveTo(pg.locateOnScreen("tools.png"))
    pg.click()
    pg.moveTo(pg.locateOnScreen("linked.png"))
    pg.click()
    pg.moveTo(pg.locateOnScreen("reload.png"))
    pg.click()
    try:
        pg.moveTo(pg.locateOnScreen("update.png"))
        pg.click()
    except pg.ImageNotFoundException:
        ...


def refreshPresentation() -> None:
    pg.press("f5")
    sleep(1.5)
    pg.moveTo(pg.locateOnScreen("slideshow.png"))
    pg.click()


def main() -> None:
    count: int = 0
    while True:
        count += 1
        nextSlide()
        sleep(WAIT)
        if count == 5:
            updateCharts()
            sleep(1)
            refreshPresentation()
            count = 0
        sleep(WAIT)


if __name__ == '__main__':
    main()
