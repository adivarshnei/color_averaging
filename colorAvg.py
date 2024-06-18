import copy
import random
import math

import pygame


board1 = []
board2 = []


class screenDefine:
    def __init__(self, screenParams):
        pygame.init()
        self.screen = pygame.display.set_mode(screenParams["dimensions"])
        pygame.display.set_caption(screenParams["caption"])
        self.screen.fill(screenParams["bgColor"])

    def returnScreenVar(self):
        return self.screen


def initBoardAnim(screen, screenParams):
    boardPixelCol = []
    global board1
    global board2

    for i in range(int(screenParams["dimensions"][0] / screenParams["size"])):
        subList = []
        subList1 = []

        for j in range(int(screenParams["dimensions"][1] / screenParams["size"])):
            n = int(255 * random.random())
            subList.append(n)
            subList1.append(0)
        boardPixelCol.append(subList)
        board1.append(subList1)
        board2.append(subList1)

    for i in range(int(screenParams["dimensions"][0] / screenParams["size"])):
        for j in range(int(screenParams["dimensions"][1] / screenParams["size"])):
            pygame.draw.rect(
                screen.returnScreenVar(),
                (boardPixelCol[i][j], boardPixelCol[i][j], boardPixelCol[i][j]),
                pygame.Rect(
                    i * screenParams["size"],
                    j * screenParams["size"],
                    (i + 1) * screenParams["size"],
                    (j + 1) * screenParams["size"],
                ),
            )

    pygame.display.update()

    board1 = copy.deepcopy(boardPixelCol)


def animate(screen, screenParams, counter):
    global board1
    global board2

    font = pygame.font.SysFont("courier", 32)

    while True:
        for i in range(int(screenParams["dimensions"][0] / screenParams["size"])):
            for j in range(int(screenParams["dimensions"][1] / screenParams["size"])):
                pygame.draw.rect(
                    screen.returnScreenVar(),
                    (board1[i][j], board1[i][j], board1[i][j]),
                    pygame.Rect(
                        i * screenParams["size"],
                        j * screenParams["size"],
                        (i + 1) * screenParams["size"],
                        (j + 1) * screenParams["size"],
                    ),
                )
        for i in range(int(screenParams["dimensions"][0] / screenParams["size"])):
            for j in range(int(screenParams["dimensions"][1] / screenParams["size"])):
                val = board1[i][j]
                divVal = 5

                if i != 0:
                    val += board1[i - 1][j]
                if i != int(screenParams["dimensions"][0] / screenParams["size"]) - 1:
                    val += board1[i + 1][j]
                if j != 0:
                    val += board1[i][j - 1]
                if j != int(screenParams["dimensions"][1] / screenParams["size"]) - 1:
                    val += board1[i][j + 1]
                if i == 0:
                    divVal -= 1
                if i == int(screenParams["dimensions"][0] / screenParams["size"]) - 1:
                    divVal -= 1
                if j == 0:
                    divVal -= 1
                if j == int(screenParams["dimensions"][1] / screenParams["size"]) - 1:
                    divVal -= 1
                val /= divVal

                # sin_divisor = counter[0]
                # sin_divisor = 100

                # sin_val = math.sin((sin_divisor * val * math.pi) / 255) * (
                #     255 / sin_divisor
                # )

                # val += sin_val

                # val = 255 if val > 255 else val
                # val = 0 if val < 0 else val

                val = int(val)

                board2[i][j] = val

        text = font.render(f"{counter[0]}", True, [255, 255, 255])
        text_rect = text.get_rect()
        text_rect.center = (
            screenParams["dimensions"][0] // 2,
            screenParams["dimensions"][1] // 2,
        )

        screen.returnScreenVar().blit(source=text, dest=text_rect)

        pygame.time.delay(10)
        pygame.display.update()

        counter[0] -= 1

        if counter[0] <= 0:
            return
        board1 = copy.deepcopy(board2)


def main():
    screenParams = {
        "dimensions": [800, 800],
        "caption": "Color Average",
        "bgColor": (31, 33, 42),
        "size": 10,
    }

    running = True
    runChk = False

    counter = 100

    screen = screenDefine(screenParams)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                running = False
        if not runChk:
            initBoardAnim(screen, screenParams)
            animate(screen, screenParams, [counter])

            running = False

            runChk = True
        pygame.display.update()

        if counter <= 0:
            running = False
    pygame.quit()


if __name__ == "__main__":
    main()
