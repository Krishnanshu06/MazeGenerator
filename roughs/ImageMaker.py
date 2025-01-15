from PIL import Image, ImageDraw

def grid_to_image(grid, pixel_size=50, cell_border=2, output_file="output.png"):
    """
    Converts a grid to an image, where '#' is black, ' ' is white, 'A' is red, and 'B' is green.

    Parameters:
        grid (list of lists): The grid to convert.
        pixel_size (int): The size of each cell in the output image.
        cell_border (int): The size of the border around each cell.
        output_file (str): The file name to save the output image.

    Returns:
        None
    """
    # Validate the input
    if not grid:
        raise ValueError("Input grid is empty.")

    rows = len(grid)
    cols = len(grid[0])

    if not all(len(row) == cols for row in grid):
        raise ValueError("Input grid must have consistent row lengths.")

    # Create a new image
    img = Image.new("RGBA", (cols * pixel_size, rows * pixel_size), "black")
    draw = ImageDraw.Draw(img)

    # Draw each cell based on the grid
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == '#':
                fill = (40, 40, 40)  # Wall
            elif char == 'A':
                fill = (255, 0, 0)  # Start
            elif char == 'B':
                fill = (0, 171, 28)  # Goal
            else:
                fill = (237, 240, 252)  # Empty cell

            # Draw cell with borders
            draw.rectangle(
                [
                    (x * pixel_size + cell_border, y * pixel_size + cell_border),
                    ((x + 1) * pixel_size - cell_border, (y + 1) * pixel_size - cell_border)
                ],
                fill=fill
            )

    # Save the image
    img.save(output_file)
    print(f"Image saved as {output_file}")

# Example grid
example_grid = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', 'A', ' ', ' ', ' ', '#', '#', '#', ' ', '#', ' ', '#', '#'],
    ['#', ' ', '#', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', ' ', '#', ' ', ' ', '#', '#', ' ', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', '#', '#', ' ', '#'],
    ['#', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', '#', ' ', '#', ' ', 'B', '#', ' ', '#', ' ', '#'],
    ['#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', ' ', '#'],
    ['#', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', ' ', '#'],
    ['#', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]

# Convert the example grid to an image
grid_to_image(example_grid)
