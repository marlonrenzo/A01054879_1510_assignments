def dijkstra(colours):
    for i in range(0, len(colours)):
        if colours[i][0] != 'b':
            colours[i] = colours[i].title()
    colours.sort()
    for i in range(0, len(colours)):
        colours[i] = colours[i].lower()
    print(colours)


def main():
    dijkstra(['blue', 'white', 'blue', 'red', 'red', 'white'])


if __name__ == '__main__':
    main()
