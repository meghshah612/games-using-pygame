"""Physics and input handling for Pong."""
import constants


def handle_collision(ball, left_paddle, right_paddle):
    if ball.y + ball.radius >= constants.HEIGHT:
        ball.y_vel *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1

    if ball.x_vel < 0:
        if left_paddle.y <= ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_vel *= -1

                middle_y = left_paddle.y + left_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (left_paddle.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel

    else:
        if right_paddle.y <= ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_vel *= -1

                middle_y = right_paddle.y + right_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (right_paddle.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel


def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys["w"] and left_paddle.y - left_paddle.VEL >= 0:
        left_paddle.move(up=True)
    if keys["s"] and left_paddle.y + left_paddle.VEL + left_paddle.height <= constants.HEIGHT:
        left_paddle.move(up=False)

    if keys["up"] and right_paddle.y - right_paddle.VEL >= 0:
        right_paddle.move(up=True)
    if keys["down"] and right_paddle.y + right_paddle.VEL + right_paddle.height <= constants.HEIGHT:
        right_paddle.move(up=False)
