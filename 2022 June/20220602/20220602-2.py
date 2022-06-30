#製作遊戲視窗
import pygame


def main():
    # 初始化導入的pygame中的模塊
    pygame.init()
    # 初始化用於顯示的視窗並設置視窗尺寸
    screen = pygame.display.set_mode((800, 600))
    # 設置當前視窗的標題
    pygame.display.set_caption('大球吃小球')
    running = True
    # 開啟一個事件循環處理髮生的事件
    while running:
        # 從消息隊列中獲取事件並對事件進行處理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()