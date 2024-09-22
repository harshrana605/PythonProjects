from PIL import Image, ImageDraw, ImageFont

# Text to convert
text = """

1. Node.js (Express.js)
Why: You already know JavaScript, so learning Node.js would allow you to use the same language for both frontend and backend. It's lightweight, flexible, and perfect for fast prototyping, hackathons, or even complex projects.
Learning Curve: Moderate (since you know JavaScript)
Usage: Ideal for web apps, APIs, small-scale projects, and real-time applications.
Future Scope: You can move to more structured Node.js frameworks like Nest.js once you get comfortable.
2. Flask (Python)
Why: You’ve shown interest in Flask for a hackathon. Flask is minimalist and flexible, allowing you to build projects quickly without a steep learning curve. You’ll also find Python’s readability very beginner-friendly.
Learning Curve: Easy to Moderate (Python is simpler to pick up and Flask has straightforward concepts)
Usage: Great for small to mid-sized projects, APIs, or applications with a simple architecture.
Future Scope: You can later explore more complex frameworks like Django if your projects require more structure or scalability.
3. FastAPI (Python)
Why: If you enjoy Flask, you’ll like FastAPI as it’s faster, more modern, and built for high-performance APIs. It's growing rapidly in popularity and is very intuitive.
Learning Curve: Moderate (similar to Flask but focuses more on APIs and performance)
Usage: Best for building APIs that need to scale, including machine learning services.
4. Go (Gin or Fiber)
Why: If you are looking for performance and concurrency, Go is one of the best options. It's fast, lightweight, and ideal for highly scalable systems.
Learning Curve: Moderate (Go is easy to learn but a bit different from JavaScript/Python)
Usage: Suitable for building scalable, high-performance applications (APIs, microservices).
5. Spring Boot (Java)
Why: If you want to work on enterprise-level applications, Spring Boot is a powerful framework. It is mature, widely used, and ideal for large-scale backend systems.
Learning Curve: Moderate to Hard (Java itself is verbose, but Spring Boot offers a lot of features and automations)
Usage: Suitable for large, complex web applications, enterprise projects, or systems requiring strong security and scalability.
"""

# Set A4 page size in pixels at 72 DPI
img_width, img_height = 595, 842

# Create an image with A4 dimensions
img = Image.new('RGB', (img_width, img_height), color=(255, 255, 255))

# Initialize drawing on the image
d = ImageDraw.Draw(img)

# Path to your handwriting-style font
font_path = "C:\\Users\\Harsh Rana\\Downloads\\Newzfolder2\\IndieFlower-Regular.ttf"
font = ImageFont.truetype(font_path, 20)  # Reduced font size to 20

# Set text starting position with padding (e.g., 20 pixels from the left)
x, y = 20, 20
line_height = 30  # Reduced line height due to smaller font size

# Write text on the image, with word wrapping to fit the image width
left_padding = 20  # Set left padding here
max_width = img_width - left_padding   # Adjust margin on both sides

for line in text.split('\n'):
    # If the line is too long, split it into multiple lines
    words = line.split(' ')
    current_line = ""
    for word in words:
        # Check the width of the current line with the new word using textbbox
        test_line = current_line + word + " "
        test_bbox = d.textbbox((x, y), test_line, font=font)
        test_width = test_bbox[2] - test_bbox[0]  # Calculate the width
        if test_width <= max_width:
            current_line = test_line
        else:
            d.text((x, y), current_line, font=font, fill=(0, 0, 0))
            y += line_height
            current_line = word + " "
    # Draw the last line
    if current_line:
        d.text((x, y), current_line, font=font, fill=(0, 0, 0))
        y += line_height

# Save the image as a PNG
img.save("handwriting_output_A4_left_padded_small_font.png")

print("Handwriting image saved as handwriting_output_A4_left_padded_small_font.png")
