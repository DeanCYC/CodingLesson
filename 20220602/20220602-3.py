#在視窗中繪圖

import pygame


def main():
    # 初始化導入的pygame中的模塊
    pygame.init()
    # 初始化用於顯示的視窗並設置視窗尺寸
    screen = pygame.display.set_mode((800, 600))
    # 設置當前視窗的標題
    pygame.display.set_caption('大球吃小球')
    # 設置視窗的背景色(顏色是由紅綠藍三原色構成的元組)
    screen.fill((242, 242, 242))
    # 繪製一個圓(參數分別是: 屏幕, 顏色, 圓心位置, 半徑, 0表示填充圓)
    pygame.draw.circle(screen, (255, 0, 0,), (100, 100), 30, 0)
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