# Salomon Martinez
# Implementation of normalized cross correlation

# Sample image
image = [
        [0,0,0,0,0,0,0],
        [0,1,1,1,0,0,0],
        [0,1,1,1,0,0,0],
        [0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]
        ]

# Sample template
template = [
        [1,1,1,0],
        [1,1,1,0],
        [1,1,1,0]
        ]

# Getting image and template lengths
x_len = len(image[0])
y_len = len(image)
u_len = len(template[0])
v_len = len(template)

# Result matrix
result = [[-1 for i in range(x_len + u_len - 1)] for j in range(y_len + v_len - 1)]

# Aveage of template values
template_avg = 0

for v in template:
    for u in v:
        template_avg += u

template_avg /= (v_len * u_len)

# Normalized Cross Correlation Matrix
def normxcorr():
    # Looping through result matrix to populate it
    for y in range(len(result)):
        for x in range(len(result[0])):
            # Average of image region under the template
            image_under_temp_avg = 0
            
            for v in range(v_len):
                for u in range(u_len):
                    if (y - v_len + v + 1) >= 0 and (x - u_len + u + 1) >= 0 and (y - v_len + v + 1) < y_len and (x - u_len + u + 1) < x_len:
                        image_under_temp_avg += image[y - v_len + v + 1][x - u_len + u + 1]
            
            image_under_temp_avg /= (v_len * u_len)
            
            # top: sum( (f - f_avg)*(t - t_avg) )
            top = 0
            # bottom_left: sum( (f - f_avg)^2 )
            bottom_left = 0
            # bottom-right: sum( (t - t_avg)^2 )
            bottom_right = 0
            
            # looping through the template for each point in the results matrix
            for v in range(v_len):
                for u in range(u_len):
                    # checking if image indexes are out of bounds
                    if (y - v_len + v + 1) >= 0 and (x - u_len + u + 1) >= 0 and (y - v_len + v + 1) < y_len and (x - u_len + u + 1) < x_len:
                        f = image[y - v_len + v + 1][x - u_len + u + 1] - image_under_temp_avg
                    else:
                        # replace with 0 if out of bounds
                        f = 0 - image_under_temp_avg
                    
                    t = template[v][u] - template_avg
                    top += f*t
                    bottom_left += f**2
                    bottom_right += t**2
            
            # check if top, bottom_left, or bottom_right are zero
            if top != 0 or (bottom_left * bottom_right) != 0:
                result[y][x] = top / ((bottom_left * bottom_right)**0.5)
            else:
                # if so, set value to 0
                result[y][x] = 0
    
    # initializing values for getting the center coords
    # of the template in the image
    maxVal = -1
    maxCoord = [0,0]
    
    # printing the matrix
    print("\nResults Matrix:")
    
    for i in range(len(result)):
        print(["%.3f" % v for v in result[i]])
        
        for j in range(len(result[i])):
            # getting the max value and coords of that value
            if result[i][j] > maxVal:
                maxVal = result[i][j]
                maxCoord = [j - int(u_len / 2),i - int(v_len / 2)]
    
    # printing the max coords
    print("\nCoordinates For Best Match:")
    print(maxCoord)

normxcorr()
