#加載圖像
#如果需要直接加載圖像到視窗上，可以使用pygame中image模塊的函數來加載圖像，再通過之前獲得的視窗對象的blit方法渲染圖像，代碼如下所示。

import pygame


def main():
    # 初始化導入的pygame中的模塊
    pygame.init()
    # 初始化用於顯示的視窗並設置視窗尺寸
    screen = pygame.display.set_mode((800, 600))
    # 設置當前視窗的標題
    pygame.display.set_caption('大球吃小球')
    # 設置視窗的背景色(顏色是由紅綠藍三原色構成的元組)
    screen.fill((255, 255, 255))
    # 通過指定的文件名加載圖像
    ball_image = pygame.image.load('./res/ball.png')
    # 在視窗上渲染圖像
    screen.blit(ball_image, (50, 50))
    # 刷新當前視窗(渲染視窗將繪製的圖像呈現出來)
    pygame.display.flip()
    running = True
    # 開啟一個事件循環處理髮生的事件
    while running:
        # 從消息隊列中獲取事件並對事件進行處理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()