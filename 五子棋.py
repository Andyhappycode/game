import sys
import random
import pygame
import time

pygame.display.set_caption('五子棋')
# 画棋盘
def draw_chessboard():
    window.fill((219, 182, 123))
    # pygame.draw.rect(window, (0, 0, 0), (2, 2, 758, 758), 4)
    pygame.draw.rect(window, (0, 0, 0), (20, 20, 720, 720), 2)
    for x in range(1, 18):
        pygame.draw.line(window, (0, 0, 0), (x * 40 + 20, 20), (x * 40 + 20, 739), 2)
    for y in range(1, 18):
        pygame.draw.line(window, (0, 0, 0), (20, y * 40 + 20), (739, y * 40 + 20), 2)
    pygame.draw.circle(window, (0, 0, 0), (141, 141), 6, 0)
    pygame.draw.circle(window, (0, 0, 0), (381, 141), 6, 0)
    pygame.draw.circle(window, (0, 0, 0), (621, 141), 6, 0)
    pygame.draw.circle(window, (0, 0, 0), (141, 381), 6, 0)
    pygame.draw.circle(window, (0, 0, 0), (381, 381), 6, 0)
    pygame.draw.circle(window, (0, 0, 0), (621, 381), 6, 0)
    pygame.draw.circle(window, (0, 0, 0), (141, 621), 6, 0)
    pygame.draw.circle(window, (0, 0, 0), (381, 621), 6, 0)
    pygame.draw.circle(window, (0, 0, 0), (621, 621), 6, 0)
    text = font_30.render(tips, True, (255, 255, 255))
    window.blit(text, (760, 365))


# 刷新棋盘
def chessboard_refresh():
    draw_chessboard()
    for black_coordinate in black_coordinate_list:
        pygame.draw.circle(window, (0, 0, 0),
                           ((black_coordinate[0] - 1) * 40 + 21, (black_coordinate[1] - 1) * 40 + 21), 17, 0)
    for white_coordinate in white_coordinate_list:
        pygame.draw.circle(window, (255, 255, 255),
                           ((white_coordinate[0] - 1) * 40 + 21, (white_coordinate[1] - 1) * 40 + 21), 17, 0)


# 将鼠标点击坐标转换成棋盘坐标
def mouse_coordinate_to_chessboard_coordinate(mouse_x, mouse_y):
    if mouse_x > 762 or mouse_y > 762:
        return "out of range"
    else:
        return int((mouse_x - 2) / 40) + 1, int((mouse_y - 2) / 40) + 1


# 放置棋子
def place_chess(chessboard_coordinate_f, side_f):
    if side_f == "black":
        black_coordinate_list.append(chessboard_coordinate_f)
    if side_f == "white":
        white_coordinate_list.append(chessboard_coordinate_f)


# 检查是否有某一方胜利
def check_chess():
    winner = " "
    for x in range(1, 20):
        for y in range(1, 20):
            # 检查白子
            count = 0
            for near_x in range(-2, 3):
                if (x + near_x, y) in white_coordinate_list:
                    count += 1
                if count == 5:
                    winner = "white"
            count = 0
            for near_y in range(-2, 3):
                if (x, y + near_y) in white_coordinate_list:
                    count += 1
                if count == 5:
                    winner = "white"
            count = 0
            for near in range(-2, 3):
                if (x + near, y + near) in white_coordinate_list:
                    count += 1
                if count == 5:
                    winner = "white"
            count = 0
            for near in range(-2, 3):
                if (x + near, y - near) in white_coordinate_list:
                    count += 1
                if count == 5:
                    winner = "white"
            # 检查黑子
            count = 0
            for near_x in range(-2, 3):
                if (x + near_x, y) in black_coordinate_list:
                    count += 1
                if count == 5:
                    winner = "black"
            count = 0
            for near_y in range(-2, 3):
                if (x, y + near_y) in black_coordinate_list:
                    count += 1
                if count == 5:
                    winner = "black"
            count = 0
            for near in range(-2, 3):
                if (x + near, y + near) in black_coordinate_list:
                    count += 1
                if count == 5:
                    winner = "black"
            count = 0
            for near in range(-2, 3):
                if (x + near, y - near) in black_coordinate_list:
                    count += 1
                if count == 5:
                    winner = "black"
    return winner


# 白子下此坐标，能赢的机会
def the_chance_to_win(x, y):  # edge_■ empty_▫ black_● white_◌
    global text_tp
    total_chance = 0
    text_tp += "水平方向:" + "\n"

    # 水平方向，堵住黑子的个数
    # 先获得该坐标附近9点的状态
    chess_list_first = []
    for i in range(-4, 5):
        if i == 0:
            chess_list_first.append("◉")
        elif x + i < 1 or x + i > 19:
            chess_list_first.append("■")
        elif (x + i, y) in black_coordinate_list:
            chess_list_first.append("●")
        elif (x + i, y) in white_coordinate_list:
            chess_list_first.append("◌")
        else:
            chess_list_first.append("▫")

    # 列表n1：排除从中间开始，已被白子挡住的黑子
    list_slice_head = 0
    list_slice_end = 9
    for i in range(1, 5):
        if chess_list_first[4 - i] == "◌" or chess_list_first[4 - i] == "■":
            if list_slice_head == 0:
                list_slice_head = 5 - i
        if chess_list_first[4 + i] == "◌" or chess_list_first[4 + i] == "■":
            if list_slice_end == 9:
                list_slice_end = 4 + i
    chess_list_n1 = chess_list_first[list_slice_head:list_slice_end]

    # 列表n2：从中间开始，与当前坐标紧紧相连的黑子
    list_slice_head = 0
    list_slice_end = 9
    for i in range(1, 5):
        if chess_list_first[4 - i] == "▫" or chess_list_first[4 - i] == "◌":
            if list_slice_head == 0:
                list_slice_head = 5 - i
        if chess_list_first[4 + i] == "▫" or chess_list_first[4 + i] == "◌":
            if list_slice_end == 9:
                list_slice_end = 4 + i
    chess_list_n2 = chess_list_first[list_slice_head:list_slice_end]

    du_zhu = 1
    try:
        if (x + list_slice_head - 5, y) in white_coordinate_list or x + list_slice_head - 5 < 1:
            du_zhu += 0.5
    except:
        pass
    try:
        if (x + list_slice_end - 4, y) in white_coordinate_list or x + list_slice_end - 4 > 19:
            du_zhu += 0.5
    except:
        pass
    total_chance += chess_list_n2.count("●") * chess_list_n2.count("●")
    total_chance += chess_list_n1.count("●")

    if chess_list_n2.count("●") == 3 and du_zhu <= 1:
        total_chance += 99999
    if chess_list_n2.count("●") == 4 and du_zhu <= 1.5:
        total_chance += 99999
    if chess_list_n2.count("●") == 5 and du_zhu <= 2:
        total_chance += 114514

    try:
        total_chance /= du_zhu
    except:
        pass

    text_tp += "chess_list_first:" + str(chess_list_first) + "\n"
    text_tp += "chess_list_n1:" + str(chess_list_n1) + "\n"
    text_tp += "chess_list_n2:" + str(chess_list_n2) + "\n"

    # --------------------------------------------------------------------------------

    text_tp += "竖直方向:" + "\n"

    # 竖直方向，堵住黑子的个数
    # 先获得该坐标附近9点的状态
    chess_list_first = []
    for i in range(-4, 5):
        if i == 0:
            chess_list_first.append("◉")
        elif y + i < 1 or y + i > 19:
            chess_list_first.append("■")
        elif (x, y + i) in black_coordinate_list:
            chess_list_first.append("●")
        elif (x, y + i) in white_coordinate_list:
            chess_list_first.append("◌")
        else:
            chess_list_first.append("▫")

    # 列表n1：排除从中间开始，已被白子挡住的黑子
    list_slice_head = 0
    list_slice_end = 9
    for i in range(1, 5):
        if chess_list_first[4 - i] == "◌" or chess_list_first[4 - i] == "■":
            if list_slice_head == 0:
                list_slice_head = 5 - i
        if chess_list_first[4 + i] == "◌" or chess_list_first[4 + i] == "■":
            if list_slice_end == 9:
                list_slice_end = 4 + i
    chess_list_n1 = chess_list_first[list_slice_head:list_slice_end]

    # 列表n2：从中间开始，与当前坐标紧紧相连的黑子
    list_slice_head = 0
    list_slice_end = 9
    for i in range(1, 5):
        if chess_list_first[4 - i] == "▫" or chess_list_first[4 - i] == "◌":
            if list_slice_head == 0:
                list_slice_head = 5 - i
        if chess_list_first[4 + i] == "▫" or chess_list_first[4 + i] == "◌":
            if list_slice_end == 9:
                list_slice_end = 4 + i
    chess_list_n2 = chess_list_first[list_slice_head:list_slice_end]

    du_zhu = 1
    try:
        if (x, y + list_slice_head - 5) in white_coordinate_list or y + list_slice_head - 5 < 1:
            du_zhu += 0.5
    except:
        pass
    try:
        if (x, y + list_slice_end - 4) in white_coordinate_list or y + list_slice_end - 4 > 19:
            du_zhu += 0.5
    except:
        pass
    total_chance += chess_list_n2.count("●") * chess_list_n2.count("●")
    total_chance += chess_list_n1.count("●")

    if chess_list_n2.count("●") == 3 and du_zhu <= 1:
        total_chance += 99999
    if chess_list_n2.count("●") == 4 and du_zhu <= 1.5:
        total_chance += 99999
    if chess_list_n2.count("●") == 5 and du_zhu <= 2:
        total_chance += 114514

    try:
        total_chance /= du_zhu
    except:
        pass

    text_tp += "chess_list_first:" + str(chess_list_first) + "\n"
    text_tp += "chess_list_n1:" + str(chess_list_n1) + "\n"
    text_tp += "chess_list_n2:" + str(chess_list_n2) + "\n"

    # --------------------------------------------------------------------------------

    text_tp += "斜向下方向:" + "\n"

    # 斜向下方向，堵住黑子的个数
    # 先获得该坐标附近9点的状态
    chess_list_first = []
    for i in range(-4, 5):
        if i == 0:
            chess_list_first.append("◉")
        elif x + i < 1 or x + i > 19 or y + i < 1 or y + i > 19:
            chess_list_first.append("■")
        elif (x + i, y + i) in black_coordinate_list:
            chess_list_first.append("●")
        elif (x + i, y + i) in white_coordinate_list:
            chess_list_first.append("◌")
        else:
            chess_list_first.append("▫")

    # 列表n1：排除从中间开始，已被白子挡住的黑子
    list_slice_head = 0
    list_slice_end = 9
    for i in range(1, 5):
        if chess_list_first[4 - i] == "◌" or chess_list_first[4 - i] == "■":
            if list_slice_head == 0:
                list_slice_head = 5 - i
        if chess_list_first[4 + i] == "◌" or chess_list_first[4 + i] == "■":
            if list_slice_end == 9:
                list_slice_end = 4 + i
    chess_list_n1 = chess_list_first[list_slice_head:list_slice_end]

    # 列表n2：从中间开始，与当前坐标紧紧相连的黑子
    list_slice_head = 0
    list_slice_end = 9
    for i in range(1, 5):
        if chess_list_first[4 - i] == "▫" or chess_list_first[4 - i] == "◌":
            if list_slice_head == 0:
                list_slice_head = 5 - i
        if chess_list_first[4 + i] == "▫" or chess_list_first[4 + i] == "◌":
            if list_slice_end == 9:
                list_slice_end = 4 + i
    chess_list_n2 = chess_list_first[list_slice_head:list_slice_end]

    du_zhu = 1
    try:
        if (x + list_slice_head - 5,
            y + list_slice_head - 5) in white_coordinate_list or x + list_slice_head - 5 < 1 or y + list_slice_head - 5 < 1:
            du_zhu += 0.5
    except:
        pass
    try:
        if (x + list_slice_end - 4,
            y + list_slice_end - 4) in white_coordinate_list or x + list_slice_end - 4 > 19 or y + list_slice_end - 4 > 19:
            du_zhu += 0.5
    except:
        pass
    total_chance += chess_list_n2.count("●") * chess_list_n2.count("●")
    total_chance += chess_list_n1.count("●")

    if chess_list_n2.count("●") == 3 and du_zhu <= 1:
        total_chance += 99999
    if chess_list_n2.count("●") == 4 and du_zhu <= 1.5:
        total_chance += 99999
    if chess_list_n2.count("●") == 5 and du_zhu <= 2:
        total_chance += 114514

    try:
        total_chance /= du_zhu
    except:
        pass

    text_tp += "chess_list_first:" + str(chess_list_first) + "\n"
    text_tp += "chess_list_n1:" + str(chess_list_n1) + "\n"
    text_tp += "chess_list_n2:" + str(chess_list_n2) + "\n"

    # --------------------------------------------------------------------------------

    text_tp += "斜向上方向:" + "\n"

    # 斜向上方向，堵住黑子的个数
    # 先获得该坐标附近9点的状态
    chess_list_first = []
    for i in range(-4, 5):
        if i == 0:
            chess_list_first.append("◉")
        elif x + i < 1 or x + i > 19 or y - i < 1 or y - i > 19:
            chess_list_first.append("■")
        elif (x + i, y - i) in black_coordinate_list:
            chess_list_first.append("●")
        elif (x + i, y - i) in white_coordinate_list:
            chess_list_first.append("◌")
        else:
            chess_list_first.append("▫")

    # 列表n1：排除从中间开始，已被白子挡住的黑子
    list_slice_head = 0
    list_slice_end = 9
    for i in range(1, 5):
        if chess_list_first[4 - i] == "◌" or chess_list_first[4 - i] == "■":
            if list_slice_head == 0:
                list_slice_head = 5 - i
        if chess_list_first[4 + i] == "◌" or chess_list_first[4 + i] == "■":
            if list_slice_end == 9:
                list_slice_end = 4 + i
    chess_list_n1 = chess_list_first[list_slice_head:list_slice_end]

    # 列表n2：从中间开始，与当前坐标紧紧相连的黑子
    list_slice_head = 0
    list_slice_end = 9
    for i in range(1, 5):
        if chess_list_first[4 - i] == "▫" or chess_list_first[4 - i] == "◌":
            if list_slice_head == 0:
                list_slice_head = 5 - i
        if chess_list_first[4 + i] == "▫" or chess_list_first[4 + i] == "◌":
            if list_slice_end == 9:
                list_slice_end = 4 + i
    chess_list_n2 = chess_list_first[list_slice_head:list_slice_end]

    du_zhu = 1
    try:
        if (x + list_slice_head - 5,
            y - list_slice_head + 5) in white_coordinate_list or x + list_slice_head - 5 < 1 or y - list_slice_head + 5 < 1:
            du_zhu += 0.5
    except:
        pass
    try:
        if (x + list_slice_end - 4,
            y - list_slice_end + 4) in white_coordinate_list or x + list_slice_end - 4 > 19 or y - list_slice_end + 4 > 19:
            du_zhu += 0.5
    except:
        pass
    total_chance += chess_list_n2.count("●") * chess_list_n2.count("●")
    total_chance += chess_list_n1.count("●")

    if chess_list_n2.count("●") == 3 and du_zhu <= 1:
        total_chance += 99999
    if chess_list_n2.count("●") == 4 and du_zhu <= 1.5:
        total_chance += 99999
    if chess_list_n2.count("●") == 5 and du_zhu <= 2:
        total_chance += 114514

    try:
        total_chance /= du_zhu
    except:
        pass

    text_tp += "chess_list_first:" + str(chess_list_first) + "\n"
    text_tp += "chess_list_n1:" + str(chess_list_n1) + "\n"
    text_tp += "chess_list_n2:" + str(chess_list_n2) + "\n"

    # --------------------------------------------------------------------------------

    if (x, y) in black_coordinate_list or (x, y) in white_coordinate_list:
        total_chance = -1

    return total_chance


# 初始化
pygame.init()
part_add = 0
delta_list_add = 1
black_coordinate_list = []
white_coordinate_list = []
tips = " "
game_mode = "start"
window = pygame.display.set_mode((1000, 762))
font_30 = pygame.font.Font("C:\\Windows\\Fonts\\simhei.ttf", 30)
draw_chessboard()
pygame.display.flip()
side = "black"

# 主循环
while True:
    for event in pygame.event.get():
        # 检测退出
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # 按空格重开
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                black_coordinate_list = []
                white_coordinate_list = []
                tips = " "
                game_mode = "start"
                draw_chessboard()
                pygame.display.flip()
                side = "black"
        # 鼠标按下后
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_mode == "end":
                black_coordinate_list = []
                white_coordinate_list = []
                tips = " "
                game_mode = "start"
                draw_chessboard()
                pygame.display.flip()
                side = "black"
            chessboard_coordinate = mouse_coordinate_to_chessboard_coordinate(event.pos[0], event.pos[1])
            if not chessboard_coordinate == "out of range":
                if chessboard_coordinate not in black_coordinate_list and chessboard_coordinate not in white_coordinate_list:
                    place_chess(chessboard_coordinate, side)
                    total_chance = 0
                    chance_xy = [(10, 10)]
                    text_tp = ""
                    text_tp += "edge_■ empty_▫ black_● white_◌\n"
                    # 逐一计算每个坐标的概率
                    for x in range(1, 20):
                        for y in range(1, 20):
                            text_tp += "--------------------------------------------------\n坐标：(" + str(
                                x) + "," + str(y) + ")\n"
                            self_chance = the_chance_to_win(x, y)
                            text_tp += "总共\nchance:" + str(self_chance) + "\n"
                            if self_chance > total_chance:
                                total_chance = self_chance
                                chance_xy = [(x, y)]
                            elif self_chance == total_chance:
                                chance_xy.append((x, y))
                    # 下面这行启用后，会输出7000行多的内容，感兴趣的可自行查看（可能会非常卡）
                    # print(text_tp)
                    last_chance_xy = random.choice(chance_xy)
                    place_chess(last_chance_xy, "white")
                    side = "black"
                    if check_chess() == "black":
                        tips = "黑棋获胜"
                        game_mode = "end"
                        time.sleep(5)
                    elif check_chess() == "white":
                        tips = "白棋获胜"
                        game_mode = "end"
                    draw_chessboard()
                    chessboard_refresh()
                    pygame.display.flip()