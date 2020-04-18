from turtle import *
color('red', 'purple')
begin_fill()
while True:
    forward(150)
    left(105)
    if abs(pos()) < 1:
        break
end_fill()
done()