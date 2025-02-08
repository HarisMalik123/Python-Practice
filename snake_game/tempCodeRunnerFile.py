
        s.increase_score()
        snake.extend()
    if snake.head.xcor()>280 or snake.head.xcor()< -280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        s.reset()
        snake.reset()
    for segment in snake.segments[1:]: