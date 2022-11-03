
visited={}
islands={}
matrix=[[1,0,0,0,0,0],
        [0,1,0,1,1,1],
        [0,0,1,0,1,0],
        [1,1,0,0,1,0],
        [1,0,1,1,0,0],
        [1,0,0,0,0,1]]

def update_islands():
        #first and last row
        for i in [0,len(matrix)-1]:
                for j in range(len(matrix)):
                        if (i,j) not in visited and matrix[i][j] == 1:
                                step((i,j))
        #first and last column
        for i in [0, len(matrix) - 1]:
                for j in range(len(matrix)):
                        if (j, i) not in visited and matrix[j][i] == 1:
                                step((j, i))


def remove_islands():
        for i in range(len(matrix)):
                for j in range(len(matrix)):
                        if (i,j) not in islands:
                                matrix[i][j]=0

def step(coordinates: tuple):   #dfs step
        if 0<=coordinates[0]<=len(matrix)-1 and 0<=coordinates[1]<=len(matrix)-1:
                visited[coordinates]=True
                islands[coordinates]=True
                steps=get_neighbors(coordinates)
                for (i,j) in steps:
                        if matrix[i][j]==1:
                                step((i,j))
def get_neighbors(coordinates):
        neighbors=[(coordinates[0] - 1, coordinates[1]),
         (coordinates[0], coordinates[1] - 1),
         (coordinates[0], coordinates[1] + 1),
         (coordinates[0] + 1, coordinates[1])]
        neighbors=[neighbor for neighbor in neighbors if ((0<=neighbor[0]<=len(matrix)-1) and (0<=neighbor[1]<=len(matrix)-1))]

        return [neighbor for neighbor in neighbors if neighbor not in visited]

def print_matrix(matrix):
        for row in matrix:
                print(row)
        print('-'*200)

if __name__ == '__main__':
    print_matrix(matrix)
    update_islands()
    remove_islands()
    print_matrix(matrix)


    