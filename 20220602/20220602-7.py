#事件處理

def main():
    # 定義用來裝所有球的容器
    balls = []
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
            # 處理鼠標事件的代碼
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # 獲得點擊鼠標的位置
                x, y = event.pos
                radius = randint(10, 100)
                sx, sy = randint(-10, 10), randint(-10, 10)
                color = Color.random_color()
                # 在點擊鼠標的位置創建一個球(大小、速度和顏色隨機)
                ball = Ball(x, y, radius, sx, sy, color)
                # 將球添加到列表容器中
                balls.append(ball)
        screen.fill((255, 255, 255))
        # 取出容器中的球 如果沒被吃掉就繪製 被吃掉了就移除
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)
        pygame.display.flip()
        # 每隔50毫秒就改變球的位置再刷新視窗
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            # 檢查球有沒有吃到其他的球
            for other in balls:
                ball.eat(other)


if __name__ == '__main__':
    main()