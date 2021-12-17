from common.text_manipulations import TextParser
def run():

    positions = []
    folds = []
    source = TextParser("day13.txt").load_file_as_list()
    for row in source:

        if row.find("fold") > -1:

            folds.append(row)
        
        elif row.find(",") > -1:

            positions.append(row)
    
    image, ab, first = set(), [0, 0], True

    for position in positions:
        image.add(tuple(map(int, position.split(","))))

    for fold in folds:
        i, j = int(fold[11] == "y"), int(fold[13:])
        ab[i] = j

        for pixel in list(image):
            if pixel[i] > j:
                image.remove(pixel)
                pixel = list(pixel)
                pixel[i] = 2 * j - pixel[i]
                image.add(tuple(pixel))

        if first:
            print(f"Part 1 result: {len(image)}")
            first = False

    print("Part 2:")
    for b in range(ab[1]):
        for a in range(ab[0]):
            
            print(" #"[(a, b) in image], end="")
        print()

if __name__ == "__main__":

    run()    