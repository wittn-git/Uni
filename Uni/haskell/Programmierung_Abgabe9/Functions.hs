


f 1 ys _ = ys
f x ( y : ys ) z = if x > z then f ( x - 1) ( x : ys ) z else ( y : ys )